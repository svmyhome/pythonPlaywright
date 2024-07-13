import time

from playwright.sync_api import Page, Request, Route, expect


def test_listen_network(page: Page):
    page.on('request', lambda request: print('>>', request.method, request.url, request.headers))
    page.on('response', lambda response: print('<<', response.status, response.url))
    page.goto('https://osinit.ru/')
    time.sleep(5)


def test_listen_network_abort_pictures(page: Page):
    page.on('request', lambda request: print('>>', request.method, request.url))
    page.on('response', lambda response: print('<<', response.status, response.url))
    page.route("**/*.{png,jpg,jpeg,svg}", lambda route: route.abort())
    page.goto('https://osinit.ru/')
    time.sleep(5)


def test_network_without_changes(page: Page):
    page.route("**/register",
               lambda route: route.continue_(post_data='{"email": "eve.holt@reqres.in", "password": "pistol"}'))
    page.on('request', lambda request: print('>>', request.method, request.url))
    page.on('response', lambda response: print('<<', response.status, response.url))
    page.goto('https://reqres.in/')
    page.get_by_text(' Register - successful ').click()
    time.sleep(5)


def test_network_with_new_data(page: Page):
    page.route("**/register", lambda route: route.continue_(post_data='{"email": "user1","password": "secret"}'))
    page.on('request', lambda request: print('>>', request.method, request.url))
    page.on('response', lambda response: print('<<', response.status, response.url))
    page.goto('https://reqres.in/')
    page.get_by_text(' Register - successful ').click()
    time.sleep(5)


def test_mock_tags_without_changes(page: Page):
    page.on('request', lambda request: print('>>', request.method, request.url, request.headers))
    page.on('response', lambda response: print('<<', response.status, response.url, response.text()))
    page.goto('https://api.realworld.io/api/tags')


def test_mock_with_changes_1(page):
    page.route("**/api/tags", lambda route: route.fulfill(path="../data.json", content_type="application/json",
                                                          status=200, ))
    page.on('response', lambda response: print('<<', response.status, response.url, response.text()))
    page.goto('https://demo.realworld.io/')
    time.sleep(5)

def test_intercepted(page: Page, request):
    def handle_route(route: Route):
        response = route.fetch()
        json = response.json()
        print(json)
        json["tags"] = ["open", "solutions"]
        route.fulfill(json=json)

    page.route("**/api/tags", handle_route)

    response1 = page.goto("https://demo.realworld.io/")
    sidebar = page.locator('css=div.sidebar')
    expect(sidebar.get_by_role('link')).to_contain_text(["open", "solutions"])
    print(response1.url)
    print(response1.headers)
    print(response1.status)
    time.sleep(5)


def test_replace_from_har(page):
    page.goto("https://reqres.in/")
    page.route_from_har("../example.har")
    users_single = page.locator('li[data-id="users-single"]')
    users_single.click()
    response = page.locator('[data-key="output-response"]')
    expect(response).to_contain_text("Voldemar")

import re
from playwright.sync_api import Playwright, sync_playwright, expect, Page


def test_add_todo(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("first task")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("second task")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.pause()
    page.get_by_placeholder("What needs to be done?").fill("third task")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.locator("li").filter(has_text="second task").get_by_label("Toggle Todo").check()


def test_add_todo_with_new_size(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("first task")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("second task")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("third task")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.locator("li").filter(has_text="second task").get_by_label("Toggle Todo").check()


def test_add_todo_count(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder("What needs to be done?").click()
    page.get_by_placeholder("What needs to be done?").fill("first task")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("second task")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("third task")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("third task")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    page.get_by_placeholder("What needs to be done?").fill("eeeeee")
    page.get_by_placeholder("What needs to be done?").press("Enter")
    x1 = page.locator(".toggle").count()
    page.locator("#todoapp >> label:has-text('second task')").click()
    print(x1)


def test_new_page(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_placeholder('What needs to be done?').type('first task')
    page.get_by_placeholder('What needs to be done?').press('Enter')
    page.locator('.new-todo').fill('Second task')
    page.locator('.new-todo').press('Enter')
    page.get_by_text('first task').click()
    print()


def test_check(page: Page):
    page.goto('https://zimaev.github.io/checks-radios/')
    result = page.locator('.form-check input')
    print(result)
    print


def test_role(page: Page):
    page.goto('https://zimaev.github.io/text_input')
    page.locator('#exampleInputEmail1').fill('test@mail.ru')
    page.get_by_title('username').press_sequentially('Vladimir')
    page.get_by_label('Password').type('qazwsx')
    page.get_by_role('checkbox').click()
    print()


def test_or(page: Page):
    page.goto('https://welcome.stepik.org/ru')
    page.get_by_role('button', name='Купить курс в подарок').or_(page.get_by_text('Купить курс в подарок')).click()
    print()


def test_and(page: Page):
    page.goto('https://zimaev.github.io/locatorand/')
    page.get_by_role('button', name='Sing up').and_(page.get_by_title('Sing up today!'))


def test_chain(page: Page):
    page.goto('https://zimaev.github.io/navbar/')
    page.locator('#navbarNavDropdown >> li:has-text("Company")').click()
    page.locator('li:has-text("Company") >> li:has-text("Contact us")').click()


def test_chain_2(page: Page):
    page.goto('https://zimaev.github.io/navbar/')
    navigation = page.locator('#navbarNavDropdown')
    company = page.locator('li:has-text("Company")')
    contact = page.locator('li:has-text("Contact us")')
    navigation.locator(company).click()
    company.locator(contact).click()
    print()


def test_filter_0(page: Page):
    page.goto('https://zimaev.github.io/filter/')
    row_locator = page.locator("tr")
    print(row_locator.filter(has_not=page.get_by_role('button')).count())


def test_filter_1(page: Page):
    page.goto('https://zimaev.github.io/navbar/')
    page.locator('li').filter(has_text='Company').click()


def test_filter_2(page: Page):
    page.goto('https://zimaev.github.io/checks-radios/')
    page.locator('.form-check').filter(has_text='Default checkbox').click()
    print()





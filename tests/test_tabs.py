from playwright.sync_api import Page


def test_tabs_1(page: Page):
    page.goto('https://zimaev.github.io/tabs')
    with page.context.expect_page() as tab:
        page.get_by_text('Переход к Dashboard').click()

    new_tab = tab.value

    assert new_tab.url == 'https://zimaev.github.io/tabs/dashboard/index.html?'
    sign_out = new_tab.locator('.nav-link',has_text='Sign out')
    assert sign_out.is_visible()

def test_tabs_2(page: Page):
    page.goto('https://zimaev.github.io/tabs', timeout=120000)
    page.screenshot(path='./screen/tab.png')
    with page.context.expect_page() as tab:
        page.get_by_text('Переход к allert').click()

    new_window = tab.value
    page.screenshot(path='./screen/new_tab.png')
    new_url = 'https://zimaev.github.io/tabs/modal/modal.html?'
    assert new_window.url ==new_url
    ico_text = new_window.locator('div', has_text='An example alert with an icon').first
    assert ico_text.is_visible()
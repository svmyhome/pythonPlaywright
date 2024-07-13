from playwright.sync_api import Page


def test_several_1(page: Page):
    page.goto('https://zimaev.github.io/checks-radios/')
    print(page.locator('.form-check-label').count())
    page.locator('.form-check-label').nth(0)


def test_check_1(page: Page):
    page.goto('https://zimaev.github.io/checks-radios/')
    page.locator('text="Default checkbox"').check()
    page.locator('#flexCheckChecked').check()
    print(page.get_by_role('radio').count())
    page.get_by_role('radio').nth(0).check()
    page.locator('text="Default checked radio"').check()
    page.locator('#flexSwitchCheckChecked').check()


def test_check_2(page: Page):
    page.goto('https://zimaev.github.io/checks-radios/')
    page.locator('text="Default checkbox"').click()
    page.locator('#flexCheckChecked').click()
    print(page.get_by_role('radio').count())
    page.get_by_role('radio').nth(0).click()
    page.locator('text="Default checked radio"').click()
    page.locator('#flexSwitchCheckChecked').click()
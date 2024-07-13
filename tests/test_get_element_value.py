from playwright.sync_api import Page


def test_get_text_element_values_1(page: Page):
    page.goto('https://zimaev.github.io/table', timeout=120000)
    row = page.locator('tr')
    print(row.all_inner_texts())


def test_get_text_element_values_2(page: Page):
    page.goto('https://zimaev.github.io/table', timeout=120000)
    row = page.locator('tr')
    print(row.all_text_contents())


def test_get_text_element_value_3(page: Page):
    page.goto('https://zimaev.github.io/table', timeout=120000)
    row = page.locator('td').first
    print(row.inner_text())


def test_get_text_element_value_4(page: Page):
    page.goto('https://zimaev.github.io/table', timeout=120000)
    row = page.locator('td').nth(4)
    print(row.text_content())

def test_get_html_element_value_4(page: Page):
    page.goto('https://zimaev.github.io/table', timeout=120000)
    row = page.locator('td').nth(4)
    print(row.inner_html())
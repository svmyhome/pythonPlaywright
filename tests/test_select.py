from playwright.sync_api import Page


def test_select_1(page: Page):
    page.goto('https://zimaev.github.io/select/')
    page.select_option('#floatingSelect', value='3')
    page.select_option('#floatingSelect', index=1)
    page.select_option('#floatingSelect', label='Нашел и завел bug')


def test_select_2(page: Page):
    page.goto('https://zimaev.github.io/select/')
    page.select_option('#skills', value=['playwright', 'python'])
    page.select_option('#skills', index=[0, 3])
    page.select_option('#skills', label=['Git', 'Docker'])
from playwright.sync_api import Page


def test_drag_drop(page: Page):
    page.goto('https://zimaev.github.io/draganddrop/')
    page.drag_and_drop('#drag', '#drop')

from playwright.sync_api import Page


def test_load_file_1(page: Page):
    page.goto('https://zimaev.github.io/upload/')
    page.set_input_files('#formFile', 'hello.txt')
    page.get_by_role('button', name='Upload').click()


def test_load_file_2(page: Page):
    page.goto('https://zimaev.github.io/upload/')
    page.on("filechooser", lambda file_chooser: file_chooser.set_files("hello.txt"))
    page.locator("#file-submit").click()


def test_load_file_3(page: Page):
    page.goto('https://zimaev.github.io/upload/')
    with page.expect_file_chooser() as fc_info:
        page.locator("#file-submit").click()
    file_chooser = fc_info.value
    file_chooser.set_files('hello.txt')

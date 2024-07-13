from playwright.sync_api import Page


def test_dialogs_1(page: Page):
    page.goto("https://zimaev.github.io/dialog/")
    page.get_by_text("Диалог Alert").click()
    page.get_by_text("Диалог Confirmation").click()
    page.get_by_text("Диалог Prompt").click()


def test_dialogs_2(page: Page):
    page.goto("https://zimaev.github.io/dialog/")
    page.on('dialog', lambda dialog: dialog.accept())
    page.on("dialog", lambda dialog: print(dialog.message))
    page.get_by_text("Диалог Confirmation").click()


def test_dialogs_3(page: Page):
    page.goto("https://zimaev.github.io/dialog/")
    page.on('dialog', lambda dialog: dialog.dismiss())
    page.on("dialog", lambda dialog: print(dialog.message))
    page.on("dialog", lambda dialog: print(dialog.type))
    page.get_by_role('button', name="Диалог Confirmation").click()
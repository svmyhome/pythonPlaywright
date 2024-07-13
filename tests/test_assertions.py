from playwright.sync_api import Page, expect



# открыть https://demo.playwright.dev/todomvc/#/
# проверить что открыт корректный url
# найти поле ввода задачи
# проверить что оно пустое
# ввести задачу номер один
# ввести задачу номер два
# проверить что количество задач в списке равно двум
# отметить одну задачу выполненной
# проверить что эта задача отмечена выполненной



def test_assert_1(page: Page) ->None:
    page.goto("https://demo.playwright.dev/todomvc/#/")
    expect(page, 'Такого нет').to_have_url('https://demo.playwright.dev/todomvc/#/')
    input_field = page.locator('.new-todo')
    expect(input_field, 'Поле не пустое').to_be_empty()
    input_field.type('задача номер один')
    input_field.press('Enter')
    input_field.fill('задача номер два')
    input_field.press('Enter')
    list_count = page.locator('.todo-list >> li')
    expect(list_count, 'Количество не равно').to_have_count(2)
    list_count.get_by_role('checkbox').nth(0).click()
    expect(list_count.nth(0), 'Нет законченых').to_have_class('completed')

def test_add_todo(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.locator("h2").is_visible()

def test_add_todo_assert(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    assert page.locator("h2").is_visible()

def test_add_todo_expect(page: Page):
    page.goto("https://demo.playwright.dev/todomvc/#/")
    expect(page.locator('h2')).to_be_visible()
## Python Playwright

### Запись скрипта с помощью Codegen
Это команда откроет два окна:
- Браузер Chromium
- Playwright Inspector  
Далее вы можете выполнить необходимое действие по сценарию в браузере, а codegen запишет и сгенерирует код для выполняемого вами действия.
```bash
playwright codegen demo.playwright.dev/todomvc/#/
```

Размер открываемого окна браузера указывается через аргумент --viewport-size
```bash
playwright codegen --viewport-size=800,600 https://demo.playwright.dev/todomvc/#/
```

Можно сразу указать файл, в который будете сохранен записанный код, добавив -о или --output и указав имя файла.
```bash
playwright codegen -o example_lesson.py https://demo.playwright.dev/todomvc/#/
```
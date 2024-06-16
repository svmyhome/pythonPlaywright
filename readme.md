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

### Playwright CLI

Запуск в режиме headed
```bash
pytest --headed
```
Запускать тесты в другом браузере chromium, firefox или webkit
```bash
pytest --headed --browser webkit --browser firefox
```

Запуск тестов в браузерах Chrome и Edge, установленных непосредственно в системе
```bash
pytest --browser-channel=msedge --headed
```

Замедление выполнения теста на указанное количество миллисекунд
```bash
pytest --headed --slowmo 1000
```
Имитации поведения браузера для определенного устройства [Список](https://github.com/microsoft/playwright/blob/main/packages/playwright-core/src/server/deviceDescriptorsSource.json)
```bash
pytest --headed --device="iPhone 13 Mini"
```

Каталог для артефактов, создаваемых тестами (по умолчанию: test-results) используется вместе с trace и.т.д.
```bash
pytest --headed --device="iPhone 13 Mini" --output=results
```

Записывать ли трассировку для каждого теста. on, off или retain-on-failure (по умолчанию: off)
```bash
pytest --headed --device="iPhone 13 Mini" --output=results --tracing=on
```

Записывать ли видео для каждого теста. on, off или retain-on-failure (по умолчанию: off)
```bash
 pytest --headed --device="iPhone 13 Mini" --video=on
```

Записывать снимок экрана после каждого теста. on, off или only-on-failure (по умолчанию: off).
```bash
pytest --headed --device="iPhone 13 Mini" --screenshot=on
```

Записывать скриншот всей страницы при ошибке. По умолчанию снимается только область просмотра. Требуется, чтобы параметр --screenshot был включен (по умолчанию: off).
```bash
pytest --headed --device="iPhone 13 Mini" --screenshot=on --full-page-screenshot
```
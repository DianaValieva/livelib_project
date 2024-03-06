<h1> Проект по тестированию интернет-сайта о литературе LiveLib.ru</h1>

<a target="_blank" href="https://www.livelib.ru">Ссылка на сайт</a>

### API-тесты
- [x] Авторизация пользователя на сайте
- [x] Изменение статуса книги
- [x] Голосование за рецензию\комментарий

### UI-тесты
- [x] Авторизация пользователя на сайте
- [x] Отправка сообщения авторизованным пользователем
- [x] Поиск книги неавторизованным пользователем
- [x] Изменения данных в разделе книжного вызова


### Проект реализован с использованием:

<img src="resources/icons/python-original.svg" width="50"> <img src="resources/icons/pytest.png" width="50"> <img src="resources/icons/intellij_pycharm.png" width="50"> <img src="resources/icons/selene.png" width="50"> <img src="resources/icons/selenoid.png" width="50"> <img src="resources/icons/jenkins.png" width="50"> <img src="resources/icons/allure_report.png" width="50"> <img src="resources/icons/allure_testops.png" width="50"> <img src="resources/icons/telegram.svg" width="50"> <img src="resources/icons/jira.png" width="50">

----

### Локальный запуск автотестов
1. Клонируйте репозиторий на свой локальный компьютер при помощи git clone
2. Создайте и активируйте виртуальное окружение
  ```bash
  python -m venv .venv
  source .venv/bin/activate
  ```
3. Установите зависимости с помощью pip
  ```bash
  pip install -r requirements.txt
  ```
4. Для запусков тестов локально используйте команд:
  ```bash
  pytest -sv -m mobile tests/mobile/
  pytest -sv -m web
  pytest -sv -m api
  ```

Получение отчёта allure:
```bash
allure serve allure-results
```

----


### Удаленный запуск автотестов выполняется на сервере Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/livelib_project/">Ссылка на проект в Jenkins</a>


#### Параметры сборки

* `comment` - комментарий для оповещения в телеграмме


#### Для запуска автотестов в Jenkins

1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/livelib_project/">проект</a>
2. Выбрать пункт `Build with Parameters`
3. Указать комментарий 
4. Нажать кнопку `Build`
5. Результат запуска сборки можно посмотреть в отчёте Allure
![This is an image](/resources/screenshots/allure_report.png)
----
### Интеграция с Allure TestOps

#### Информация о запуске сборки автотестов
![This is an image](/resources/screenshots/allure_launch.png)

#### Информация о тест-кейсах проекта
![This is an image](/resources/screenshots/allure_test_cases.png)

### Настроено автоматическое оповещение о результатах сборки Jenkins в Telegram-бот
![This is an image](/resources/screenshots/telegram_message.png)

### Пример видеозаписи прохождения  WEB-теста
![This is a пша](/resources/screenshots/video_attach.gif)

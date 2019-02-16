# Simple parser
Простое приложение, которое получает данные о вакансиях со страницы на https://spb.hh.ru/employer/889

# Установка и настройка
### Требования
Необходимо, чтобы в системе был установлен `pytohn 3.6`.

Подразумевается, что в системе установлен свежий `pip`.
### Установка
Получем исходный код проекта:
```sh
$ git clone https://github.com/Nekr0bz/Simple-parser
```
**Настройка окружения** 

Для работоспособности проекта необходимо установить дополнительные модули, перечисленные в файле `requirements.txt`:
```sh
$ pip install -r requirements.txt
```
### База данных
Приложение использует PostgreSQL, настройки которой находятся в `simpleParser/settings.py`.

Создаем базу данных:
```sh
$ python manage.py migrate
```

### Дополнительная настройка
Для управления очередями задач исползуется Celery. В качестве брокера и бэкенда для Celery используется Redis. <br/> 
Изменить эти настройки можно в файлах: `simpleParser/celery.py` и `simpleParser/settings.py`

# Запуск
Перед запуском приложения должен быть запущен **Redis server**.

Запускаем Celery к примеру так:
```sh
$ celery worker -A simpleParser --loglevel=debug
```
Теперь должно работать:
```sh
$ python manage.py runserver
```

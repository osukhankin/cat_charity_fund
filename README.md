# QRkot - приложение для Благотворительного фонда поддержки котиков
## Описание
API - Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.
### Возможности

- Создание/получение/обновление/удаление проектов фонда.
- Создание/получение пожертвований от пользователей.
- Регистрация/аутентификация/авторизация пользователей сервиса

### Технологии

* FastAPI
* SQLAlchemy

## Запуск проекта:
Клонировать репозиторий и перейти в него в командной строке:


```
git clone https://github.com/osukhankin/cat_charity_fund.git
```


Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

В корне проекта создайте `.env` файл
```
APP_TITLE=QRKot
DESCRIPTION=Благотворительный фонд поддержки котиков
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
secret=<секретный ключ>
FIRST_SUPERUSER_EMAIL=<почта суперпользователя>
FIRST_SUPERUSER_PASSWORD=<пароль суперпользователя>
```

Запустите команды для создания базы
```
alembic upgrade head
```

Запуск сервера
```
uvicorn app.main:app --reload
```

## Справка
При первом запуске будет создан заданный в .env суперпользователь 
Сервисом можно воспользоваться через RestApi

### http://localhost:8000/docs/
### http://localhost:8000/redoc/
### API (Docs: [OpenAPI](https://github.com/osukhankin/cat_charity_fund/blob/master/openapi.json))

## Автор
Суханкин Олег - [osukhankin@yandex.ru](mailto:osukhankin@yandex.ru)


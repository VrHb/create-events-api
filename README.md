# Сервис для создания мероприятий

## Как запустить

### Переменные окружения:

Создайте файл `.env`:

```
touch .env
```

1. Секретный ключ проекта:

```
echo "DJANGO_SECRET_KEY=<ключ проекта>" >> .env
```

2. Название директории для статики

```sh
echo "STATIC_DIR_NAME=<название директории>"
```

### Установка c помощью docker

```sh
docker-compose build && docker-compose up -d
```

### Установка вручную

#### Выполните миграции в БД

```sh
python manaage.py makemigrations event_app
python manage.py migrate event_app
python manage.py makemigrations userapp
python manage.py migrate userapp
python manage.py migrate
```

#### Установите бд REDIS

```sh
sudo apt install redis
```

#### Запустите сервер

```sh
python manage.py runserver
```


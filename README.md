# Сервис для создания мероприятий


## Переменные окружения:

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

## Установка c помощью docker

Для запуска сайта нужно установить docker, см. [доку](https://docs.docker.com/engine/install/)

```sh
docker-compose up --build -d
```

```sh
docker-compose exec web -it python manage.py createsuperuser
```

## Как использовать сервис

- Создайте пользователя

Url - http://127.0.0.1:9000/register


- Получите token 

Пример запроса:

```sh
curl \
  --header "Content-Type: application/json" \
  --request POST \
  --data  '{"email":"value1", "password":"value2"}' \
  http://127.0.0.1:9000/api/token/
```

- Создайте событие 

Пример запроса:

```sh
curl \
  --header "Content-Type: application/json" \
  --header "Authorization: Bearer <token>" \
  --request POST \
  --data  '{"title":"Event", "description":"some", "date": "2024-12-23"}' \
  http://127.0.0.1:9000/event/
```

- Создайте организацию 

Пример запроса:

```sh
curl \
  --header "Content-Type: application/json" \
  --header "Authorization: Bearer <token>" \
  --request POST \
  --data  '{"title":"Event", "description":"some", "address": "Some address", "postcode": "188283"}' \
  http://127.0.0.1:9000/organization/
```

- Информация по мероприятию 

Пример запроса:

```sh
curl \
  --header "Content-Type: application/json" \
  --header "Authorization: Bearer <token>" \
  --request GET \
  http://127.0.0.1:9000/event/1/
```

- Список мероприятий 

Пример запроса:

```sh
curl \
  --header "Content-Type: application/json" \
  --header "Authorization: Bearer <token>" \
  --request GET \
  http://127.0.0.1:9000/events/
```

Доступные параметры:

- `search` - поиск по дате, названию и описанию мероприятия
- `ordeting=date` - сортировка по дате проведения
- `page` - пагинация по 5 мероприятий

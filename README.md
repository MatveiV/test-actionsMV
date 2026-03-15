# Time API

Бэкенд на FastAPI для работы со временем: получение текущего времени сервера и конвертация между часовыми поясами.

## Запуск локально

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Запуск через Docker

```bash
docker build -t time-api .
docker run -d -p 8000:8000 time-api
```

## Эндпоинты

### `GET /time`
Возвращает текущее время сервера.

```json
{"server_time": "2026-03-15T20:00:00.000000"}
```

### `GET /date`
Возвращает текущую дату сервера.

```json
{"server_date": "2026-03-15"}
```

### `GET /datetime`
Возвращает дату и время сервера раздельно.

```json
{
  "date": "2026-03-15",
  "time": "20:00:00.000000",
  "datetime": "2026-03-15T20:00:00.000000"
}
```

### `GET /convert`
Конвертирует дату и время из одного часового пояса в другой.

| Параметр       | Тип    | Описание                              | Пример                  |
|----------------|--------|---------------------------------------|-------------------------|
| `datetime_str` | string | Дата и время в формате ISO 8601       | `2026-03-15T20:00:00`   |
| `from_tz`      | string | Исходный часовой пояс (IANA)          | `Europe/Moscow`         |
| `to_tz`        | string | Целевой часовой пояс (IANA)           | `America/New_York`      |

```
GET /convert?datetime_str=2026-03-15T20:00:00&from_tz=Europe/Moscow&to_tz=America/New_York
```

```json
{
  "original": "2026-03-15T20:00:00+03:00",
  "converted": "2026-03-15T13:00:00-04:00",
  "from_tz": "Europe/Moscow",
  "to_tz": "America/New_York"
}
```

## Деплой

При пуше в `main` или открытии Pull Request GitHub Actions запускает три job'а:

1. `check` — устанавливает зависимости и проверяет импорты (запускается на push и PR)
2. `build-and-push` — собирает Docker образ и пушит в GitHub Container Registry (только push в main)
3. `deploy` — подключается к серверу по SSH, пуллит новый образ, проверяет контрольную сумму и перезапускает контейнер если образ изменился (только push в main)

PR в `main` не может быть смержен если job `check` упал.

Продакшн: http://89.111.154.157:8000  
Swagger UI: http://89.111.154.157:8000/docs

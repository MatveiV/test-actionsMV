# Time API

Тестовый бэкенд на FastAPI, возвращающий текущее время сервера.

## Установка

```bash
pip install -r requirements.txt
```

## Запуск

```bash
uvicorn main:app --reload
```

## Использование

```
GET /time
```

Пример ответа:

```json
{
  "server_time": "2026-03-15T12:34:56.789012"
}
```

Документация доступна по адресу: http://127.0.0.1:8000/docs

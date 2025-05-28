# Project For MPS

## Описание
Это учебный проект для курса MPS, реализованный с использованием Django и FastAPI. Проект позволяет создавать и редактировать тексты с подсчётом количества слов. Подсчёт слов выполняется синхронно через вызов FastAPI-сервиса.

## Технологии
- **Django**: Основной фреймворк для веб-приложения с SQLite3 как базой данных.
- **FastAPI**: Используется для подсчёта слов через локальный API.
- **Python**: Версия 3.12.

## Установка
1. Установите зависимости:
   ```bash
   pip3 install -r requirements.txt
   ```
2. Выполните миграции для создания базы данных:
   ```bash
   cd main_service
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```
3. Запустите FastAPI:
   ```bash
   cd /Users/businessbook/Desktop/Project_For_MPS
   uvicorn main:app --host 0.0.0.0 --port 8001
   ```
4. Запустите Django-сервер:
   ```bash
   cd main_service
   python3 manage.py runserver
   ```

## Использование
- Перейдите на `http://localhost:8000/` в браузере.
- Зарегистрируйтесь или войдите, чтобы создать или отредактировать текст через `/create/`.

## Структура проекта
- `main_service/`: Основной Django-проект с моделями, видами и шаблонами.
- `main.py`: Файл FastAPI для подсчёта слов.
- `requirements.txt`: Список зависимостей.

## Автор
- [Ваше имя] (businessbook)

## Статус
Проект завершён. Использованы SQLite3 вместо PostgreSQL, убраны Docker и асинхронность (Celery).

## Дата обновления
28 мая 2025 года
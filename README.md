# Project For MPS

## Описание
Это учебный проект для курса МШП, реализованный с использованием Django и FastAPI. Проект позволяет создавать и редактировать тексты с подсчётом количества слов. Подсчёт слов выполняется синхронно через вызов FastAPI-сервиса.

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
   cd text_processor
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
- Харазян Левон

## Дата обновления
28 мая 2025 года
-------------------------------------
## Description
This is a tutorial project for the MShP course, built using Django and FastAPI. The project allows users to create and edit text, with word count functionality. The word count is calculated synchronously by calling a FastAPI service.

## Technologies
- **Django**: The main framework for the web application, using SQLite3 as the database.
- **FastAPI**: Used for word counting via a local API.
- **Python**: Version 3.12.

## Installation
1. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```
2. Run migrations to create the database:
   ```bash
   cd main_service
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```
3. Start FastAPI:
   ```bash
   cd text_processor
   uvicorn main:app --host 0.0.0.0 --port 8001
   ```
4. Start the Django server:
   ```bash
   cd main_service
   python3 manage.py runserver
   ```

## Usage
- Go to `http://localhost:8000/` in your browser.
- Register or log in to create or edit text via `/create/`.

## Project structure
- `main_service/`: The main Django project with models, views and templates.
- `main.py`: FastAPI file for word counting.
- `requirements.txt`: List of dependencies.

## Author
- Levon Khrazian

## Last updated
28 May 2025

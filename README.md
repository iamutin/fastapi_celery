# FastAPI Celery Integration Example

Пример интеграции FastAPI с Celery для асинхронной обработки задач с поддержкой Docker.

## Описание

Этот проект демонстрирует, как организовать асинхронную обработку задач с помощью Celery в FastAPI приложении с использованием Docker Compose. Основные возможности:

- Отправка задач в Celery из FastAPI
- Отслеживание статуса выполнения задач
- Пример долгой задачи (симуляция)
- Полностью контейнеризированное решение с Redis как брокером сообщений

## Технологии

- Python 3.9+
- FastAPI
- Celery
- Redis
- Docker
- Pydantic Settings для управления конфигурацией

## Структура проекта
# FastAPI Celery Integration Example

Пример интеграции FastAPI с Celery для асинхронной обработки задач с поддержкой Docker.

## Описание

Этот проект демонстрирует, как организовать асинхронную обработку задач с помощью Celery в FastAPI приложении с использованием Docker Compose. Основные возможности:

- Отправка задач в Celery из FastAPI
- Отслеживание статуса выполнения задач
- Пример долгой задачи (симуляция)
- Полностью контейнеризированное решение с Redis как брокером сообщений

## Технологии

- Python 3.12
- FastAPI
- Celery
- Redis
- Docker
- Pydantic Settings для управления конфигурацией


## Быстрый старт

1. Клонировать репозиторий:
   ```bash
   git clone https://github.com/iamutin/fastapi_celery.git
   cd fastapi_celery
   ```

2. Создать файл `.env` на основе примера:
    ```bash
    cp .env.example .env
    ```

3. Запустить сервисы через Docker Compose:
    ```bash
    docker-compose up --build
    ```

После запуска будут доступны:

- FastAPI: http://localhost:8000

- Документация API: http://localhost:8000/docs

- Redis: redis://localhost:6379
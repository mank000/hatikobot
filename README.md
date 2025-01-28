# Система проверки IMEI устройств

Данный проект представляет собой бэкенд-систему для проверки IMEI устройств с интеграцией Telegram-бота и предоставлением REST API. Проект реализован с использованием FastAPI, aiogram и aiohttp.

## Функционал

### 1. Доступ
- **Белый список пользователей для Telegram**: Только пользователи из белого списка могут взаимодействовать с ботом.
- **Авторизация через API**: Доступ к API осуществляется с использованием токенов. Отправляем api, который указан в файле .env!

### 2. Telegram-бот
- Пользователь отправляет боту IMEI.
- Бот проверяет валидность IMEI.
- В ответ отправляется информация о предоставленном IMEI.

### 3. API
- Эндпоинт для проверки IMEI:
  - **Метод**: `POST /api/check-imei`
  - **Параметры запроса**:
    - `deviceId` (строка, обязательный) — IMEI устройства.
    - `serviceId` (строка, обязательный) — номер сервиса.
  - **Ответ**: JSON с информацией о IMEI.

## Установка и запуск

```
git clone <URL_РЕПОЗИТОРИЯ>
```
Для развертывания приложения с использованием Docker:
Создайте .env и заполните его как написано в .env.example

Запустите контейнер:
```
sudo docker-compose up -d
```

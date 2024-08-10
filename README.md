# Skymarket - дипломный проект backend-части для сайта объявлений

## Автор

Равиль Латыпов (группа Python-разработчик 30.0)

## Описание проекта

electronic_sales_network - Этот проект представляет собой веб-приложение с API-интерфейсом и админ-панелью для управления сетью по продаже электроники.
Сеть представляет собой иерархическую структуру, состоящую из заводов, розничных сетей и индивидуальных предпринимателей. Каждый узел сети связан с поставщиком оборудования,
причём уровень иерархии определяется отношением к другим узлам.

## Основной функционал
## Админ-панель
### Просмотр и управление узлами сети:

- Возможность фильтрации объектов по названию города.
- Ссылки на поставщиков для каждого объекта сети.
- Функционал очистки задолженности перед поставщиком.

### Управление контактной информацией:

- Добавление и редактирование контактной информации.

### Управление продуктами:

- Добавление и редактирование информации о продуктах, таких как название, модель и дата выхода на рынок.

## API-интерфейс
### CRUD-операции для узлов сети:

- Создание, просмотр, редактирование и удаление узлов сети.
- Запрещено обновление поля "Задолженность перед поставщиком" через API.
- Фильтрация объектов по стране.

### Права доступа к API:

- Только активные сотрудники могут получить доступ к API.
- Доступ к админ-действиям предоставляется только администраторам.

## Технологии

- Python 3.12
- Django 5.0+
- Django Rest Framework
- PostgreSQL
- Djoser (для аутентификации)

## Установка и запуск

1. Клонируйте репозиторий: **git clone https://github.com/ravcode9/skymarket_diplom**
2. Перейдите в директорию проекта: **cd skymarket_diplom\skymarket**
3. Создайте и активируйте виртуальное окружение: **python -m venv venv**
**source venv/bin/activate**  (Для Linux/MacOS)
**venv\Scripts\activate**  (Для Windows)
4. Установите зависимости: **pip install -r requirements.txt**
5. Создайте файл `.env` в корневой директории проекта. Добавьте переменные окружения из .env.sample со своими значениями
6. Примените миграции: **python manage.py migrate**
7. Запустите сервер: **python manage.py runserver**

## API Эндпоинты

### Звенья сети (NetworkNode)

- **GET /network_nodes/** - Получить список всех звеньев сети
- **POST /network_nodes/** - Создать новое звено сети
- **GET /network_nodes/{id}/** - Получить детали конкретного звена сети
- **PUT /network_nodes/{id}/** - Обновить информацию о звене сети
- **PATCH /network_nodes/{id}/** - Частично обновить информацию о звене сети
- **DELETE /network_nodes/{id}/** - Удалить звено сети

### Дополнительные действия

- **POST /network_nodes/{id}/clear_debt/** - Очистить задолженность конкретного звена сети (только для админов)
- **POST /network_nodes/clear_multiple_debt/** - Очистить задолженность нескольких звеньев сети (только для админов)

- Для авторизации используйте JWT токен через POST localhost:8000/token/, скопируйте и вставьте токен в поле Authorization в Headers в таком виде: "Bearer <ваш токен>"
- Запросы можно отправлять через программу Postman
- 
### Фильтрация

- Фильтрация звеньев сети по стране: `/network_nodes/?country=<название страны>`

### Пользователи
- **^users/$** - Список пользователей (name='users-list')
- **^users/activation/$** - Активация пользователей (name='users-activation')
- **^users/me/$** - Информация о текущем пользователе (name='users-me')
- **^users/resend_activation/$** - Повторная отправка активационного письма (name='users-resend-activation')
- **^users/reset_password/$** - Сброс пароля (name='users-reset-password')
- **^users/reset_password_confirm/$** - Подтверждение сброса пароля (name='users-reset-password-confirm')
- **^users/reset_email/$** - Сброс email (name='users-reset-username')
- **^users/reset_email_confirm/$** - Подтверждение сброса email (name='users-reset-username-confirm')
- **^users/set_password/$** - Установка нового пароля (name='users-set-password')
- **^users/set_email/$** - Установка нового email (name='users-set-username')
- **^users/(?P<id>[^/.]+)/$** - Детали пользователя (name='users-detail')

### Регистрация нового пользователя

**POST** localhost:8000/users/
**Content-Type**: application/json
{
**"email"**: "user@example.com",
**"first_name"**: "string",
**"last_name"**: "string",
**"password"**: "string",
**"phone"**: "string",
**"image"**: "http://example.com"
}

### Создание нового звена

**POST** localhost:8000/network_nodes/
**Content-Type**: application/json
{
    **"id"**: 6,
    **"name"**: "gestore",
    **"contact_info"**: [],
    **"products"**: [],
    **"supplier"**: null,
    **"debt"**: "0.00",
    **"created_at"**: "2024-08-10T12:40:33.333541+05:00",
    **"level**": 0
}

### Документация API

- **GET /swagger/** - Документация API в формате Swagger UI
- **GET /redoc/** - Документация API в формате ReDoc

### Примечания

- Для авторизации используйте JWT токен
- Все запросы к API должны содержать заголовок `Content-Type: application/json`
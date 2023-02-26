### 1. Подготовка
1. Запустить Docker Desktop
2. Убедиться что включен режим Linux Containers
3. Запускать контейнер с базой данных через терминал WSL. 
Для этого открыть терминал Ubuntu в папке проекта с .yml файлом и выполнить команду:

*docker-compose -f run.yml up*

### 2. Миграции alembic

*alembic init migrations*

*alembic revision --autogenerate -m "initial migration"*

*alembic upgrade heads*

### 3. Запуск сервера приложения

*uvicorn app:app --reload*
### 1. Подготовка к запуску на Windows

Открыть терминал Ubuntu (или WSL + Docker Desktop + Linux Containers) 
в папке проекта с .yml файлом и выполнить команды:

*docker-compose -f run.yml up -d*

*docker build -t tree .*

*docker run -p 8000:8000 tree*

### 2. Создать таблицы alembic на основе существующих миграций

Выполнить из каталога ./data, с использованием venv :

*alembic upgrade heads*

### 3. Создать корневой узел root через SQL консоль

*INSERT INTO node (id, name, value, parent) VALUES (1, 'root', null, null);*
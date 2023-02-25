### Запуск
1. Запустить Docker Desktop
2. Убедиться что включен режим Linux Containers
3. Запускать контейнер с базой данных через терминал WSL. 
Для этого открыть терминал Ubuntu в папке проекта с .yml файлом и выполнить команду:

*docker-compose -f run.yml up*

4. запуск приложения

*uvicorn app:app --reload*
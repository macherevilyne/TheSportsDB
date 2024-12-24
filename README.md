Проект The SportsDB API

Для запуска проекта небходимо:
1) установить все зависимости командой pip install -r requirements.txt
2) Выполнить миграции командой: 
-python manage.py makemigrations
-python manage.py migrate
3) Создать суперпользователя командой
-python manage.py createsuperuser
4) Запустить сервер командой
-python manage.py runserver
5) На главной странице пользователю будет предложено создать записи в БД, это для тестов с админой и фильтрами
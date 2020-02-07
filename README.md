1) Clone repo
2) create database real_align_django
3) change mysql user and password under real_align_django/settings.py
4) virtualenv realalign
5) activate the virtualenv
6) pip install -r requirements.txt
7) python manage.py makemigrations
8) python manage.py migrate
9) python manage.py runserver


** sudo apt-get install libmysqlclient-dev
** sudo ufw delete allow 8000
** sudo ufw allow 'Nginx Full'

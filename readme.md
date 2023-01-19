# Simple Django blog

## Initial project

### create virtual environment(venv)
`python -m venv venv`

### activate venv
`source venv/bin/venv`

### install django
`pip install django`

### create django project config in the same directory
`django-admin startproject config .`

### first run the project
`python manage.py runserver`

### create django app blog
`python manage.py startapp blog`

add app 'blog' to config/settings.py into INSTALLED_APPS section

### install python-dotenv
`pip install python-dotenv`

Create .env file from .env_example and copy values SECRET_KEY from settings.py to .env

WARNING 
Don't add .env file to git


## Database init

### first migrate
`python manage.py migrate`

### create model
edit blog/models.py

### create migrations
`python manage.py makemigrations`
`python manage.py migrate`

### create superuser
`python manage.py createsuperuser`

### edit blog/admin.py

## Create views

### edit blog/views.py

### edit urls.py

### add templates dir to settings.py

### add static files (css, js, etc)


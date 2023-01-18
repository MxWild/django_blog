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

## Database init

### first migrate
`python manage.py migrate`

### create model
edit blog/models.py

### create migrations
`python manage.py makemigrations`
`python manage.py migrate`


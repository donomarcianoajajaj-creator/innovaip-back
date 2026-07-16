release: python manage.py migrate && python create_superuser.py
web: gunicorn config.wsgi:application

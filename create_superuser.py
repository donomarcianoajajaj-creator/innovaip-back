import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User

if not User.objects.filter(username='moderador').exists():
    User.objects.create_superuser('moderador', 'mod@innovaip.com', 'moderador123')
    print('Superuser creado: moderador / moderador123')
else:
    print('El usuario moderador ya existe')

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')


application = get_wsgi_application()

from whitenoise import WhiteNoise

application = WhiteNoise(application, root='/Users\yahdeen\Downloads\Focus\manucho\myapp')
"""
ASGI config for user_management project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from decouple import config
from django.core.asgi import get_asgi_application

if config('DJANGO_DEVELOPMENT') == 'dev':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_management.settings.dev')
elif config('DJANGO_DEVELOPMENT') == 'prod':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_management.settings.settings')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_management.settings.settings')

application = get_asgi_application()

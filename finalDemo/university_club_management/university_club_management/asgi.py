"""
ASGI config for university_club_management project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'university_club_management.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'university_club_management.settings.production')


application = get_asgi_application()
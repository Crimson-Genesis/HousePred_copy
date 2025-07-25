"""
wsgi config for housepred project.

it exposes the wsgi callable as a module-level variable named ``application``.

for more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HousePred.settings')

application = get_wsgi_application()

"""
WSGI config for main_p project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main_p.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=os.path.join(BASE_DIR, 'staticfiles'))

app = application
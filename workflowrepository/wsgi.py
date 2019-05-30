"""
WSGI config for workflowrepository project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

from django.contrib.sessions.backends.db import SessionStore

s = SessionStore()

if s.session_key is None:
    s.clear()
    s.create()
    s.cycle_key()
    s.set_expiry(10)
print " Fecha de expiracion:  "+ str(s.get_expiry_date()) + str(s.session_key)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "workflowrepository.settings")

application = Cling(get_wsgi_application())

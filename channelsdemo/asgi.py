"""
ASGI config for channelsdemo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from channelsdemo.ws_urlpatterns import ws_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channelsdemo.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(ws_urlpatterns)
})

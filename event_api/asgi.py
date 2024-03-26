import os

from django.core.asgi import get_asgi_application
from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

from chat.routing import websocket_urlpatterns


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_api.settings')

application = ProtocolTypeRouter(
        {
            'http': get_asgi_application(),
            'websocket': AllowedHostsOriginValidator(
                URLRouter(websocket_urlpatterns),
            )
        }
)

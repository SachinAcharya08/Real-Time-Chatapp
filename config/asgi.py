# """
# ASGI config for config project.

# It exposes the ASGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/6.1/howto/deployment/asgi/
# """

import os
from apps.chats import routing

from django.core.asgi import get_asgi_application
from channels.security.websocket import AllowedHostsOriginValidator
from apps.chats.channels_middleware import JWTWebSocketMiddleware
from channels.routing import ProtocolTypeRouter,URLRouter
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')



application = ProtocolTypeRouter(
    {
    "http":get_asgi_application(),
    "websocket":AllowedHostsOriginValidator(JWTWebSocketMiddleware(
                    URLRouter(routing.websocket_urlpatterns)
            )
)}
    )

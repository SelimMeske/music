import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from django.conf.urls import url

from .consumers import EchoCosnumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'music.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # Just HTTP for now. (We can add other protocols later.)
    "websocket": AuthMiddlewareStack(
        URLRouter([
            url(r"^notify", EchoCosnumer.as_asgi())
        ])
    ),
})
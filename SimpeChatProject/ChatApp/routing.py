from django.urls import path
from .consumers import ChatAppConsumer

websocket_urlpatterns = [
    path('',ChatAppConsumer.as_asgi()),
]
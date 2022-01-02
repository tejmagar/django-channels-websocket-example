from django.urls import path

from channelsdemo.consumers import NumberGenerator

ws_urlpatterns = [
    path('ws/', NumberGenerator.as_asgi(), name='number-generator')
]

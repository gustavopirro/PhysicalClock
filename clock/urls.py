from django.urls import path, include

from clock.views import *

urlpatterns = [
    path('', ClockAPI.as_view(), name='clock'),
]

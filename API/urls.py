#   Copyright (c) Code Written and Tested by Ahmed Emad in 28/02/2020, 16:53

from django.urls import path

from .views import Shorten

app_name = 'core'

urlpatterns = [
    path('api/shorten', Shorten, name='shorten'),
]
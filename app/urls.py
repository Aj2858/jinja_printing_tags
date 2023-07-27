from django.urls import path
from app.views import *

app_name = 'app'

urlpatterns = [
    path('data_render/', data_render, name = 'data_render')
]
from django.urls import path
from app3.views import *

app_name = 'app3'

urlpatterns = [
    path('ifcondtion/', ifcondtion, name = 'ifcondtion'),
    path('if_elif_condtion/', if_elif_condtion, name = 'if_elif_condtion'),
    path('nestedif/', nestedif, name = 'nestedif'),
    path('forloop/', forloop, name = 'forloop'),
]
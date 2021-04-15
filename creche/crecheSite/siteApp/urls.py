# from django.urls import include, path
# from rest_framework import routers
# from . import views

from django.urls import path
from .api import EmployeeCreateApi, EmployeeUpdateApi

urlpatterns = [
    path('api', EmployeeCreateApi.as_view()),
    path('api/<int:pk>',EmployeeUpdateApi.as_view()),
]

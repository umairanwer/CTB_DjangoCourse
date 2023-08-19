from django.urls import path
from .views import *

urlpatterns = [
    path("1", home1, name='home1'),
    path("2", home2, name='home2'),
    path("3", home3, name='home3'),
    path("4", home4, name='home4'),
    path("5", home5, name='home5')
]

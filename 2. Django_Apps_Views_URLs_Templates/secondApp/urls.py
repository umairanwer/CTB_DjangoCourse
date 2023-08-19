from django.urls import path
from .views import *

app_name = 'secondApp'

urlpatterns = [
    path("1", home1, name='home1'),
    path("2", home2, name='home2'),
    path("3", home3, name='home3'),

]

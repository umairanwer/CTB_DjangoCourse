from django.urls import path
from .views import *

app_name = 'myapp'

urlpatterns = [
    path('index/', index, name='index'),
    path('home/', home, name='home')
]


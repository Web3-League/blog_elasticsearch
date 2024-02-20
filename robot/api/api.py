# urls.py dans votre application robots

from django.urls import include, path
from . import views

app_name = 'api'

urlpatterns = [
    path('robot/', include('robot.robots.robots')),
]

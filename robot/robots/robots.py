from django.urls import path
from . import views

app_name = 'robot'

urlpatterns = [
    path('get_robots/', views.robot_list, name='robot_list'),
    path('get_robot/<str:name>/', views.robot_detail, name='robot_detail'),
    path('add_robot/', views.robot_add, name='robot_add'),
    path('update_robot/<str:name>/', views.robot_update, name='robot_update'),
    path('delete_robot/<str:name>/', views.robot_delete, name='robot_delete'),
    path('update_location/<str:name>/', views.robot_update_location, name='robot_update_location'),
]

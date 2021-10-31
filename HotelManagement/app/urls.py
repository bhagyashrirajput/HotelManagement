from django.urls import path

from . import views

urlpatterns = [
    path('api/users', views.userList, name='user-list'),
    path('', views.index, name='index'),
]

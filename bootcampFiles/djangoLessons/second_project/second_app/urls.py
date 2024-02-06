from django.urls import path
from second_app import views

urlpatterns = [
    path("help", views.help, name="help"),
    path("", views.users, name="users"),
]
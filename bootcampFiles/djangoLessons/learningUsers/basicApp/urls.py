from django.urls import path
from basicApp import views

# TEMPLATE TAGGING
app_name = 'basicApp'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('userlogin/', views.user_login, name='userlogin'),
]
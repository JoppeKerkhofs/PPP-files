from django.urls import path
from basicApp import views

# TEMPLATE TAGGING
app_name = 'basicApp'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
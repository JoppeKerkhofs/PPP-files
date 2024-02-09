from django.urls import path
from . import views

app_name = 'food'

urlpatterns = [
    path('', views.IndexClassView.as_view(), name='index'),
    path('item/<int:pk>/', views.FoodDetail.as_view(), name='item'),
]
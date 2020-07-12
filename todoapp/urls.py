from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('update_task/<int:pk>/', views.updateTask, name="update_task"),

    
]
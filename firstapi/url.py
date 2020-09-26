from django.urls import path
from firstapi import views

urlpatterns = [
    path('saludos/', views.Saludos.as_view())
]

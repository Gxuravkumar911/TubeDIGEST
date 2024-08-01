from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_summary, name='generate_summary'),
]


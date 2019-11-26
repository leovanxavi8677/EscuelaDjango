from django.urls import path
from ..materias import views

urlpatterns = [
    path('', views.index, name='index'),

]
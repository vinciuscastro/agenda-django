from django.contrib import admin
from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('', view=views.index, name='index'),
]
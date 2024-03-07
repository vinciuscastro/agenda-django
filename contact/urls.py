from django.contrib import admin
from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    path('search/', view=views.search, name='search'),
    path('', view=views.index, name='index'),   


    path('contact/<int:contact_id>/', view=views.contact, name='contact'),
    path('contact/<int:contact_id>/update/', view=views.update, name='update'),
    path('contact/<int:contact_id>/delete/', view=views.delete, name='delete'),
    path('contact/create/', view=views.create, name='create'),
]   
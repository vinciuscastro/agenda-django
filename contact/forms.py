from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ValidationError
from contact.models import Contact
from django import forms
from . import models

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ['first_name', 'last_name', 'phone', 'email', 'description', 'category']


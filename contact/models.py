from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
  class Meta:
    verbose_name_plural = 'Categories'
    verbose_name = 'Category'
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Contact(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50, blank=True)
  phone = models.CharField(max_length=50)
  email = models.EmailField(max_length=250, blank=True)
  created = models.DateTimeField(default=timezone.now)
  description = models.TextField(blank=True)
  show = models.BooleanField(default=True)
  picture = models.ImageField(upload_to='pictures/%Y/%m/', blank=True, null=True)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
  owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

  def __str__(self):
    return self.first_name + ' ' + self.last_name
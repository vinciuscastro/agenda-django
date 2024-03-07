from django.contrib import admin
from contact import models

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'first_name', 'last_name', 'phone', 'email', 'created', 'show')
  search_fields = ('id','first_name', 'last_name', 'phone', 'email', 'created')
  list_filter = ('created',)
  ordering = ('-created',)
  list_editable = ('show',)
  list_per_page = 25
  list_max_show_all = 100

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name',)
  ordering = ('-id',)
from django.contrib import admin
from contact import models

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
  list_display = ('first_name', 'last_name', 'phone', 'email', 'created')
  search_fields = ('first_name', 'last_name', 'phone', 'email', 'created')
  list_filter = ('created',)
  ordering = ('-created',)
  list_per_page = 25
  list_max_show_all = 100
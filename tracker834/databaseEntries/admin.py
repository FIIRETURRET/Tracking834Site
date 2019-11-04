from django.contrib import admin

from .models import Database

# Register your models here.
class DatabaseAdmin(admin.ModelAdmin):
    list_display = ('data', 'whereFound', 'description', 'goodLink', 'needed', 'notes')

admin.site.register(Database, DatabaseAdmin)
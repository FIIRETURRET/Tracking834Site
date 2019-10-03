from django.contrib import admin

from .models import Entry834

# Register your models here.
class Entry834Admin(admin.ModelAdmin):
    list_display = ('groupnum', 'name', 'assigned', 'renewal', 'fileType', 'testFileName', 'testDate', 'approvedWho', 'prodFileName', 'prodDate', 'analyticsVerified', 'approvedWhoTwo')

admin.site.register(Entry834, Entry834Admin)

from django.contrib import admin

from .models import Query

# Register your models here.
class QueryAdmin(admin.ModelAdmin):
    list_display = ('queryName', 'folderName', 'subfolder', 'queryUsedFor', 'files', 'convertYN', 'conversionStartDate', 'assignedTo', 'conversionCompletionDate', 'newNameInBI',)

admin.site.register(Query, QueryAdmin)

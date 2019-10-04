from django.db import models

from django.forms import ModelForm

# Create your models here.

class Query(models.Model):
    folderName                  = models.CharField(max_length=50, blank=True, null=True)
    subfolder                   = models.CharField(max_length=100, blank=True, null=True)
    queryUsedFor                = models.CharField(max_length=500, blank=True, null=True)
    queryName                   = models.CharField(max_length=50)
    files                       = models.CharField(max_length=100, blank=True, null=True)
    convertYN                   = models.BooleanField()
    conversionStartDate         = models.DateField('Conversion Start Date', blank=True, null=True)
    assignedTo                  = models.CharField(max_length=20, blank=True, null=True)
    conversionCompletionDate    = models.DateField('Conversion Completion Date', blank=True, null=True)
    newNameInBI                 = models.CharField(max_length=100, blank=True, null=True)
    
    def get_all_field_names(self):
        return Query._meta.fields()
    
    def formatNoneType(inString):
        if inString is None:
            return ''
        return str(inString)
    
    def __str__(self):
        return  Query.formatNoneType(self.queryName) + " | " + Query.formatNoneType(self.assignedTo) + " | " + Query.formatNoneType(self.convertYN) + " | " + Query.formatNoneType(self.queryUsedFor)
        
        

from django.db import models

# Create your models here.

class Entry834(models.Model):
    groupnum    = models.CharField(max_length=20)
    name        = models.CharField(max_length=50)
    assigned    = models.CharField(max_length=20)
    renewal     = models.CharField(max_length=20)
    fileType    = models.CharField(max_length=20)
    testFileName= models.CharField(max_length=100)
    testDate    = models.DateField('Test Date')
    approvedWho = models.CharField(max_length=20)
    prodFileName= models.CharField(max_length=100)
    prodDate    = models.DateField('Production Date')
    analyticsVerified   = models.CharField(max_length=20)
    approvedWhoTwo      = models.CharField(max_length=20)
    
    def __str__(self):
        return  self.groupnum + " | " + self.name + " | " + self.assigned + " | " + self.testFileName
        
        
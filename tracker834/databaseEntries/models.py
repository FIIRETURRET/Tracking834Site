from django.db import models

# Create your models here.

class Database(models.Model):
    data        = models.CharField(max_length=100)
    whereFound  = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    goodLink    = models.BooleanField(default=False)
    needed      = models.BooleanField(default=False)
    notes       = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return Database.formatNoneType(self.data) + " | " + Database.formatNoneType(self.whereFound) + " | " + Database.formatNoneType(self.goodLink)

    def formatNoneType(inString):
        if inString is None:
            return ''
        return str(inString)

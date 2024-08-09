from django.db import models

class Statement(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    amount = models.IntegerField(blank=True, null=True)
    date_added = models.CharField(max_length=10, blank=True, null=True)
    

    def __str__(self):
        return self.title

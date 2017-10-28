from django.db import models

class Contest(models.Model):
    title = models.CharField(max_length=511, null=True)
    description = models.CharField(max_length=511, null=True)
    date_start = models.DateTimeField('date_start', null=True)
    date_finish = models.DateTimeField('date_finish', null=True)
    site_link = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    category = models.IntegerField(null=True)
    coordinates = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title

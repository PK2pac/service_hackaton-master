from django.db import models

class Contest(models.Model):
    title = models.CharField(max_length=511)
    description = models.CharField(max_length=511)
    date_start = models.DateTimeField('date_start')
    date_finish = models.DateTimeField('date_finish')
    site_link = models.CharField(max_length=255)
    category = models.IntegerField()
    coordinates = models.CharField(max_length=255)

    def __str__(self):
        return self.title

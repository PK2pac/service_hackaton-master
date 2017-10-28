from django.db import models
#from geoposition.fields import GeopositionField

# Create your models here.
class Organisation(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    coordinates = models.CharField(max_length=255)
    site_link = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category_contest(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Contest(models.Model):
    title = models.CharField(max_length=511)
    description = models.CharField(max_length=511)
    date_start = models.DateTimeField('date_start')
    date_finish = models.DateTimeField('date_finish')
    site_link = models.CharField(max_length=255)
    category = models.ForeignKey(Category_contest, on_delete=models.CASCADE, default=None)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

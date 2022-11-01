from distutils.command.upload import upload
from unicodedata import category
from django.db import models

class shop(models.Model):
    shopName = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    landmark = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    shopCategory = models.CharField(max_length=20)
    shopImage = models.ImageField(upload_to="media")

    def __str__(self):
        return self.shopName

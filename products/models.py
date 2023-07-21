from django.db import models


class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    compound = models.TextField()

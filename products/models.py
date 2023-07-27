from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    compound = models.TextField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.title






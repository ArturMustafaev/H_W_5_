from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100)
    descriptions = models.TextField(null=True, blank=True)
    price = models.FloatField()
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 null=True,
                                 related_name='products')

    @property
    def rating(self):
        return 0
    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField(default=1)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='reviews')

    def __str__(self):
        return self.text
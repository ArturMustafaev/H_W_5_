from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
       return self.name

class Product(models.Model):
    title = models.CharField(max_length=100, unique=True)
    descriptions = models.TextField(null=True, blank=True)
    price = models.FloatField()
    tags = models.ManyToManyField(Tag, blank=True)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 null=True,
                                 related_name='products')

    @property
    def rating(self):
        total_amout = self.reviews.all().count()
        if total_amout == 0:
            return 0
        sum_ = 0
        for i in self.reviews.all():
            sum_ += i.stars
        return sum_ / total_amout

class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField(default=1)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='reviews')

    def __str__(self):
        return self.text
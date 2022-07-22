from django.db import models


# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.TextField()
    description = models.TextField(max_length=1000)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField(default=1)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    @property
    def rating(self):
        total_amout = self.reviews.all().count()
        if total_amout == 0:
            return 0
        sum_ = 0
        for i in self.reviews.all():
            sum_ += i.stars
        return sum_ / total_amout

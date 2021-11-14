from django.db import models

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    phone_number = models.IntegerField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.CharField(max_length=20)
    text = models.TextField()
    datetime = models.DateTimeField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} - {self.school}"

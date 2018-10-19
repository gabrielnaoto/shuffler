from django.db import models


# Create your models here.

class Student(models.Model):
    RANKS = (
        ('A', 'A'),
        ('B', 'B')
    )
    name = models.CharField(max_length=100)
    rank = models.CharField(max_length=1, choices=RANKS)

    def __str__(self):
        return self.name

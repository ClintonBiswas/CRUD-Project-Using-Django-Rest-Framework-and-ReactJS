from pyexpat import model
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
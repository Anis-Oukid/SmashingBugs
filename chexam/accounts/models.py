from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Classroom(models.Model):
    year = models.CharField(blank=False, max_length=3)
    number = models.IntegerField(blank=False)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.RESTRICT)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Classroom(models.Model):
    year = models.CharField(blank=False, max_length=3)
    number = models.IntegerField(blank=False)

    def __str__(self):
        return f'Year-{self.year} _ G-{self.number}'


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,db_constraint=False)
    classroom = models.ForeignKey(Classroom, on_delete=models.RESTRICT)

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,db_constraint=False)


class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,db_constraint=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_constraint=False)

    def __str__(self):
        return self.user.username


class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_constraint=False)

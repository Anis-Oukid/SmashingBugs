from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Classroom(models.Model):
    year = models.CharField(blank=False, max_length=3)
    number = models.IntegerField(blank=False)

    def __str__(self):
        return f'Year-{self.year} _ G-{self.number}'


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_constraint=False)
    classroom = models.ForeignKey(Classroom, on_delete=models.RESTRICT, null=True, blank=True)
    student_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def calc_average(self):
        results = self.result_set.all()
        if len(results):
            return sum(result.mark for result in results) / len(results)
        return 0


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,db_constraint=False)
    module_name = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.user.username

    def get_full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'


class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, db_constraint=False)
    module_name = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.user.username

    def get_full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

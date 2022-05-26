from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class classroom(models.Model):
    year=models.CharField(blank=False,max_length=3)
    number=models.IntegerField(blank=False)
    
class User(AbstractUser):
    TYPE_CHOICES = (
      ('student', 'student'),
      ('teacher', 'teacher'),
      ('administrator', 'administrator'),
    )
    user_type = models.CharField(choices=TYPE_CHOICES,max_length=14)
    def __str__(self):
        return self.User.user_type +'   '+self.User.username
class student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    classroom=models.ForeignKey(classroom,on_delete=models.RESTRICT)


class teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)  


class administrator(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)


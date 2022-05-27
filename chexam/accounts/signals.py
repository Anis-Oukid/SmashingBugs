from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student, Classroom


@receiver(post_save, sender=User)
def create_user_student(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance, classroom=Classroom.objects.get(id=1))


@receiver(post_save, sender=User)
def save_user_student(sender, instance, **kwargs):
    instance.student.save()

# Generated by Django 4.0.4 on 2022-05-28 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_student_student_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_id',
        ),
        migrations.AddField(
            model_name='student',
            name='matricule',
            field=models.CharField(default='    ', max_length=10),
        ),
    ]

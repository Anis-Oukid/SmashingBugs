# Generated by Django 4.0.4 on 2022-05-28 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_remove_student_student_id_student_matricule'),
        ('exams', '0009_alter_exam_solution_alter_result_scan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.student'),
        ),
    ]

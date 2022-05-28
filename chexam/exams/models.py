from django.db import models
from django.db.models import Model
from django.apps import apps
from accounts.models import Teacher, Student


class Exam(Model):
    module_name = models.CharField(max_length=500)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    date_passed = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    solution = models.FileField(upload_to='Solutions', default=None,blank=True)

    def __str__(self):
        return f'{self.module_name}'


def folder_name(result, filename):
    return u'%s/%s/PDFs/_%s' % (str(result.exam.id), str(result.student),
                                filename)


class Result(Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    mark = models.FloatField()
    scan = models.FileField(upload_to=folder_name, default=None,blank=True)
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student} _ {self.exam}'


class Reclamation(Model):
    result = models.OneToOneField(Result, on_delete=models.CASCADE)
    treated = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.result}'


# problem types
counting = 'counting'
miss_judging = 'miss_judging'
forgetting = 'forgetting'

PROBLEM_TYPE_CHOICES = [
    (counting, 'Counting'),
    (miss_judging, 'Miss Judging'),
    (forgetting, 'Forgetting'),
]


def folder_name2(Problem, filename):
    return u'%s/%s/Problems/_%s' % (str(Problem.reclamation.result.exam.id), str(Problem.reclamation.result.student),
                                    filename)


class Problem(Model):
    reclamation = models.ForeignKey(Reclamation, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1500)
    approved = models.BooleanField(default=False)
    problem_type = models.CharField(
        max_length=30,
        choices=PROBLEM_TYPE_CHOICES,
        default=counting,
    )
    scan = models.FileField(upload_to=folder_name2, default=None, null=True, blank=True)

    def __str__(self):
        return f'{self.reclamation} - {self.comment[:10]}'

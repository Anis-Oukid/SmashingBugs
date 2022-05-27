from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Result, Reclamation
from accounts.models import Teacher, Student


def is_teacher(user):
    return Teacher.objects.filter(user=user).exists()


@login_required
def results_page(request):
    if is_teacher(request.user):
        return redirect("reclamations_page")

    student = request.user.student
    results = student.result_set.all()

    context = {
        'results': results
    }
    return render(request, "exams/results_page/index.html", context=context)


@login_required
def reclamations_page(request):
    teacher = request.user.teacher
    # results = student.result_set.all()
    reclamations = Reclamation.objects.filter(result__exam__teacher=teacher)

    context = {
        'reclamations': reclamations
    }
    return render(request, "exams/reclamations_page/index.html", context=context)

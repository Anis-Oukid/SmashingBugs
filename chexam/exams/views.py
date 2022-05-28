import json
# import glob, sys, fitz
import os
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.http import require_POST

from .models import Result
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Result, Reclamation, Problem
from accounts.models import Teacher, Student
from pdf2image import convert_from_path


def is_teacher(user):
    return Teacher.objects.filter(user=user).exists()


def is_student(user):
    return Student.objects.filter(user=user).exists()


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


from django.http import FileResponse


@login_required
def result_details(request, pk):
    result = Result.objects.get(id=pk)
    if is_student(request.user) and result.student == request.user.student \
            or (is_teacher(request.user) and result.exam.teacher == request.user.teacher):
        problems = Problem.objects.filter(reclamation__result=result)
        context = {
            'is_teacher': is_teacher(request.user),
            'problems': problems,
            'result': result,
        }
        return render(request, "exams/result_details/result_details.html", context=context)

    raise Http404


@login_required
def reclamations_page(request):
    teacher = request.user.teacher
    reclamations = Reclamation.objects.filter(result__exam__teacher=teacher)

    context = {
        'reclamations': reclamations
    }
    return render(request, "exams/reclamations_page/index.html", context=context)


@login_required
def verify_result(request, pk):
    try:
        result = Result.objects.get(id=pk)
        pdf_link = result.scan.url
        images = f"./{result.scan.url}"
        images_link = f"{images}/Photos"

        if is_student(request.user) and result.student == request.user.student:
            if request.method == "POST":
                result.verified = True
                result.save()
        return redirect("result_details", pk=result.reclamation.result.id)
    except:
        pass
    return redirect("results_page")


@login_required
def refuse_problem(request, pk):
    try:
        problem = Problem.objects.get(id=pk)

        if is_teacher(request.user) and problem.reclamation.result.exam.teacher == request.user.teacher:
            if request.method == "POST":
                problem.approved = False
                problem.save()
        return redirect("result_details", pk=problem.reclamation.result.id)
    except:
        pass
    return redirect("results_page")


@login_required
def validate_problem(request, pk):
    try:
        problem = Problem.objects.get(id=pk)
        print(is_teacher(request.user) and problem.reclamation.result.exam.teacher == request.user.teacher)
        if is_teacher(request.user) and problem.reclamation.result.exam.teacher == request.user.teacher:
            if request.method == "POST":
                problem.approved = True
                problem.save()
                return redirect("result_details", pk=problem.reclamation.result.id)
        pass
    except:
        pass
    return redirect("results_page")


@login_required
@require_POST
def add_problem(request, pk):
    user = request.user
    message = {}

    try:
        reclamation = Reclamation.objects.get(id=pk)

        if request.method == 'POST':
            comment = request.POST.get('comment')
            problem_type = request.POST.get('problem_type')
            problem_photo = request.POST.get('croped')
            problem_types = ('counting', 'miss_judging', 'forgetting')

            if problem_type in problem_types:
                problem = Problem(
                    reclamation=reclamation,
                    comment=comment,
                    problem_type=problem_type,
                    scan=problem_photo,
                )
                problem.save()
                message = 'Problem added'
            else:
                message = 'Invalid problem type'
    except:
        message = 'Invalid reclamation'
    return HttpResponse(json.dumps(message), content_type='application/json')

from email.errors import MultipartInvariantViolationDefect
import json
import glob, sys
from exams.forms import addPdf
import os
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST

from .models import Result
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Result, Reclamation, Problem, Exam
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
    result = get_object_or_404(Result, id=pk)
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


def convertPDFToImg(pdfLoc):
    images = convert_from_path(pdfLoc, 500, poppler_path=r'C:\Program Files\poppler-0.67.0\bin')
    for i in range(len(images)):
        images[i].save('page' + str(i) + '.jpg', 'JPEG')


@login_required
def reclamations_page(request):
    teacher = request.user.teacher
    reclamations = Reclamation.objects.filter(result__exam__teacher=teacher, treated=False)
    form = addPdf(request.POST, request.FILES)
    if is_teacher(request.user):
        exam = get_object_or_404(Exam, teacher=teacher)
        student = get_object_or_404(Student, matricule='111')
        if request.method == "POST" and 'scansub' in request.POST:
            form = addPdf(request.POST, request.FILES,
                          initial={'exam': exam, 'student': student})  # Do not forget to add: request.FILES
            result = Result(exam=exam, student=student, mark=0.33)
            result.save()
            if form.is_valid():
                # Do something with our files or simply save them
                # if saved, our files would be located in media/ folder under the project's base folder

                form.student = student
                form.save()
    context = {
        'reclamations': reclamations,
        'form': form
    }
    return render(request, "exams/reclamations_page/index.html", context=context)


@login_required
def verify_result(request, pk):
    try:
        result = get_object_or_404(Result, id=pk)
        pdf_link = result.scan.url
        images = f"./{result.scan.url}"
        images_link = f"{images}/Photos"

        if is_student(request.user) and result.student == request.user.student \
                or is_teacher(request.user) and result.exam.teacher == request.user.teacher:
            if request.method == "POST":
                result.verified = True
                result.reclamation.treated = True
                result.reclamation.save()
                result.save()
        return redirect("result_details", pk=result.reclamation.result.id)
    except:
        pass
    return redirect("results_page")


@login_required
def refuse_problem(request, pk):
    try:
        problem = get_object_or_404(Problem, id=pk)

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
        problem = get_object_or_404(Problem, id=pk)
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
        reclamation = get_object_or_404(Reclamation, id=pk)

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

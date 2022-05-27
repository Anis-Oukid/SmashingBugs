from django.shortcuts import render
from .models import Result
from django.http import HttpResponse
from pdf2image import convert_from_path
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

from django.http import FileResponse
def result_details(request,id):
    result = Result.objects.get(id=id)
    a= f'.{result.exam.solution.url}'
    sol = open(a, "rb").read()

 
   
    
    
    context={
        'a':a,
        'sol':sol,
        'result':result,
    }
    return render(request,"exams/result_details/result_details.html",context=context)


@login_required
def reclamations_page(request):
    teacher = request.user.teacher
    # results = student.result_set.all()
    reclamations = Reclamation.objects.filter(result__exam__teacher=teacher)

    context = {
        'reclamations': reclamations
    }
    return render(request, "exams/reclamations_page/index.html", context=context)

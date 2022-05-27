from django.shortcuts import render
from .models import Result
from django.http import HttpResponse
from pdf2image import convert_from_path

def results_page(request):
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


from django.urls import path
from . import views

urlpatterns = [
    path('', views.results_page, name='results_page'),
    path('result/<int:pk>', views.result_details, name='result_details'),
    path('result/<int:pk>/verify/', views.verify_result, name='verify_result'),
    path('reclamations/', views.reclamations_page, name='reclamations_page'),
    path('problem/<int:pk>/validate/', views.validate_problem, name='validate_problem'),
    path('problem/<int:pk>/refuse/', views.refuse_problem, name='refuse_problem'),
    path('reclamation/<int:pk>/add_problem/', views.add_problem, name='add_problem'),
    path('add_solution/', views.add_scans, name='add_solution'),
    path('add_exam/', views.add_exam, name='add_exam'),
    path('list/', views.exams_list, name='exams_list'),
]

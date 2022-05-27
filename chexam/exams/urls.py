from django.urls import path
from . import views

urlpatterns = [
    path('', views.results_page, name='results_page'),
    path('result/<int:id>', views.result_details, name='result_details'),
    path('reclamations/', views.reclamations_page, name='reclamations_page'),
]

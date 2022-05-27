from django.urls import path
from . import views

urlpatterns = [
    path('', views.results_page, name='results_page'),
    path('reclamations/', views.reclamations_page, name='reclamations_page'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.results_page, name='results_page'),
]

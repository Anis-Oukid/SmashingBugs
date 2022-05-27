from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name='home'),
    path('settings/', views.settings, name='settings'),
    path('edit_password', views.edit_password, name='edit_password'),
    path('change_password/', views.change_password, name='change_password'),
    path('logout', views.logout_request, name='logout')
]

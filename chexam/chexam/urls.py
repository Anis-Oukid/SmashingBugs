from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exams/', include('exams.urls')),
    path('account/', include('accounts.urls')),
    path('auth/', include('allauth.urls')),
]

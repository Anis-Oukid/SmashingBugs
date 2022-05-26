from django.contrib import admin
from .models import student,teacher,administrator,classroom
# Register your models here.
admin.site.register(student)
admin.site.register(teacher)
admin.site.register(administrator)
admin.site.register(classroom)
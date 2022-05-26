from django.contrib import admin
from .models import Exam, Result, Reclamation, Problem


class ExamAdmin(admin.ModelAdmin):
    list_display = ('module_name', 'teacher')


class ResultAdmin(admin.ModelAdmin):
    list_display = ('exam', 'student', 'mark')


class ReclamationAdmin(admin.ModelAdmin):
    list_display = ('result', 'approved', 'treated')


admin.site.register(Exam, ExamAdmin)
admin.site.register(Result, ResultAdmin)
admin.site.register(Reclamation, ReclamationAdmin)
admin.site.register(Problem)

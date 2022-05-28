from django.forms.widgets import Select, Widget
from django import forms
from exams.models import Result,Exam
class addPdf(forms.ModelForm):
    scan=forms.FileField()
    class Meta:
        model = Result
        fields=['scan']
        widgets = {

           }
class addSolutionForm(forms.ModelForm):
    solution=forms.FileField()
    class Meta:
        model = Exam
        fields=['solution']
        
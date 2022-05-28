from django.forms.widgets import Select, Widget
from django import forms
from exams.models import Result
class addPdf(forms.ModelForm):
    CHOICES = (('sfsd', 'sfsd'),('sfsd1', 'sfsd1'),)
    scan=forms.FileField()
    class Meta:
        model = Result
        fields=['scan','exam','student','mark']
        widgets = {

            'exam': forms.TextInput(attrs={
               'id':"input1" ,
               'type':"text" ,
               'class':"form-control",
               'placeholder':"Nom" ,
               'value':"{{user.teacher}}",
                  
               
            }),}
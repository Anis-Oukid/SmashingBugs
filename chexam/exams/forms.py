from django.forms.widgets import Select, Widget
from django import forms
from exams.models import Result, Exam, Problem


class addPdf(forms.ModelForm):
    scan = forms.FileField()

    def __init__(self, *args, **kwargs):
        super(addPdf, self).__init__(*args, **kwargs)
        self.fields['scan'].widget.attrs.update({
            'type': "file",
            'id': "students_files",
            'class': "hidden",
            'name': "students_files",
            # 'onchange':"form.submit()",
        })

    class Meta:
        model = Result
        fields = ['scan']
        widgets = {

        }


class addSolutionForm(forms.ModelForm):
    solution = forms.FileField(widget=forms.FileInput(attrs={
        'type': "file",
        'id': "correction",
        'class': "hidden",
        'name': "correction",
        # 'onchange':"form.submit()",
        'multiple': "true",

    }))

    class Meta:
        model = Exam
        fields = ['solution']


class imgForm(forms.ModelForm):
    solution = forms.FileField(widget=forms.FileInput(attrs={
        'type': "file",
        'id': "screenshot",
        'class': "",
        'name': "screenshot",
        # 'onchange':"form.submit()",
        'multiple': "false",

    }))

    class Meta:
        model = Problem
        fields = ['scan']

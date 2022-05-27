from allauth.utils import set_form_field_order
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm


class UpdateProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(UpdateProfileForm, self).__init__(*args, **kwargs)

    input_classes = 'focus:outline-blue-500 block m-auto p-5 w-full rounded-full custom-shadow'
    # username = forms.CharField(
    #     label='Username',
    #     min_length=2,
    #     max_length=150,
    #     widget=forms.TextInput(attrs={
    #         'class': input_classes,
    #         'placeholder': 'Username',
    #     }),
    # )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': input_classes,
            'placeholder': 'Email'
        }),
    )

    class Meta:
        model = User
        fields = ('email',)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.exclude(pk=self.user.pk).filter(email=email).exists():
            raise forms.ValidationError("Email is already exists")
        return email


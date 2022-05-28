from allauth.utils import set_form_field_order
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from allauth.account.forms import LoginForm


class CustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        input_classes = 'block h-12 w-2/3 rounded py-1'
        login_field = forms.EmailField(
            label='E-mail',
            widget=forms.EmailInput(attrs={
                'class': input_classes,
                'placeholder': 'Email address',
                'autofocus': '',
                'style': 'all:unset'
            }),
        )
        password_field = forms.CharField(
            label='Password',
            widget=forms.PasswordInput(attrs={
                'class': input_classes,
                'placeholder': 'Password',
                'style': 'all:unset'
            }),
        )
        remember_field = forms.BooleanField(
            label="Remember Me",
            widget=forms.CheckboxInput(attrs={
                'class': '',
                'checked': 'checked'
            })
        )
        self.request = kwargs.pop("request", None)
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields["login"] = login_field
        self.fields["password"] = password_field
        self.fields["remember"] = remember_field
        set_form_field_order(self, ["login", "password", "remember"])


class UpdateProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(UpdateProfileForm, self).__init__(*args, **kwargs)

    input_classes = 'block h-12 w-2/3 rounded'

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': input_classes,
            'placeholder': 'Email',
            'style': 'all:unset'
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

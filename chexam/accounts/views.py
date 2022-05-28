import json

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UpdateProfileForm
from django.contrib.auth import logout
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from .models import Teacher, Student
from django.shortcuts import get_object_or_404


def is_teacher(user):
    return Teacher.objects.filter(user=user).exists()


def is_student(user):
    return Student.objects.filter(user=user).exists()


@login_required
def settings(request):
    user = request.user

    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=user, user=user)
        if form.is_valid():
            email = form.cleaned_data['email']

            user.email = email
            user.save()
    else:
        form = UpdateProfileForm(instance=request.user, user=user)

    context = {
        'form': form,
        'role': 'Student' if is_student(user) else ('Teacher' if is_teacher(user) else 'Admin'),
        'header_title': 'Settings'
    }

    return render(request, "accounts/settings/index.html", context=context)


def change_password(request):
    user = request.user
    message = {}

    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        retype_new_password = request.POST.get('re_new_password')

        if user.check_password(old_password):
            if new_password == retype_new_password and new_password != '':
                user.set_password(new_password)
                user.save()
                message = 'Password was successfully changed'
                update_session_auth_hash(request, request.user)  # This code will keep session when user change password
            else:
                message = 'Invalid Passwords !'
        else:
            message = 'Your old password is wrong !'

    return HttpResponse(json.dumps(message), content_type='application/json')


@login_required
def edit_password(request):
    return render(request, "accounts/edit_password/index.html", context={'header_title': 'Change Password'})


def logout_request(request):
    logout(request)
    return redirect("home")


def homepage(request):
    return redirect("account_login")


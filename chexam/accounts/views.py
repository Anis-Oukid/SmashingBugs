import json

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UpdateProfileForm


@login_required
def settings(request):
    user = request.user

    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=user, user=user)
        if form.is_valid():
            # username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            # user.username = username
            user.email = email
            user.save()
    else:
        form = UpdateProfileForm(instance=request.user, user=user)

    context = {'form': form}

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

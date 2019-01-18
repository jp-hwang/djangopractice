from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings


def singup(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup_form.html',{
        'form':form,
    })



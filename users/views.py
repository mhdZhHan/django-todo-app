from django.shortcuts import render
from django.http import HttpResponse
# from django.shortcuts import redirect
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from users.forms import StudentLoginForm, StudentRegistrForm
from users.models import StudentUser
from main.functions import genarate_form_errors


def login(request):
    if request.method == "POST":
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(request, username=cleaned_data['username'], \
                                 password=cleaned_data['password'])
            
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect('/')
            else: 
                context = {
                    "title": "Django ToDo | Login",
                    "error": True,
                    "message": "Invalid username or password",
                    "form": form,
                }
        else:
            context = {
                 "title": "Django ToDo | Login",
                 "error": True,
                 "message": "Enter username and password",
                 "form": form,
            }
    else:
        form = StudentLoginForm()
        context = {
            "title": "Django ToDo | Login",
            "form": form,
        }

    return render(request, 'users/login.html', context)


def logout(request):
    auth_logout(request)
    # return redirect('/users/login')
    return HttpResponseRedirect('/users/login') 


def register(request):
    if request.method == 'POST':
        form = StudentRegistrForm(request.POST)
        if form.is_valid():

            instance = form.save(commit=False)
            instance.set_password(form.cleaned_data['password'])
            instance.save()

            user_ = authenticate(
                request, 
                username=instance.username, 
                password=form.cleaned_data['password']
            )

            auth_login(request, user_)

            return HttpResponseRedirect('/')
        else:
            error_message = genarate_form_errors(form)
            form = StudentRegistrForm()
            context = {
                "title": "Django ToDo | Signup",
                "error": True,
                "message": error_message,
                "form": form,
            }
    else:
        form = StudentRegistrForm()
        context = {
            "title": "Django ToDo | Signup",
            "form": form,
        }
        
    return render(request, 'users/register.html', context)

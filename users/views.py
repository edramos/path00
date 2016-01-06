from django.shortcuts import render

def toSignup(request):
    return render(request, 'users/signup.html')

def toLogin(request):
    return render(request, 'users/login.html')
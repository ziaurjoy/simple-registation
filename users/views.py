from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic

from users.forms import CreateEmployeeForm, CreateUserForm, LoginForm
from users.models import CreateEmployee


def home(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            user = authenticate(
                username = forms.cleaned_data['username'],
                password = forms.cleaned_data['password']
            )
            if user:
                login(request,user)
                return redirect('create-user')
    context = {'forms': forms}
    return render(request,'pages/home.html',context)


def create_user(request):
    forms = CreateUserForm()
    if request.method == 'POST':
        forms = CreateUserForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            re_password = forms.cleaned_data['re_password']
            if password == re_password:
                user_obj = User.objects.create(username=username, password=password)
                new_user = forms.save(commit=False)
                new_user.user = user_obj
                new_user.save()
                return redirect('create-employee')
    context = {"forms":forms}
    return render(request,'pages/createuser.html',context)



def crete_employee(request):
    forms = CreateEmployeeForm()
    if request.method == 'POST':
        forms = CreateEmployeeForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('create-complite')
    context = {'forms': forms}
    return render(request,'pages/create_employee.html',context)

def complite(request):
    return render(request,'pages/complite.html')
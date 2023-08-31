from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ToDoForm
from .models import ToDo
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# for login:


def Login(request):
    if request.method == 'GET':
        forms = AuthenticationForm()
        context = {
            "form": forms
        }
        return render(request, 'tasks/login.html', context=context)
    else:
        forms = AuthenticationForm(data=request.POST)
        print(forms.is_valid())
        if forms.is_valid():
            username = forms.cleaned_data.get('username')
            password = forms.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                context = {
                    'form': forms
                }
                return render(request, 'tasks/login.html', context=context)
    return render(request, 'tasks/login.html', context={'form':forms})


# For SignUp
def Signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            "form": form
        }
        return render(request, 'tasks/signup.html', context=context)
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)
        context = {
            "form": form
        }
        if form.is_valid():
            user = form.save()
            print(user)
            if user is not None:
                return redirect('login')
        else:
            return render(request, 'tasks/signup.html', context=context)


def Logout(request):
    logout(request)
    return redirect('login')



@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = ToDoForm()
        todo = ToDo.objects.filter(user=user).order_by('priority')
        return render(request, 'tasks/index.html', context={'form': form, 'todos': todo})

# To add
@login_required(login_url='login')
def add_todo(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = ToDoForm(request.POST)
        if form.is_valid():
            print("RIGHT CODE")
            print(form.cleaned_data)
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            print(todo)
            return redirect("home")
        else:
            print('Not Right Code')
            return render(request, 'tasks/index.html', context={'form': form})


# To delete tode:
@login_required(login_url='login')
def delete_todo(request, id):
    print(id)
    ToDo.objects.get(pk=id).delete()
    return redirect('home')

# Change todo:


@login_required(login_url='login')
def change_todo(request, id, status):
    todo = ToDo.objects.get(pk=id)
    todo.status = status
    todo.save()
    return redirect('home')

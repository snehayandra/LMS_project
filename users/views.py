from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from DBApp.models import Student

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        password = request.POST.get('password')

        try:
            student = Student.objects.get(full_name=full_name, password=password)
            return redirect('std_dashurl')  # Replace 'teacher_dashboard' with your desired redirect URL name
        except Student.DoesNotExist:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')

def dashboard(request):
    return render(request,'student_dashboard.html')


def register_view(request):
    if request.method == 'POST':
        fo = UserCreationForm(request.POST)
        print(fo)
        if fo.is_valid():
            fo.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('loginurl')  
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        fo = UserCreationForm()

    return render(request, 'register.html', {'form': fo})


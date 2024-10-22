from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from DBApp.models import Teacher
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        password = request.POST.get('password')

        try:
            teacher = Teacher.objects.get(full_name=full_name, password=password)
            return redirect('dashurl')  # Replace 'teacher_dashboard' with your desired redirect URL name
        except Teacher.DoesNotExist:
            messages.error(request, 'Invalid username or password')

    return render(request, 'teacher_login.html')

def dashboard(request):
    return render(request,'teacher_dashboard.html')


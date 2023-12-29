from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import FinanceResource


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Invalid login
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@login_required
def home_view(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def income_revenue_view(request):
    return render(request, 'income_revenue.html')

def expenses_view(request):
    return render(request, 'expenses.html')

def analysis_view(request):
    return render(request, 'analysis.html')

def education_library_view(request):
    return render(request, 'education_library.html')

def registration_view(request):
    return render(request, 'registration.html')

def finance_resources_view(request):
    resources = FinanceResource.objects.all()
    return render(request, 'finance_resource.html', {'resources': resources})


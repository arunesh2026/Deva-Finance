from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from loan.models import LoanApplication
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

from dashboard.forms import SignUpForm, LoginForm


def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    
    form = SignUpForm()
        
    if request.method == "POST":
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect("login")
            
    
    context = {
        "form": form
    }
    
    return render(request=request, template_name="dashboard/register.html", context=context)



def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    
    form = LoginForm()
        
    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)
        
        if form.is_valid():
            
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            
            user = authenticate(username=username, password=password)
            
            login(request=request, user=user)
            
            return redirect("dashboard")
            
    
    context = {
        "form": form
    }
    
    return render(request=request, template_name="dashboard/login.html", context=context)



def logout_view(request):
    logout(request=request)
    return redirect("login")




def dashboard(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    context = {
        "user": request.user,
    }
        
    return render(request=request, template_name="dashboard/dashboard.html", context=context)


def applied_loan(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    try:
        loan_list = LoanApplication.objects.filter(email=request.user.email).order_by("-created_date")[0]
    except IndexError:
        loan_list = None
    
    
    context = {
        "user": request.user,
        "loan_list": loan_list
    }
        
    return render(request=request, template_name="dashboard/applied-loan.html", context=context)

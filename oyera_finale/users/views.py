from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import RegistrationForm, UserLoginForm
from django.contrib.auth import authenticate

# Create your views here.
def registerPage(request):
    if request.method == "POST":
        data = request.POST
        form = RegistrationForm(data)
        if form.is_valid():
            form.save()
            return redirect("logIn")

    else:
        form = RegistrationForm()
    context ={
            "form": form
    }
    return render(request, "finals/registration_form.html", context)


def loginPage(request):
    if request.method =="POST":
        data = request.POST
        form = UserLoginForm(request, data)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect("customer_dashboard")
    else:
        form = UserLoginForm()
    return render (request, "finals/login.html")


def sensitive_view(request): 
    if request.method == 'POST':
         # Verify the current user's password again 
        password =request.POST.get('password')
        user = authenticate(username=request.user.username, password=password)
        if user is not None: request.session['reauthenticated'] = True
        return redirect('sensitive_data') 
    return render(request, 'verify_password.html')
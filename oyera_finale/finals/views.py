from django.shortcuts import render
from .forms import SignInForm

# Create your views here.
def homePage(request):
    return render(request, 'finals/index.html')

def signIn(request):
    if request.method == 'POST':
        payload = request.POST
        
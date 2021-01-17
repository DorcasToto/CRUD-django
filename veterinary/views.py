from django.shortcuts import render
from . forms import RegistrationForm
from django.contrib import messages
from .models import *
from django.shortcuts import redirect

# Create your views here.
def index(request):
    all_veterinarians = Veterinary.objects.all()
    return render(request,'index.html',{'vets':all_veterinarians})

def register(request):

    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')

    else:
        registration_form= RegistrationForm()

    return render(request, 'register.html', {'registration_form': registration_form})
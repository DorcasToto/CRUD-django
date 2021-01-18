from django.shortcuts import render
from . forms import *
from django.contrib import messages
from .models import *
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

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

def register_vet(request):
    current_user = request.user
    if request.method == 'POST':
        form = RegisitervetForm(request.POST)
        if form.is_valid():
            formVet = form.save(commit=False)
            formVet.user = current_user
            formVet.save()
            return redirect('home')

    else:
        form = RegisitervetForm()

    return render(request,"register_vet.html",{"formVet":form})

def delete_vet(request,id):
    vet = Veterinary.objects.get(id = id)
    vet.delete()
    messages.error(request, 'The record has been deleted successfully')
    # message = "The record has been deleted successfully"
    return redirect('home')

def update_vet(request,id):
    if request.POST:
        vet_form = RegisitervetForm(request.POST)

        if vet_form.is_valid():
            vet = Veterinary.objects.get(id=id)
            vett_form = RegisitervetForm(request.POST, instance = vet)
            vett_form.save() 
            return redirect('home')
    else:
        vet = Veterinary.objects.get(id = id)       
        vett_form = RegisitervetForm(instance=vet)
        params = {
            'form':vett_form,
            'vet':vet,
        }

    return render(request,'edit_vet.html',params)  

    
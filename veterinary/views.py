from django.shortcuts import render
from . forms import *
from django.contrib import messages
from .models import *
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView,DeleteView
from django.urls import reverse_lazy

#Api
from .serializer import *
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@login_required
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

    return render(request, 'accounts/register.html', {'registration_form': registration_form})

@login_required
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

class delete_vet(DeleteView): 
    model = Veterinary
    success_url ="/"
    
class update_vet(UpdateView):
    model= Veterinary
    template_name='edit_vet.html'
    fields = ['name','email','county','id_no','phone_number']
    success_url = reverse_lazy('home')






#create api endpoints
class UserViewSet(APIView):
  #create a new admin endpoint
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VetList(APIView):
    """
    List all vets, or create a new vet.
    """

    permission_classes = [IsAuthenticated]
    #display vets
    def get(self, request, format=None):
        vets = Veterinary.objects.all()
        serializer = VetSerializer(vets, many=True)
        return Response(serializer.data)

    #onboard vet
    def post(self, request, format=None):
        serializer = VetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VetDetailList(APIView):
    """
    Retrieve, update or delete a vet instance.
    """
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Veterinary.objects.get(pk=pk)
        except Veterinary.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        vet = self.get_object(pk)
        serializer = VetSerializer(vet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        vet = self.get_object(pk)
        serializer = VetSerializer(vet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        vet = self.get_object(pk)
        vet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
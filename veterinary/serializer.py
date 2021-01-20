from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    @staticmethod
    def validate_password(password: str) -> str:
        return make_password(password)
    class Meta:
        model = User
        fields = ['id', 'username', 'email','password']

class VetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Veterinary
        # fields = '__all__'
        fields = ['id','user','name','email','county','id_no','phone_number']
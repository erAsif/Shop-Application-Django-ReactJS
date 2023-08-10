from rest_framework import serializers
from .models import RegistrationModel

from django.contrib.auth.hashers import make_password


class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegistrationModel
        fields = ('user_name','email','password','created_at','updated_at','uid') # required fields
        extra_kwargs = {
            'password':{'write_only': True},
        }
        
    def create(self, validated_data):
        user = RegistrationModel.objects.create(
            email=validated_data['email'],
            user_name=validated_data['user_name'],
            password = make_password(validated_data['password'])
             ) 
        return user  

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50)
    class Meta:
        model = RegistrationModel
        fields = ['email' , 'password']

    def create(self, validated_data):
        user = RegistrationModel.objects.create(
            email=validated_data['email'],
            password = make_password(validated_data['password'])
             ) 
        return user    
    
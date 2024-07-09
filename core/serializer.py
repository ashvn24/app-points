from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'is_active', 'is_staff', 'is_superuser')
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data.pop('password', None))
        user.save()
            
        return user

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    access_token = serializers.CharField(max_length=255, read_only=True)
    refresh_token = serializers.CharField(max_length=255, read_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'access_token', 'refresh_token']
        
    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        request = self.context.get('request')
        user = authenticate(request, email=email, password=password)
        print(user,email,'------')
        if not user:
            raise serializers.ValidationError({'error': 'Invalid email or password.'})
            
        user_token = user.tokens()
        print(user_token,'------')
        return {
            'email': user.email,
            'access_token': str(user_token.get('access')),
            'refresh_token':str(user_token.get('refresh'))
            }
            
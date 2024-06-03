from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CustomUser


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email

        return token
    

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True,
    )
    password2 = serializers.CharField(write_only=True, required=True)
    email = serializers.EmailField(
        required=True,

    )

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password', 'password2']

    def validate(self, attrs):
        print(f"Password 1: {attrs['password']}")
        print(f"Password 2: {attrs['password2']}")
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match"}
            )
        
        return attrs
    
    def validate_email(self, attrs):
        print(f"EMAILLLLL: {attrs}")
        if CustomUser.objects.filter(email=attrs).first():
            raise serializers.ValidationError(
                {"email": "This email already exists"}
            )
    
    def create(self, validated_data):
        user = CustomUser.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

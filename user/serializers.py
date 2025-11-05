from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from user.exceptions import UserAlreadyExistsByEmailException
from user.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise UserAlreadyExistsByEmailException()
        return email

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

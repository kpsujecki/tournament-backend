from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

from users.models import NewUser

User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    user_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)
    birthday = serializers.DateField()


    class Meta:
        model = NewUser
        fields = ('id','email', 'user_name', 'password', 'birthday')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class showProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'user_name',
            'email',
            'birthday'
        ]


from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        # exclude = ['patronymic', 'avatar', 'birth_date', 'created_at']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class LoginSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ["number", "password"]


class DoctorRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        # exclude = ['is_verified']
        fields = "__all__"

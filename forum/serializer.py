from rest_framework import serializers
from .models import *


class DiseasePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseasePost
        fields = "__all__"


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

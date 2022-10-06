from rest_framework import serializers
from .models import *


class QuizesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quizes
        fields = '__all__'

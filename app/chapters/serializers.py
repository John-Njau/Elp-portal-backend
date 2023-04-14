from rest_framework import serializers
from .models import Chapter, ChapterRegister

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = '__all__'


class ChapterRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChapterRegister
        fields = ['chapter', 'user']
        
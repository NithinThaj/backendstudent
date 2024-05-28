from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    subjects = serializers.JSONField(required=True)
    class Meta:
        model = Student
        fields = "__all__"
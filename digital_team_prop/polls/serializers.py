from rest_framework import serializers
from django.utils import timezone
from .models import *

class ParentSerializer(serializers.ModelSerializer):
    # parent_name = serializers.CharField(max_length = 100)
    # parent_mail = serializers.CharField(max_length = 100)
    # parent_phone = serializers.CharField(max_length = 30)
    # registration_date = serializers.DateTimeField(
    #     required=False, 
    #     default=timezone.now()
    # )
    
    class Meta:
        model = Parent
        fields = [
            'id',
            'parent_name',
            'parent_mail',
            'parent_phone',
            'registration_date',
        ]
        # fields = ('__all__')

class ChildSerializer(serializers.ModelSerializer):
    parent = serializers.RelatedField(source="parent", read_only=True)
    child_name = serializers.CharField(max_length = 200)
    child_birth_date = serializers.DateTimeField(
        "birth date", 
        default=timezone.now()
    )
    registration_date = serializers.DateTimeField(
        required=False, 
        default=timezone.now()
    )

    class Meta:
        model = Child
        fields = ('__all__')

class CourseSerializer(serializers.ModelSerializer):
    # course_name = serializers.CharField(max_length = 50)
    # course_description = serializers.CharField(max_length = 150)
    # teacher = serializers.CharField(max_length = 100)
    # reviews = serializers.IntegerField(default = 0)
    # creation_date = serializers.DateTimeField(
    #     required=False, 
    #     default=timezone.now()
    # )
    # update_date = serializers.DateTimeField(
    #     required=False, 
    #     default=timezone.now()
    # )

    class Meta:
        model = Course
        fields = [
            'id',
            'course_name',
            'course_description',
            'teacher',
            'reviews',
            'creation_date',
            'update_date'
        ]

class RegistrationSerializer(serializers.ModelSerializer):
    child = serializers.RelatedField(source="child", read_only=True)
    course = serializers.RelatedField(source="course", read_only=True)
    status = serializers.IntegerField(default = 0)
    creation_date = serializers.DateTimeField(
        required=False, 
        default=timezone.now()
    )
    update_date = serializers.DateTimeField(
        required=False, 
        default=timezone.now()
    )

    class Meta:
        model = Registration
        fields = ('__all__')






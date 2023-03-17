from django.contrib import admin
from .models import (Parent, Child, Course, Registration)


class ParentAdmin(admin.ModelAdmin):
    list_display = (
        'parent_name', 
        'parent_mail', 
        'parent_phone', 
        'registration_date'
    )

class ChildAdmin(admin.ModelAdmin):
    list_display = (
        'parent',
        'child_name', 
        'child_birth_date', 
        'registration_date'
    )

class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'course_name', 
        'course_description', 
        'teacher', 
        'reviews', 
        'creation_date', 
        'update_date'
    )

class RegistrationAdmin(admin.ModelAdmin):
    list_display = (
        'child', 
        'course',
        'status', 
        'creation_date', 
        'update_date'
    )

admin.site.register(
    Parent,
    ParentAdmin
)

admin.site.register(
    Child,
    ChildAdmin
)

admin.site.register(
    Course,
    CourseAdmin
)



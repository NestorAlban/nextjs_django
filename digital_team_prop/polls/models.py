import datetime
from django.db import models
from django.utils import timezone


class Parent(models.Model):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        verbose_name='ID'
    )
    parent_name = models.CharField(max_length = 100)
    parent_mail = models.CharField(max_length = 100)
    parent_phone = models.CharField(max_length = 30)
    registration_date = models.DateTimeField(
        "date registered", 
        # default=datetime.date.today,
        auto_now_add=True
    )

    def __str__(self):
        return self.parent_name


class Child(models.Model):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        verbose_name='ID'
    )
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    child_name = models.CharField(max_length = 200)
    child_birth_date = models.DateTimeField(
        "birth date", 
        auto_now_add=True
    )
    # child_mail = models.CharField(max_length = 200)
    # child_phone = models.CharField(max_length = 30)
    registration_date = models.DateTimeField(
        "date registered", 
        # default=timezone.now()
        auto_now_add=True
    )

    def __str__(self):
        return self.child_name

class Course(models.Model):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        verbose_name='ID'
    )
    course_name = models.CharField(max_length = 50)
    course_description = models.CharField(max_length = 150)
    teacher = models.CharField(max_length = 100)
    reviews = models.IntegerField(
        default=0,
        editable=False
    )
    creation_date = models.DateTimeField(
        "date registered", 
        auto_now_add=True
    )
    update_date = models.DateTimeField(
        "date registered", 
        auto_now_add=True
    )

    def __str__(self):
        return self.course_name
    

class Registration(models.Model):
    id = models.AutoField(
        auto_created=True,
        primary_key=True,
        verbose_name='ID'
    )
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.IntegerField(default = 0)
    creation_date = models.DateTimeField(
        "date registered", 
        auto_now_add=True
    )
    update_date = models.DateTimeField(
        "date registered", 
        auto_now_add=True
    )

    def __str__(self):
        return self.child





from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from .serializers import *


def index(request):
    return HttpResponse("Pag principal")

def family(request, parent_id):
    return HttpResponse(f"El padre con id {parent_id}")

def courses(request, course_id):
    return HttpResponse(f"El curso con id {course_id}")

def enrollements(request, registration_id):
    return HttpResponse(f"La matrícula con id {registration_id}")


class ParentViews(APIView):

    parent_class = ParentSerializer

    def get(self, request):
        detail = [ {
            "id": detail.id,
            "parent_name": detail.parent_name,
            "parent_mail": detail.parent_mail,
            "parent_phone": detail.parent_phone,
            "registration_date": detail.registration_date
        } 
        for detail in Parent.objects.all()]
        return Response(detail)

    def post(self, request):
        serializer = ParentSerializer(data= request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
            # return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        # else:
        #     return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class CoursesViews(APIView):

    course_class = CourseSerializer

    def get(self, request):
        detail = []
        success = False
        serializer = Course.objects.all()
        if serializer:
            success = True
            detail = [ {
                "id": detail.id,
                "name": detail.course_name,
                "description": detail.course_description,
                "teacher": detail.teacher,
                "reviews": detail.reviews,
                "creation": detail.creation_date,
                "update": detail.update_date
            } for detail in Course.objects.all()]
            
        return Response({"success": success, "detail": detail})

    def post(self, request):
        serializer = CourseSerializer(data= request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Course
from .serializers import CourseListSerializer

@api_view(['GET'])
def get_courses(request):
    courses = Course.objects.all()
    #  because it is multiple objects we pass many = True
    serializer = CourseListSerializer(courses, many=True)
    return Response(serializer.data)

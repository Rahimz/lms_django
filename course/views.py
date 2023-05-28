from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth.models import User


from .models import Course, Lesson, Comment, Category
from .serializers import CourseListSerializer, CourseDetailSerializer, LessonListSerializer, CommentSerializer, CategorySerializer, QuizSerializer, UserSerializer


@api_view(['GET'])
def get_quiz(request, course_slug, lesson_slug):
    lesson = Lesson.objects.get(slug=lesson_slug)
    quiz = lesson.quizzes.first()
    serializer = QuizSerializer(quiz)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_courses(request):
    category_id = request.GET.get('category_id', '')
    courses = Course.objects.all()

    if category_id:
        courses = courses.filter(categories__in=[int(category_id)])
    #  because it is multiple objects we pass many = True
    serializer = CourseListSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([]) # to show courses on homwpage
@permission_classes([])
def get_frontpage_courses(request):
    courses = Course.objects.all()[:4]
    #  because it is multiple objects we pass many = True
    serializer = CourseListSerializer(courses, many=True)
    return Response(serializer.data)



@api_view(['GET'])
# @authentication_classes([]) # to show courses on homwpage
# @permission_classes([])
def get_course(request, slug):
    course = Course.objects.get(slug=slug)
    course_serializer = CourseDetailSerializer(course)
    lesson_serializer = LessonListSerializer(course.lessons.all(), many=True) #many = true because it has more object than 1

    if request.user.is_authenticated:
        course_data = course_serializer.data 
    else: 
        course_data ={}
    data = {
        'course': course_data,
        'lessons': lesson_serializer.data
    }
    return Response(data)

@api_view(['GET'])
def get_comments(request, course_slug, lesson_slug):
    lesson = Lesson.objects.get(slug=lesson_slug)
    serializer = CommentSerializer(lesson.comments.all(), many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_comment(request, course_slug, lesson_slug):
    data = request.data
    name = data.get('name')
    content = data.get('content')

    course = Course.objects.get(slug=course_slug)
    lesson = Lesson.objects.get(slug=lesson_slug)
    comment = Comment.objects.create(
        course=course,
        lesson=lesson,
        name=name,
        content=content,
        created_by=request.user
    )

    serializer = CommentSerializer(comment)

    return Response(serializer.data)


@api_view(['GET'])
def get_author_courses(request, user_id):
    user = User.objects.get(pk=user_id)
    courses = user.courses.all()

    user_serializer = UserSerializer(User, many=False)
    courses_serializer = CourseListSerializer(courses, many=True)

    return Response({
        'courses': courses_serializer.data,
        'created_by': user_serializer.data
    })
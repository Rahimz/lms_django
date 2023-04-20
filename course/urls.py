from django.urls import path
from . import views 


urlpatterns = [
    path('', views.get_courses),
    path('get-frontpage-courses/', views.get_frontpage_courses),
    path('get_categories/', views.get_categories),
    path('<slug:slug>/', views.get_course),
    path('<slug:course_slug>/<str:lesson_slug>/', views.add_comment),
    path('<slug:course_slug>/<str:lesson_slug>/get-comments/', views.get_comments),
    path('<slug:course_slug>/<str:lesson_slug>/get-quiz/', views.get_quiz),
]

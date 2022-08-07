from django.contrib import admin
from .models import Course, Category, Lesson, Comment


admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Comment)
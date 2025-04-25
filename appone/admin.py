from django.contrib import admin
from .models import Teacher, Student, Course, Test, Question

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Test)
admin.site.register(Question)
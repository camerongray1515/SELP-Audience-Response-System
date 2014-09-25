from django.contrib import admin
from .models import *

@admin.register(Tutor)
class Tutor_admin(admin.ModelAdmin):
    pass

@admin.register(Student)
class Student_admin(admin.ModelAdmin):
    pass

@admin.register(Course)
class Course_admin(admin.ModelAdmin):
    pass

@admin.register(Tutor_assignment)
class Tutor_assignment_admin(admin.ModelAdmin):
    pass

@admin.register(Enrollment)
class Enrollment_admin(admin.ModelAdmin):
    pass

@admin.register(Session)
class Session_admin(admin.ModelAdmin):
    pass

@admin.register(Question)
class Question_admin(admin.ModelAdmin):
    pass

@admin.register(Question_option)
class Question_option_admin(admin.ModelAdmin):
    pass

@admin.register(Student_response)
class Student_response_admin(admin.ModelAdmin):
    pass
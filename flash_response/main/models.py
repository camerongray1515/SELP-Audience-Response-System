from django.db import models
from django.contrib.auth.models import User

# This model represents which users are tutors
class Tutor(models.Model):
    user = models.ForeignKey(User, unique=True)

# This model represents which users are students
class Student(models.Model):
    user = models.ForeignKey(User, unique=True)

# This model stores all courses that use the ARS
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

# This model stores which tutors are assigned to which course
class Tutor_assignment(models.Model):
    tutor = models.ForeignKey(Tutor)
    course = models.ForeignKey(Course)

# This model stores which students are enrolled in which course
class Enrollment(models.Model):
    student = models.ForeignKey(Student)
    course = models.ForeignKey(Course)

# This model stores individual sessions (lectures/lessons) of each course
class Session(models.Model):
    course = models.ForeignKey(Course)
    title = models.CharField(max_length=255)

# This model stores individual questions
class Question(models.Model):
    session = models.ForeignKey(Session)
    question_body = models.TextField()

# This model stores each possible answer for a question
class Question_option(models.Model):
    question = models.ForeignKey(Question)
    body = models.TextField()
    correct = models.BooleanField(default=False)

# This model stores which question option was picked by a student
class Student_response(models.Model):
    student = models.ForeignKey(Student)
    option = models.ForeignKey(Question_option)
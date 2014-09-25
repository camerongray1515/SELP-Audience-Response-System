from django.db import models
from django.contrib.auth.models import User

# This model represents which users are tutors
class Tutor(models.Model):
    user = models.ForeignKey(User, unique=True)

    def __str__(self):
        return "Tutor: {0}".format(self.user.username)

# This model represents which users are students
class Student(models.Model):
    user = models.ForeignKey(User, unique=True)

    def __str__(self):
        return "Student: {0}".format(self.user.username)

# This model stores all courses that use the ARS
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

# This model stores which tutors are assigned to which course
class Tutor_assignment(models.Model):
    tutor = models.ForeignKey(Tutor)
    course = models.ForeignKey(Course)

    def __str__(self):
        return "Tutor: {0}, Course: {1}".format(self.tutor.user.username, self.course.title)

# This model stores which students are enrolled in which course
class Enrollment(models.Model):
    student = models.ForeignKey(Student)
    course = models.ForeignKey(Course)

    def __str__(self):
        return "Student: {0}, Course: {1}".format(self.student.user.username, self.course.title)

# This model stores individual sessions (lectures/lessons) of each course
class Session(models.Model):
    course = models.ForeignKey(Course)
    title = models.CharField(max_length=255)
    url_code = models.CharField(max_length=5, default='')

    def __str__(self):
        return self.title

# This model stores individual questions
class Question(models.Model):
    session = models.ForeignKey(Session)
    question_body = models.TextField()

    def __str__(self):
        return self.question_body

# This model stores each possible answer for a question
class Question_option(models.Model):
    question = models.ForeignKey(Question)
    body = models.TextField()
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.body

# This model stores which question option was picked by a student
class Student_response(models.Model):
    student = models.ForeignKey(Student)
    option = models.ForeignKey(Question_option)

    def __str__(self):
        return "Student: {0}, Option: {1}".format(self.student.user.username, self.option.body)
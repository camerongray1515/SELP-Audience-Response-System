from django.shortcuts import render, render_to_response
from main.decorators import user_is_tutor, user_is_student

@user_is_tutor
def welcome(request):
    return render_to_response('welcome.html')

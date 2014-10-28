from django.shortcuts import render, render_to_response
from main.decorators import user_is_student
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from main.models import Session, Current_question, Question_option
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext
from django.utils import timezone

import json
import datetime
import random

@user_is_student
def respond(request, session_code):
    # If a session exists, go to the response page, otherwise throw a 404
    try:
        s = Session.objects.get(url_code=session_code, course__enrollment__student__user=request.user, running=True)
    except ObjectDoesNotExist:
        raise Http404

    data = {}

    data['session'] = s

    return render_to_response('response.html', data, context_instance=RequestContext(request))

@user_is_student
def check_question_availability(request):
    session_code = request.GET.get('session_code')

    # Check if the session exists and that the student is allowed to access it
    try:
        s = Session.objects.get(url_code=session_code, course__enrollment__student__user=request.user, running=True)
    except ObjectDoesNotExist:
        raise Http404

    data = {'question_available': False}
    # Now check if there is an assigned question for this session
    session_questions = Current_question.objects.filter(session=s).order_by('-start_time');
    if session_questions:
        newest_assignment = session_questions[0]
        # Check if this assignment is still valid
        if timezone.now() < newest_assignment.start_time:
            # Get a shuffled list of all question options
            question_options = []
            for option in Question_option.objects.filter(question=newest_assignment.question):
                question_options.append({'body': option.body, 'id': option.id})
            random.shuffle(question_options)

            # Calculate the number of miliseconds until the question is due to start
            time_to_start = (int) ((newest_assignment.start_time - timezone.now()).total_seconds() * 1000)
            data['question_available'] = True
            data['time_to_start'] = time_to_start
            data['question_body'] = newest_assignment.question.question_body
            data['question_options'] = question_options
            data['run_time'] = newest_assignment.run_time

    return HttpResponse(json.dumps(data), content_type='application/json')
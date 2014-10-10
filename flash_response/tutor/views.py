from django.shortcuts import render, render_to_response
from main.decorators import user_is_tutor, tutor_course_is_selected
from django.template import RequestContext
from django.http import HttpResponseRedirect
from main.models import Tutor_assignment, Tutor, Session, Question
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

@user_is_tutor
def welcome(request):
    return render_to_response('welcome.html', context_instance=RequestContext(request))

@csrf_exempt
@user_is_tutor
def select_course(request):
    course_id = int(request.POST['course'])

    # We first must check if the tutor is actually assigned to this course
    tutor = Tutor.objects.get(user=request.user)
    assignments = Tutor_assignment.objects.filter(tutor=tutor, course_id=course_id)

    # Could throw a pretty error here but in this should never happen in normal use of
    # the application
    if len(assignments) == 0:
        return HttpResponseRedirect('/tutor/')

    # We have verified that the tutor is assigned to the course
    # so we can set the session variable
    request.session['course_id'] = course_id
    return HttpResponseRedirect('/tutor/')

@user_is_tutor
@tutor_course_is_selected
def sessions(request):
    data = {}

    data['sessions'] = Session.objects.filter(course_id=request.session['course_id'])

    return render_to_response('sessions.html', data, context_instance=RequestContext(request))

@user_is_tutor
@tutor_course_is_selected
def new_session(request):
    data = {}

    # If the form has been submitted, add the session
    if request.method == 'POST':
        session_title = request.POST['session-title']

        # Title must be set, if not set an error message
        if session_title:
            # Add the session then redirect to the page to allow editing of it
            s = Session()
            s.title = session_title
            s.course_id = request.session['course_id']
            s.save()

            return HttpResponseRedirect('/tutor/sessions/edit/{0}'.format(s.pk))
        else:
            data['error'] = 'You must specify a title for this session'


    return render_to_response('new_session.html', data, context_instance=RequestContext(request))

@user_is_tutor
@tutor_course_is_selected
def edit_session(request, session_id):
    data = {}

    # If the form has been submitted, work out what action should be taken and do it
    if request.method == 'POST':
        question_id = request.POST['question-id']
        if 'delete' in request.POST:
            try:
                s = Session.objects.get(id=session_id, course=request.session['course_id'])
                q = Question.objects.get(pk=question_id, session=s.id)
                q.delete()
            except ObjectDoesNotExist:
                pass # If the question doesn't exist, we don't need to really do anything


    # Get the session and all questions in it
    try:
        data['session'] = Session.objects.get(id=session_id, course=request.session['course_id'])
    except ObjectDoesNotExist:
        data['error'] = 'The session specified could not be found'
        return render_to_response('error.html', data, context_instance=RequestContext(request))

    data['questions'] = Question.objects.filter(session=session_id)

    return render_to_response('edit_session.html', data, context_instance=RequestContext(request))
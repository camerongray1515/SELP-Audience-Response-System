from django.shortcuts import render, render_to_response
from main.decorators import user_is_tutor, tutor_course_is_selected
from django.template import RequestContext
from django.http import HttpResponseRedirect
from main.models import Tutor_assignment, Tutor, Session, Question, Question_option
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

            return HttpResponseRedirect('/tutor/sessions/{0}'.format(s.pk))
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

@user_is_tutor
@tutor_course_is_selected
def edit_question(request, session_id, question_id):
    data = {'type': 'edit'}

    # Check we are allowed to actually access this session
    if not Session.objects.filter(id=session_id, course=request.session['course_id']):
        data['error'] = 'The session specified could not be found'
        return render_to_response('error.html', data, context_instance=RequestContext(request))

    if request.method == 'POST':
        question = request.POST.get('question')
        max_options = request.POST.get('max-options')

        # Question must have a body set and the current course must contain the session
        if question:
            # We can now add the question to the database
            q = Question.objects.get(pk=question_id)
            q.question_body = question
            q.save()

            # Delete all current question options
            Question_option.objects.filter(question_id=question_id).delete()
            for x in range(0,int(max_options)):
                # Is there an option set at this index?
                option_body = request.POST.get('option-body[{0}]'.format(x))
                option_correct = bool(request.POST.get('option-correct[{0}]'.format(x)))
                if option_body:
                    o = Question_option()
                    o.question_id = question_id
                    o.body = option_body
                    o.correct = option_correct
                    o.save()

            return HttpResponseRedirect('/tutor/sessions/{0}/'.format(session_id))
        else:
            data['error'] = 'Your question must have a body'

    # Get the question and check the session to be sure the tutor owns the question
    try:
        q = Question.objects.get(pk=question_id)
        s = Session.objects.get(pk=q.session.pk, course=request.session['course_id'])
    except ObjectDoesNotExist:
        data['error'] = 'The question specified could not be found'
        return render_to_response('error.html', data, context_instance=RequestContext(request))
    data['question'] = q
    data['question_options'] = Question_option.objects.filter(question=q)

    return render_to_response('question_form.html', data, context_instance=RequestContext(request))

@user_is_tutor
@tutor_course_is_selected
def new_question(request, session_id):
    data = {'type': 'new'}

    # Check we are allowed to actually access this session
    if not Session.objects.filter(id=session_id, course=request.session['course_id']):
        data['error'] = 'The session specified could not be found'
        return render_to_response('error.html', data, context_instance=RequestContext(request))

    if request.method == 'POST':
        question = request.POST.get('question')
        max_options = request.POST.get('max-options')

        # Question must have a body set and the current course must contain the session
        if question:
            # We can now add the question to the database
            q = Question()
            q.session_id = session_id
            q.question_body = question
            q.save()

            for x in range(0,int(max_options)):
                # Is there an option set at this index?
                option_body = request.POST.get('option-body[{0}]'.format(x))
                option_correct = bool(request.POST.get('option-correct[{0}]'.format(x)))
                if option_body:
                    o = Question_option()
                    o.question_id = q.pk
                    o.body = option_body
                    o.correct = option_correct
                    o.save()

            return HttpResponseRedirect('/tutor/sessions/{0}/'.format(session_id))
        else:
            data['error'] = 'Your question must have a body'

    return render_to_response('question_form.html', data, context_instance=RequestContext(request))
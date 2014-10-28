from django.shortcuts import render, render_to_response
from main.decorators import user_is_student
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from main.models import Session
from django.core.exceptions import ObjectDoesNotExist
from django.template import RequestContext

@user_is_student
def respond(request, session_code):
    # If a session exists, go to the response page, otherwise throw a 404
    try:
        s = Session.objects.get(url_code=session_code, course__enrollment__student__user=request.user)
    except ObjectDoesNotExist:
        raise Http404

    data = {}

    data['session'] = s

    return render_to_response('response.html', data, context_instance=RequestContext(request))
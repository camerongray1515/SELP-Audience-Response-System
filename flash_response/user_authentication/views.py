from django.shortcuts import render, render_to_response
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from main.models import Student, Tutor
from django.http import HttpResponseRedirect

def login_main(request):
    return render_to_response('login_main.html')

def login_form(request, realm):
    data = {
        'realm': realm,
    }
    data.update(csrf(request))

    # Has the form been submitted?
    if request.method == 'POST':
        data['login_error'] = True, # This will be set to false later if login successful

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            # Is this user part of the realm we are using?
            if realm == 'student':
                is_in_realm = Student.objects.filter(user=user).count()
            elif realm == 'tutor':
                is_in_realm = Tutor.objects.filter(user=user).count()
            else:
                raise Exception('Invalid realm specified!')

            if user.is_active and is_in_realm:
                login(request, user)
                data['login_error'] = False;

                return HttpResponseRedirect('/{0}/'.format(realm))

    return render_to_response('login_form.html', data);

def do_logout(request):
    logout(request)

    return render_to_response('logout_confirmation.html')
from main.models import Tutor_assignment, Tutor
from django.core.exceptions import ObjectDoesNotExist

def course_assignments_processor(request):
    tutor = None
    if request.user.is_authenticated:
        try:
            tutor = Tutor.objects.get(user=request.user.pk) # Get the logged in tutor
        except ObjectDoesNotExist:
            pass
            
    if tutor:
        course_assignments = Tutor_assignment.objects.filter(tutor=tutor) # Get all course assignments
    else:
        course_assignments = []

    return {'course_assignments': course_assignments}
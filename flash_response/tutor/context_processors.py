from main.models import Tutor_assignment
from django.core.exceptions import ObjectDoesNotExist

def course_assignments_processor(request):            
    if tutor:
        course_assignments = Tutor_assignment.objects.filter(user=request.user) # Get all course assignments
    else:
        course_assignments = []

    return {'course_assignments': course_assignments}
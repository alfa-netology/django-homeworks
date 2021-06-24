from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    students = Student.objects.order_by('group', 'name').prefetch_related('teacher').all()

    object_list = list()

    for student in students:
        object_list.append({'student': student, 'teachers': student.teacher.all()})

    context = {'object_list': object_list}
    return render(request, template, context)

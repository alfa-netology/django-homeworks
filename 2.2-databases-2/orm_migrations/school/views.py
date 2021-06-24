from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    students = Student.objects.order_by('group').prefetch_related('teacher').all()

    object_list = list()

    for student in students:
        object_list.append({'student': student, 'teachers': student.teacher.all()})


    print(students_list)


    # for s in students:
    #     if s['name'] not in students_counter:
    #         students_counter.append(s['name'])
    #         object_list.append({'name': s['name'], 'group': s['group'],
    #                             'teachers': [{'name': s['teacher__name'], 'subject': s['teacher__subject']}]})
    #     else:
    #         for o in object_list:
    #             if o['name'] == s['name']:
    #                 o['teachers'].append({'name': s['teacher__name'], 'subject': s['teacher__subject']})
    # context = {
    #     'object_list': object_list
    # }
    # return render(request, template, context)

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'
    context = {'object_list': object_list}
    return render(request, template, context)

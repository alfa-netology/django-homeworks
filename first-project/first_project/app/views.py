from datetime import datetime
import os

from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    template_name = 'app/time.html'
    current_time = datetime.strftime(datetime.now(), "%H:%M:%S")

    context = {
        'time': current_time
    }
    return render(request, template_name, context)


def workdir_view(request):
    template_name = 'app/files.html'

    context = {
        'dir': os.path.basename(os.getcwd()),
        'files': os.listdir(os.getcwd())
    }
    return render(request, template_name, context)

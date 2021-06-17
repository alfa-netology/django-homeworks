from csv import DictReader

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open('data-398-2018-08-30.csv', encoding='utf-8', newline='') as file:
        reader = DictReader(file)
        stations = [row for row in reader]

        paginator = Paginator(stations, per_page=10)
        current_page = request.GET.get('page', 1)
        page = paginator.get_page(current_page)

    context = {
       'page': page,
       'bus_stations': page.object_list,
    }
    return render(request, 'stations/index.html', context)

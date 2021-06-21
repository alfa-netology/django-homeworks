from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', 'default')

    sorting = {
        'default': lambda: Phone.objects.all(),
        'name': lambda: Phone.objects.order_by("name"),
        'min_price': lambda: Phone.objects.order_by("price"),
        'max_price': lambda: Phone.objects.order_by("-price"),
    }

    phones = sorting[sort]()

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = [item for item in Phone.objects.filter(slug=slug).values()][0]
    context = {'phone': phone}
    return render(request, template, context)

from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def home_view(request):
    template = 'calculator/index.html'

    context = {
        'dishes': DATA.keys()
    }
    return render(request, template, context)

def dish_view(request, dish):
    template = 'calculator/dish.html'
    data = DATA.get(dish, 'no such dish')
    servings = int(request.GET.get('servings', '0'))

    has_dish = True if data != 'no such dish' else False
    has_servings = True if servings != 0 else False

    if has_dish and has_servings:
        data = {k: round(v * int(servings), 3) for k, v in data.items()}

    context = {
        'has_servings': has_servings,
        'has_dish': has_dish,
        'servings': servings,
        'dish': dish,
        'data': data,
    }
    return render(request, template, context)

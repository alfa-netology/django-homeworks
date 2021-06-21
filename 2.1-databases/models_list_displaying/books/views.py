from django.shortcuts import render, redirect

from .models import Book

def index(request):
    return redirect('catalog')

def catalog(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)

def page(request, date):

    prev_page = Book.objects.filter(pub_date__lt=date).order_by('-pub_date').first()
    next_page = Book.objects.filter(pub_date__gt=date).order_by('pub_date').first()

    prev_page = prev_page.pub_date.strftime('%Y-%m-%d') if prev_page else None
    next_page = next_page.pub_date.strftime('%Y-%m-%d') if next_page else None

    template = 'books/books_details.html'
    books = Book.objects.filter(pub_date=date)

    print(prev_page)

    context = {
        'books': books,
        'next_page': next_page,
        'prev_page': prev_page,
    }
    return render(request, template, context)

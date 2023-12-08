from django.core.paginator import Paginator
from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    book_objects = Book.objects.all()
    context = {
        'books': book_objects
    }
    return render(request, template, context)

def book_catalog(request, date):
    template = 'books/books.html'
    book_objects = Book.objects.get(pub_date=date)
    book_all = Book.objects.all()
    page_number = int(request.GET.get('page', 1))
    book_paginator = Paginator(book_all, 1)
    page = book_paginator.get_page(page_number)
    context = {
        'books': book_objects,
        'page_obj': page
    }
    return render(request, template, context)

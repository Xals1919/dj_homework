import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open('pagination/data-398-2018-08-30.csv', newline='', encoding='utf8') as csvfile:
        reader: list = list(csv.DictReader(csvfile))
    page_number: int = request.GET.get("page", 1)
    paginator = Paginator(reader, 10)
    page = paginator.get_page(page_number)

    context: dict = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)

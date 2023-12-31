from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_pages = request.GET.get('sort')
    if sort_pages == 'name':
        phone_objects = Phone.objects.order_by('name')
    elif sort_pages == 'min_price':
        phone_objects = Phone.objects.order_by('price')
    elif sort_pages == 'max_price':
        phone_objects = Phone.objects.order_by('-price')
    else:
        phone_objects = Phone.objects.all()
    context = {
        'phones': phone_objects
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_objects = Phone.objects.get(slug=slug)
    context = {
        'phone': phone_objects
    }
    return render(request, template, context)

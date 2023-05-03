from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def sort_product(request):
    sort_filter = request.GET.get('sort')
    if sort_filter == 'name':
        phone_objects = Phone.objects.all().order_by('name')
    elif sort_filter == 'min_price':
        phone_objects = Phone.objects.all().order_by('price')
    else:
        phone_objects = Phone.objects.all().order_by('price').reverse()
    return phone_objects


def show_catalog(request):
    template = 'catalog.html'
    phone_objects = sort_product(request)
    context = {
        'phones': [phone for phone in phone_objects]
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_objects = Phone.objects.filter(slug=slug)
    context = {
        'phone': [phone for phone in phone_objects][0]
    }
    return render(request, template, context)

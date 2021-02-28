from django.shortcuts import render
from django.http import HttpResponse
from django.template.defaultfilters import slugify
from .models import Phone

def welcome(request):
    return HttpResponse('its a starting page')

def show_catalog(request):
    phone_list = Phone.objects.all()
    sort_param = request.GET.get('sort')
    template = 'catalog.html'
    if sort_param == 'name':
        phone_list = phone_list.order_by('name')
    if sort_param == 'min_price':
        phone_list = phone_list.order_by('price')
    if sort_param == 'max_price':
        phone_list = phone_list.order_by('-price')

    context = {'phones': phone_list}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)

from django.shortcuts import render
from .models import order
from .forms import OrderForms
from cms.models import CmsSlider

# Create your views here.

def first_page(request):
    slider_list = CmsSlider.objects.all()
    return render(request, './index.html', {'slider_list': slider_list })

def thanks_page(request):
    name = request.GET['name']
    phone = request.GET['phone']
    element = order(order_name = name, order_phone = phone)
    element.save()
    return  render(request, "./thanks.html", {'name': name,
                                               'phone': phone})
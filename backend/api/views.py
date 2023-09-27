from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def api_home(request, *args, **kwargs):
    instance =Product.objects.all().order_by("?").first()
    data = {}

    if instance:
        '''data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price'''

        #does the same than above
        #data = model_to_dict(instance, fields=['id,', 'title', 'price', 'sale_price'])
        data = ProductSerializer(instance).data
    return JsonResponse(data)

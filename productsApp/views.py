from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Products
from .serializers import ProductsSerializer

# Create your views here.


# def index(request):
#     return HttpResponse("Hello, world. You're at the products index.")


@csrf_exempt
def productsApi(request, id=False):
    if request.method == 'GET':
        if(id == False):
            products = Products.objects.all()
            products_serializer = ProductsSerializer(products, many=True)
            return JsonResponse(products_serializer.data, safe=False)
        else:
            products = Products.objects.filter(id=id)
            products_serializer = ProductsSerializer(products)
            return JsonResponse(products_serializer.data, safe=False)
    elif request.method == 'POST':
        product_data = JSONParser().parse(request)
        products_serializer = ProductsSerializer(data=product_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse('Added successfully', safe=False)
        return JsonResponse('Failed to add', safe=False)
    elif request.method == 'PUT':
        product_data = JSONParser().parse(request)
        product = Products.objects.get(id=product_data['id'])
        products_serializer = ProductsSerializer(product, data=product_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse('Updated successfully', safe=False)
        return JsonResponse('Failed to update')
    elif request.method == 'DELETE':
        product = Products.objects.get(id=id)
        product.delete()
        return JsonResponse('Deleted successfully', safe=False)

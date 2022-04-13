from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from rest_framework import status

@api_view(['GET', 'POST'])
def products_list(request):

    if request.method == 'GET':
        cars = Product.objects.all()
        serializer = ProductSerializer(cars, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)       

@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    car = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        serializer = ProductSerializer(car)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(car, data=request.data) 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
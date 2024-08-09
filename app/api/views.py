from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .models import Car
from .serializers import CarSerializer


@api_view(['GET', 'POST'])
def car_list_create(request) -> Response:
    if request.method == 'GET':
        cars = Car.objects.all()

        # Фильтрация
        filter_params = {
            'brand': 'brand',
            'model': 'model',
            'year': 'year',
            'fuel_type': 'fuel_type',
            'transmission': 'transmission',
            'mileage_min': 'mileage__gte',
            'mileage_max': 'mileage__lte',
            'price_min': 'price__gte',
            'price_max': 'price__lte',
        }

        filter_criteria = {lookup: request.query_params.get(param)
                           for param, lookup in filter_params.items()
                           if request.query_params.get(param) is not None}

        cars = cars.filter(**filter_criteria)

        # Пагинация
        paginator = PageNumberPagination()
        paginated_cars = paginator.paginate_queryset(cars, request)
        if paginated_cars is not None:
            serializer = CarSerializer(paginated_cars, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    # POST запрос
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def car_detail(request, pk) -> Response:
    try:
        car = Car.objects.get(pk=pk)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CarSerializer(car)
    return Response(serializer.data)

from .models import Food
from rest_framework import viewsets
from .serializer import FoodSerializer
from django.shortcuts import render


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


def home(response):
    return render(response, "kcal/home.html", {})


def base(response):
    return render(response, "kcal/base.html", {})


def Foodlist(request):
    foodlist=Food.objects.all()
    context = {
        'object': foodlist
    }
    return render(request, "kcal/foodlist.html", context)

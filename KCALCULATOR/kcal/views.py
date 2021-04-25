from .models import Food
from rest_framework import viewsets
from .serializer import FoodSerializer
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


def home(response):
    return render(response, "kcal/home.html", {})


def base(response):
    return render(response, "kcal/base.html", {})


def foodlist(response):
    return render(response, "kcal/foodlist.html", {})

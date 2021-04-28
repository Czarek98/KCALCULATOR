from .models import Food
from rest_framework import viewsets
from .serializer import FoodSerializer
from django.shortcuts import render
from django.views.generic import DetailView, ListView


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class Foodlist(ListView):
    model = Food
    template_name = 'kcal/foodlist.html'


class FoodDetail(DetailView):
    model = Food
    template_name = 'kcal/food_detail.html'

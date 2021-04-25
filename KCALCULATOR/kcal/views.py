from .models import Food
from rest_framework import viewsets
from .serializer import FoodSerializer
from django.template import loader


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

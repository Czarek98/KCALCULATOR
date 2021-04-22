from .models import Food
from rest_framework import viewsets
from .serializer import FoodSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

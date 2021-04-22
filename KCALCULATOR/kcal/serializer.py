from .models import Food
from rest_framework import serializers


class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'name', 'grams', 'kcal', 'proteins', 'fat', 'carbs', 'status']

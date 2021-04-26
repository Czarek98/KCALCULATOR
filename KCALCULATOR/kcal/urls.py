from rest_framework import routers
from django.urls import include, path
from .views import FoodViewSet, base, home, Foodlist

router = routers.DefaultRouter()
router.register(r'foods', FoodViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('home/', home),
    path('', base),
    path('home/list', Foodlist)
]

from rest_framework import routers
from django.urls import include, path
from .views import FoodViewSet, Foodlist, FoodDetail

router = routers.DefaultRouter()
router.register(r'foods', FoodViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('foodlist', Foodlist.as_view(), name="food"),
    path('foodlist/<int:pk>', FoodDetail.as_view(), name="food-detail")
]

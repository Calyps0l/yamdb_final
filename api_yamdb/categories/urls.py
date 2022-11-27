from categories.views import CategoryViewSet
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router_v1 = DefaultRouter()
router_v1.register(r'', CategoryViewSet, basename='categories')

urlpatterns = []

urlpatterns += path('v1/categories/', include(router_v1.urls)),

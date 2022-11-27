from django.urls import include, path
from genres.views import GenreViewSet
from rest_framework.routers import DefaultRouter

router_v1 = DefaultRouter()
router_v1.register(r'', GenreViewSet, basename='genres')

urlpatterns = []

urlpatterns += path('v1/genres/', include(router_v1.urls)),

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from titles.views import TitleViewSet

router_v1 = DefaultRouter()
router_v1.register(r'', TitleViewSet, basename='titles')

urlpatterns = []

urlpatterns += path('v1/titles/', include(router_v1.urls)),

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router_v1 = DefaultRouter()
router_v1.register(r'', views.UserViewSet, basename='users')
auth_patterns_v1 = [
    path('signup/', views.get_confirmation_code),
    path('token/', views.get_jwt_token)
]

urlpatterns = []

urlpatterns += (
    path('v1/auth/', include(auth_patterns_v1)),
    path('v1/users/', include(router_v1.urls))
)

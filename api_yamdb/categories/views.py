from api.permissions import IsAdmin, IsSuperUser, PermissionClassMixin
from categories.models import Category
from categories.serializers import CategorySerializer
from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny


class CategoryViewSet(PermissionClassMixin,
                      mixins.CreateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet,
                      ):
    model = Category
    queryset = Category.objects.all()
    permission_classes = (AllowAny, )
    filter_backends = [SearchFilter, ]
    search_fields = ['name', ]
    serializer_class = CategorySerializer
    permission_action_classes = {
        'create': [
            IsAdmin
            | IsSuperUser
        ],
        "destroy": [
            IsAdmin
            | IsSuperUser
        ]
    }

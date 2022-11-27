from api.permissions import IsAdmin, IsSuperUser, PermissionClassMixin
from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from titles.filters import TitlesFilter
from titles.models import Title
from titles.serializers import TitleListSerializer, TitleSerializer


class TitleViewSet(PermissionClassMixin, ModelViewSet):
    model = Title
    http_method_names = ['get', 'post', 'delete', 'patch']
    permission_classes = (AllowAny,)
    filter_backends = [DjangoFilterBackend, ]
    filterset_class = TitlesFilter
    action_serializers = {
        'list': TitleListSerializer,
        'retrieve': TitleListSerializer,
    }
    serializer_class = TitleSerializer
    permission_action_classes = {
        'create': [
            IsAdmin
            | IsSuperUser
        ],
        "destroy": [
            IsAdmin
            | IsSuperUser
        ],
        'partial_update': [
            IsAdmin
            | IsSuperUser
        ]
    }

    def get_serializer_class(self):
        if self.action in self.action_serializers:
            return self.action_serializers.get(self.action)
        return super().get_serializer_class()

    def get_queryset(self):
        return (Title.objects
                .annotate(rating=Avg('reviews__score'))
                .all()
                )

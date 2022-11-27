from api.permissions import IsAdmin, IsSuperUser, PermissionClassMixin
from genres.models import Genre
from genres.serializers import GenreSerializer
from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny


class GenreViewSet(PermissionClassMixin,
                   mixins.CreateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet,
                   ):
    model = Genre
    queryset = Genre.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = GenreSerializer
    filter_backends = [SearchFilter, ]
    search_fields = ['name', ]
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

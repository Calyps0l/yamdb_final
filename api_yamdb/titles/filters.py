from django_filters import CharFilter, FilterSet
from titles.models import Title


class TitlesFilter(FilterSet):
    name = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Title
        fields = [
            'category',
            'genre',
            'name',
            'year',
        ]

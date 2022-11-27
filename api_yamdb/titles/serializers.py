from datetime import date

from categories.serializers import CategorySerializer
from genres.serializers import GenreSerializer
from rest_framework.serializers import (IntegerField, ModelSerializer,
                                        ValidationError)
from titles.models import Title


class TitleSerializer(ModelSerializer):
    def validate(self, attrs):
        today = date.today()
        year = attrs.get('year')
        if year and year > today.year:
            raise ValidationError({
                'year': "Год выпуска не может быть больше чем текущий"
            })

        return attrs

    class Meta:
        model = Title
        fields = [
            'id',
            'name',
            'year',
            'description',
            'genre',
            'category',
        ]


class TitleListSerializer(ModelSerializer):
    genre = GenreSerializer(many=True)
    category = CategorySerializer()
    rating = IntegerField(read_only=True)

    class Meta:
        model = Title
        fields = [
            'id',
            'name',
            'year',
            'description',
            'genre',
            'category',
            'rating',
        ]

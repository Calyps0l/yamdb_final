from rest_framework import serializers
from reviews.models import Comment, Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )
    title = serializers.SlugRelatedField(
        slug_field='name', read_only=True
    )

    def validate(self, data):
        if self.context['request'].method != 'POST':
            return data
        title_id = self.context['view'].kwargs.get('title_id')
        review = Review.objects.filter(
            author=self.context['request'].user,
            title=title_id
        )
        if review.exists():
            raise serializers.ValidationError(
                'Нельзя добавлять отзыв на одно и тоже производение дважды'
            )
        return data

    def validate_score(self, value):
        if value > 10 or value < 1:
            raise serializers.ValidationError(
                'Поставьте оценку от 1 до 10'
            )
        return value

    class Meta:
        model = Review
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        model = Comment
        fields = [
            'id',
            'text',
            'author',
            'pub_date',
        ]

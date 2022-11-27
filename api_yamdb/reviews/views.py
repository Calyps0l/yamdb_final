from api.permissions import (AuthorOrReadOnly, IsAdmin, IsModerator,
                             IsSuperUser, PermissionClassMixin)
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from reviews.models import Review
from reviews.serializers import CommentSerializer, ReviewSerializer
from titles.models import Title


class ReviewViewSet(PermissionClassMixin, ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        (AuthorOrReadOnly | IsAdmin | IsModerator | IsSuperUser)
    ]

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        return title.reviews.all()

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, id=title_id)
        serializer.save(
            author=self.request.user,
            title=title
        )


class CommentViewSet(PermissionClassMixin, ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        (AuthorOrReadOnly | IsAdmin | IsModerator | IsSuperUser)
    ]

    def get_queryset(self):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id)
        return review.comments.all()

    def perform_create(self, serializer):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, id=review_id)
        return serializer.save(
            author=self.request.user,
            review=review
        )

from django.contrib import admin
from reviews.models import Comment, Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'author', 'score', 'pub_date']
    search_fields = ['title', 'author', 'text']
    list_filter = ['title', 'pub_date']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'author', 'review', 'pub_date']
    search_fields = ['text', 'author']
    list_filter = ['pub_date']

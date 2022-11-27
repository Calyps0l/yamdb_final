from django.contrib import admin
from titles.models import Title


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    list_display = ['name', 'year', 'category']
    list_filter = ['category', 'genre']
    search_fields = ['name', ]

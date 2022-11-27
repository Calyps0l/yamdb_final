from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    slug = models.SlugField(_("Slug"), primary_key=True, unique=True)
    name = models.CharField(_("Название"), max_length=50)

    def __str__(self):
        return f'{self.name} (slug: {self.slug})'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

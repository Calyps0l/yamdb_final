from django.db import models
from django.utils.translation import gettext_lazy as _


class Title(models.Model):
    name = models.CharField(_("Название"), max_length=128)
    year = models.IntegerField(_("Год выпуска"))
    description = models.TextField(_("Описание"), null=True, blank=True)
    genre = models.ManyToManyField(
        "genres.Genre",
        verbose_name=_("Жанры")
    )
    category = models.ForeignKey(
        "categories.Category",
        verbose_name=_("Категория"),
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

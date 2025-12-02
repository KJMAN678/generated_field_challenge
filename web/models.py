from django.db import models
from django.db.models import F, Func, Value
from django.db.models.functions import Cast


class MakeDate(Func):
    function = "MAKE_DATE"
    output_field = models.DateField()


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="タイトル")
    author = models.CharField(max_length=255, verbose_name="著者")
    selled_year = models.PositiveIntegerField(verbose_name="発売年")
    selled_month = models.PositiveIntegerField(verbose_name="発売月")
    selled_date = models.GeneratedField(
        expression=MakeDate(
            Cast(F("selled_year"), models.IntegerField()),
            Cast(F("selled_month"), models.IntegerField()),
            Value(1),
        ),
        output_field=models.DateField(),
        db_persist=True,
    )

    class Meta:
        verbose_name = "本"
        verbose_name_plural = "本"

    def __str__(self) -> str:
        return self.title

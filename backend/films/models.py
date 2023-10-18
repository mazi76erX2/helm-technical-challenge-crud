from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Genre(models.Model):
    name: models.CharField = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Film(models.Model):
    title: models.CharField = models.CharField(max_length=200)
    length: models.PositiveIntegerField = models.PositiveIntegerField(
        blank=True, null=True
    )
    year: models.PositiveIntegerField = models.PositiveIntegerField(
        blank=True, null=True
    )
    score: models.FloatField = models.FloatField(
        blank=True, null=True, validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    genre: models.ForeignKey = models.ForeignKey(
        Genre, blank=True, null=True, on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        if self.year:
            return f"{self.title} ({self.year})"
        return self.title

    def get_fields(self) -> list[tuple[str, str]]:
        return [
            (str(field.verbose_name), str(getattr(self, field.name)))
            if field.name != "genre"
            else (
                str(field.verbose_name),
                Genre.objects.get(pk=getattr(self, field.name)).name,
            )
            for field in self.__class__._meta.fields[1:]
        ]

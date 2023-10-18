from django.db import models

from rest_framework import viewsets, generics
from typing import Any

from .models import Film
from .serializers import FilmSerializer


class FilmViewSet(viewsets.ModelViewSet):
    queryset: models.QuerySet[Film] = Film.objects.all()
    serializer_class: Any = FilmSerializer


class FilmListView(generics.ListAPIView):
    queryset: models.QuerySet[Film] = Film.objects.all()
    serializer_class: Any = FilmSerializer


class FilmDetailView(generics.RetrieveAPIView):
    queryset: models.QuerySet[Film] = Film.objects.all()
    serializer_class: Any = FilmSerializer


class FilmCreateView(generics.CreateAPIView):
    queryset: models.QuerySet[Film] = Film.objects.all()
    serializer_class: Any = FilmSerializer


class FilmUpdateView(generics.UpdateAPIView):
    queryset: models.QuerySet[Film] = Film.objects.all()
    serializer_class: Any = FilmSerializer


class FilmDeleteView(generics.DestroyAPIView):
    queryset: models.QuerySet[Film] = Film.objects.all()
    serializer_class: Any = FilmSerializer

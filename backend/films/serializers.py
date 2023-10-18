from rest_framework import serializers

from .models import Film, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name"]


class FilmSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()

    class Meta:
        model = Film
        fields = ["id", "title", "length", "year", "score", "genre"]

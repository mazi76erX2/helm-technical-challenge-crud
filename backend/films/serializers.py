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

    def create(self, validated_data):
        genre_data = validated_data.pop("genre")
        genre_serializer = GenreSerializer(data=genre_data)
        genre_serializer.is_valid(raise_exception=True)
        genre = genre_serializer.save()
        validated_data["genre"] = genre
        film = Film.objects.create(**validated_data)
        return film

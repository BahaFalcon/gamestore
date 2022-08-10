from rest_framework import serializers

from .models import Game, Genre


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'title',)


class GameSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    genres = GenreSerializer(many=True)

    class Meta:
        model = Game
        fields = ('id', 'name', 'genres', 'image', 'description', 'video_url', 'price', 'available',)
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Game, Genre
from .serializers import GameSerializer, GenreSerializer
from rest_framework.pagination import PageNumberPagination


class GameAPIListPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'
    max_page_size = 10000


class GameAPIList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = GameAPIListPagination


class GameAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        genre = Genre.objects.get(pk=pk)
        return Response({'genre': genre.title})

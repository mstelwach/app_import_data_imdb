from django.db.models import Q
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from imdb.models import Actor, Movie
from imdb.serializers import MovieSerializer, ActorSerializer, ActorDetailSerializer, MovieDetailSerializer


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 1000


class ActorListAPIView(generics.ListCreateAPIView):
    lookup_field = 'pk'
    serializer_class = ActorSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        qs = Actor.objects.all().order_by('pk')
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(profession=query) | Q(last_name=query)).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ActorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ActorDetailSerializer

    def get_queryset(self):
        return Actor.objects.all()


class MovieListAPIView(generics.ListCreateAPIView):
    lookup_field = 'pk'
    serializer_class = MovieSerializer
    pagination_class = LargeResultsSetPagination

    def get_queryset(self):
        qs = Movie.objects.all().order_by('pk')
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(genres__icontains=query) | Q(start_year=query)).distinct()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MovieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = MovieDetailSerializer

    def get_queryset(self):
        return Movie.objects.all()





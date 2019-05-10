from django.conf.urls import url

from imdb import views

urlpatterns = [
    url(r'^actors/list/$', views.ActorListAPIView.as_view(),
        name='actor-list'),
    url(r'^actor/(?P<pk>(\d)+)/$', views.ActorDetailAPIView.as_view(),
        name='actor-detail'),
    url(r'^movies/list/$', views.MovieListAPIView.as_view(),
        name='movie-list'),
    url(r'^movie/(?P<pk>(\d)+)/$', views.MovieDetailAPIView.as_view(),
        name='movie-detail'),
]
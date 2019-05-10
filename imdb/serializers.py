from rest_framework import serializers

from imdb.models import Actor, Movie


class ActorSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(view_name='actor-detail')

    class Meta:
        model = Actor
        fields = [
            'first_name',
            'last_name',
            'detail'
        ]
        read_only_fields = ['pk']


class MovieSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(view_name='movie-detail')

    class Meta:
        model = Movie
        fields = [
            'pk',
            'name',
            'genres',
            'start_year',
            'detail'
        ]

        read_only_fields = ['pk']

    def validate_name(self, value):
        title = Movie.objects.filter(name__iexact=value)
        if self.instance:
            title = title.exclude(pk=self.instance.pk)
        if title.exists():
            raise serializers.ValidationError('This title has already been used.')


class ActorDetailSerializer(serializers.ModelSerializer):
    movies = serializers.StringRelatedField(source='moviecast_set', many=True, read_only=True)

    class Meta:
        model = Actor
        fields = [
            'first_name',
            'last_name',
            'birth_year',
            'death_year',
            'profession',
            'movies',
        ]
        read_only_fields = ['first_name', 'last_name']


class MovieDetailSerializer(serializers.ModelSerializer):
    cast = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = [
            'name',
            'type_title',
            'genres',
            'is_adult',
            'start_year',
            'end_year',
            'run_time',
            'cast',
        ]
        read_only_fields = ['name', 'type_title']


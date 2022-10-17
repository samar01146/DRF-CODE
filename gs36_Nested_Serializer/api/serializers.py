from .models import Singer, Song
from rest_framework import serializers
# field ke under Field is called nested serializer


class SongSerializer(serializers.ModelSerializer):
    singer =  serializers.StringRelatedField(read_only=True )
    class Meta:
        model = Song
        fields = ['id' , 'title' , 'singer' , 'duration' ]


class SingerSerializer(serializers.ModelSerializer):
    song = SongSerializer(many=True, read_only=True )
    class Meta:
        model = Singer
        fields = ['id' , 'name' , 'gender' , 'song' ]
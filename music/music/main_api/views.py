from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from song.models import Song
from .serializers import SongSerializer

class SongView(APIView):
    
    def get(self, request, *args, **kwargs):
        all_songs = Song.objects.all()
        serializer = SongSerializer(all_songs, many=True)
        return Response(serializer.data)
    
    def post(slef, request):
        return Response(0)
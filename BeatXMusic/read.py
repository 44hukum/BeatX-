from .models import Song
#returns the songs
class ReadMusic:
    def readMusic(self,data):
        return Song.objects.get(pk=data)

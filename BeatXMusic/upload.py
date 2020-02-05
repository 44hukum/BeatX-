from .models import Song
from .models import MusicMetaData
#uploads the songs
class UploadSong:
    def uploadSong(self,song,user):
         obj=Song(uploadedby=user,song=song)
         obj.save()
         return True,obj.id

    def musicData(self,son,des,usr,dur,art,tit):
         music=MusicMetaData(song=son,description=des,title=tit,user=usr,artist=art)
         music.save()
         return True

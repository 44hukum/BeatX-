#Here the metadata of the uploaded music is extracted using TinyTag module
# of python: to know more about Tiny tag follow the link
#https://pypi.org/project/tinytag/
#
import os #to perform the basic search in
from tinytag import TinyTag

class MusicMeta:
     isTrue=False
     art=''
     time=''
     def metadata(self,music,user):
     #for the title of the music for different types of music file extension
            #MP3, OGG, OPUS, MP4, M4A, FLAC, WMA and Wave
         description=""
         title=""
         artist=""
         duration=0 #returns the duration in seconds
         filename=os.path.basename(music) #gives only the file name
         #file name conversion for different file type
         if filename.endswith('.mp3'):
             description=filename.split('.mp3')
             description="".join(description)
         elif f.endswith('.ogg'):
             description=filename.split('.ogg')
             description="".join(description)
         elif f.endswith('.wav'):
             description=filename.split('.wav')
             description="".join(description)
         elif f.endswith('.opus'):
             description=filename.split('.opus')
             description="".join(description)
         songdata=TinyTag.get(music)
         title=songdata.title #returns the title of the song
         #returns the duration in seconds with only roundoff to second figure
         duration=str(round(float(songdata.duration),2))
         duration=duration.split('.')
         duration=':'.join(duration)
         #for artist
         artist=songdata.artist
         if artist == None:
             artist="unknown"
         if title == None:
             title="unknown"
         return description,user,duration,artist,title

#4:th function of crud where the user is deleted from the database
from .models import Registration
from BeatXMusic.models import Song
import os #class to remove the file
class DeleteUser:
    def deleteuser(self,user):
        isTrue=False
        usertodelete=Registration.register.get(username=user)
        ab=Song.objects.filter(uploadedby_id=usertodelete.id)
        for i in ab:
            path=i.song.path
            os.remove(path)
        a=usertodelete.delete()
        if a:
            isTrue=True
        return isTrue

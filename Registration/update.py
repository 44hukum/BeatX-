#3:Update functiionality
from .models import Registration
from BeatXMusic.models import MusicMetaData
class UpdateUserData:
    def update(self,curr,userr,phone,passw):
        use=Registration.register.get(username=curr)
        use.username=userr
        use.phone_number=phone
        use.password=passw
        use.save()
        updatinguploadprofile=MusicMetaData.objects.filter(user=curr)
        for i in updatinguploadprofile:
            i.user=userr
            i.save()
        return True

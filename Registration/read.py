from .models import Registration

# 2: Read of the crud functionality, here with the user request for find friends BeatX engine
#and also provides the functionality to read the user
#returns all the users
class BeatXUsers:
    def users(self):
        obj=Registration.register.all()
        return obj
    def userProfile(self,req):
        try:
            obj=Registration.register.get(username=req)
            return obj
        except:
            return False
    def prof(self,req):
        obj=Registration.register.get(id=req)
        return obj

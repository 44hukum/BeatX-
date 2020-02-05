#where the friends are registered
from Registration.models import Friends
class Addfriend:

    def addfriend(self,user,friend):        
        friendobj=Friends()
        friendobj.friend_user=friend
        friendobj.self_user=user
        friendobj.save()
        return True

from Registration.models import Registration,Friends
class ListFriend:
    def listfriend(self,user):
        user=Registration.register.get(username=user)
        friend=Friends.objects.filter(self_user_id=user.id)
        user=[]
        for i in friend:
            user.append(Registration.register.get(id=i.friend_user_id))
        return user

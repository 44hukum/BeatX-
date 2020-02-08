from Registration.models import Registration,Friends
class FriendFilter:
    def filter(self,user):
        reg=(Registration.register.get(username=user)).id
        try:
            friends=Friends.objects.get(self_user_id=reg)
            registeredUser=Registration.register.all()
            list=[]
            for i in registeredUser:
                if i.id == friends.friend_user_id:
                    pass
                elif i.id != friends.friend_user_id:
                    list.append(i.id)
            return True,list
        except:
            return False,'h'

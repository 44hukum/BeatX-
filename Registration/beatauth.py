from .models import Registration
#where the user are authorized to use the beart
class Authorize_Beat_User:
    def authorize(self,user,password):
        isTrue=False
        message=""
        #search for the user using user name in the registration database
        try:
            beatuser=Registration.register.get(username__exact=user)
            if beatuser:
                if password == beatuser.password:  #if beaAuth found the user then it check wether the password is correct or not
                     isTrue=True
                     message=beatuser.username
                else:
                    message="password is incorrect"
            else:
                message="user not found "
        except:
            message="user does  not exist"

        return isTrue,message

from .models import Registration
from .create import UserCreation
#where the user input are validated
class beat_user_authentication:
    def validator(self,user,email,phone,gender,passw):
        u=Registration.register.filter(username=user) #checks wether the user is available or not
        message=""
        isTrue=False
        if not u:
            e=Registration.register.filter(email_addr=email)
            if not e:
                p=Registration.register.filter(phone_number=phone)
                if not p:
                    userCreationModule=UserCreation()
                    isTrue=userCreationModule.create(user,email,phone,gender,passw)
                    registereduser=Registration.register.get(username=user)
                    message=registereduser.username #returns the name of the registered user
                else:
                    message="phone number already used"
            else:
                message="email already taken"

        else:
            message="user name already taken" #returns message if the user is already taken
        return isTrue,message

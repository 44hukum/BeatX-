from .models import Registration
#where the user creation occurs
#1st: functionality of the crud
class UserCreation:
    def create(self,user,email,phone,gender,passw):
        usercreation=Registration(username=user,gender=gender)
        usercreation.phone_number=phone
        usercreation.email_addr=email
        usercreation.password=passw
        usercreation.save()
        self.user=Registration.register.filter(username=user) #conforms the user creation
        return self.user #return true if the user exists

from django.test import SimpleTestCase
from django.urls import reverse,resolve
from Registration.views import index,login,signup,forgetpass,logout,deleteUser

#url testing 1
class TestRegistrationUrls(SimpleTestCase):
    def test_Registration_index_urls_resolved(self):
        url=reverse('Registration:index') #reserve method traces the url path
        self.assertEquals(resolve(url).func,index)

        #testing the login url
    def test_Registration_login_urls_resolved(self):
        url=reverse('Registration:login')
        self.assertEquals(resolve(url).func,login)
        #testing the signup url
    def test_Registration_signup_urls_resolved(self):
        url=reverse('Registration:signup')
        self.assertEquals(resolve(url).func,signup)
        #testing the forgetpass url
    def test_Registration_forgetpass_urls_resolved(self):
        url=reverse('Registration:forgetpass')
        self.assertEquals(resolve(url).func,forgetpass)
        #testing the logout url
    def test_Registration_logout_urls_resolved(self):
        url=reverse('Registration:logout')
        self.assertEquals(resolve(url).func,logout)
        #testing the deleteuser url
    def test_Registration_delete_urls_resolved(self):
        url=reverse('Registration:deleteUser')
        self.assertEquals(resolve(url).func,deleteUser)


        

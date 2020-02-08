from django.test import TestCase, Client #client is used to memic how the user can excess our views
from django.urls import reverse
from Registration.models import Registration,Friends

#Registration views testing
class TestRegistrationViews(TestCase):
    def setup(self): #setup file for each test
        self.client = Client()


     #testing the index view
    def test_index_view(self):
        response = self.client.get(reverse('Registration:index'))
        self.assertEquals(response.status_code,200) #if the request returned the
        self.assertTemplateUsed(response,'Registration/login.html') #used the template

        #testing the login_view
    def test_login_view(self):
        response=self.client.get(reverse('Registration:login'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'Registration/login.html')
            #when the user is successfully logged in
        response_twice=self.client.post(reverse('Registration:login'),username='a',password='11',follow=True)
        a=response_twice.redirect_chain # user authentication required
        self.assertEquals(response_twice.status_code,200)
        self.assertTemplateUsed(response_twice,'Registration/login.html')

       #testing the signup view
    def test_signup_view(self):
        response=self.client.get(reverse('Registration:signup'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'Registration/signup.html')
          #user login test
        signup=Registration.register.create(
            username='test1',
            email_addr='test1@email.com',
            gender="male",
            password="123",
            phone_number="9803251923"
        )
        response_for_signup=self.client.post(reverse('Registration:signup'),{
          'username':'test1',
          'emailaddr':'test1@email.com',
          'gender':"male",
          "password":"123",
          "password2":"123",
          "phone_number":"9803251923"
        })
        self.assertEquals(response_for_signup.status_code,200)

       #testing the logout view
    def test_logout_view(self):
        response=self.client.get(reverse('Registration:logout'),follow=True)
        redirectionToIndex=response.redirect_chain
        #checks wether the redirection to index is successfull or not
        self.assertEquals(redirectionToIndex[0][1],302)

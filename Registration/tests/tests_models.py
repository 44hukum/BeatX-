#testing models
from django.test import TestCase
from Registration.models import Registration,Friends

#Registration views testing
class TestRegistrationmodels(TestCase):
     #user creation
    def test_usercreation_model(self):
        Registration.register.create(
        username='test1',
        email_addr='test1@email.com',
        gender="male",
        password="123",
        phone_number="9803251923"
        )
        user=Registration.register.get(username='test1')
        self.assertEquals(user.username,'test1')

    def test_friend_model(self):
        Registration.register.create(
        username='test1',
        email_addr='test1@email.com',
        gender="male",
        password="123",
        phone_number="9803251923"
        )
        Registration.register.create(
        username='test2',
        email_addr='test2@email.com',
        gender="male",
        password="1232",
        phone_number="19803251923"
        )
        #testing the friend creation
        user=Registration.register.get(username='test1')
        friend=Registration.register.get(username='test2')
        Friends.objects.create(self_user=user,friend_user=friend)

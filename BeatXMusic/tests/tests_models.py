#testing models
from django.test import TestCase
from Registration.models import Registration
from BeatXMusic.models import Song
#Registration views testing
class TestBeatXmodels(TestCase):
     #user creation
    def test_songcreation_model(self):
        #creats the user to save the Registration instance
        Registration.register.create(
        username='test1',
        email_addr='test1@email.com',
        gender="male",
        password="123",
        phone_number="9803251923"
        )
        user=Registration.register.get(username='test1')
        Song.objects.create(uploadedby=user,song="file") #Songs data
        song=Song.objects.get(uploadedby_id=user.id)
        self.assertEquals(song.song,'file')

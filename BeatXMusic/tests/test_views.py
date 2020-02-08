from django.test import TestCase, Client #client is used to memic how the user can excess our views
from django.urls import reverse
from BeatXMusic.models import Song,MusicMetaData
from importlib import import_module
from django.conf import settings

#Registration views testing
class TestBeatXViews(TestCase):
    def setup(self): #setup file for each test
        self.client = Client()
          #handeling the session

    def test_index_view(self):
        response = self.client.get(reverse('BeatXMusic:index'))
        self.assertEquals(response.status_code,200) #if the request returned the
        self.assertTemplateUsed(response,'Registration/login.html') #used the template

    def test_pages_view(self):
        response = self.client.get(reverse('BeatXMusic:pages',args=['profile']))
        self.assertEquals(response.status_code,200)

    def test_search_views(self):
        response=self.client.get(reverse('BeatXMusic:search',args=[1,3]))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'Registration/login.html') #used the template

    def test_friend_views(self):
        response=self.client.get(reverse('BeatXMusic:searchfriend'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'Registration/login.html') #used the template

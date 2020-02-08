from django.test import SimpleTestCase
from django.urls import reverse,resolve
from BeatXMusic.views import index,searchfriend,uploadprofile,uploadprofilee
from BeatXMusic.views import updateProfile,search,download,pages,addfriend
from BeatXMusic.views import searchSong
#url testing 1
class TestBeatXUrls(SimpleTestCase):
    def test_beatX_index_urls_resolved(self):
        url=reverse('BeatXMusic:index') #reserve method traces the url path
        self.assertEquals(resolve(url).func,index)
    #
    #     for search friend
    def test_beatX_searchFriend_resolved(self):
        url=reverse('BeatXMusic:searchfriend')
        self.assertEquals(resolve(url).func,searchfriend)
     #for upload profile
    def test_beatX_uploadprofile_urls_resolved(self):
        url=reverse('BeatXMusic:uploadprofile')
        self.assertEquals(resolve(url).func,uploadprofile)
     #for upload profile from profile page
    def test_beatX_uploadprofilee_urls_resolved(self):
        url=reverse('BeatXMusic:uploadprofilee')
        self.assertEquals(resolve(url).func,uploadprofilee)
    #to search song
    def test_beatX_searchSong_urls_resolved(self):
        url=reverse('BeatXMusic:searchSong')
        self.assertEquals(resolve(url).func,searchSong)
     #to updateProfile
    def test_beatX_updateProfile_urls_resolved(self):
        url=reverse('BeatXMusic:updateProfile')
        self.assertEquals(resolve(url).func,updateProfile)
     #to search friends
    def test_beatX_search_urls_resolved(self):
        #since the url pattern takes two field as integer
        url=reverse('BeatXMusic:search',args=[1,2])
        self.assertEquals(resolve(url).func,search)
     #to download friends
    def test_beatX_download_urls_resolved(self):
        #since the url pattern takes 1 argument as integer
        url=reverse('BeatXMusic:download',args=[1])
        self.assertEquals(resolve(url).func,download)
    #for pages to return profile
    def test_beatX_pages_urls_resolved(self):
        #since the url pattern takes 1 argument as str
        url=reverse('BeatXMusic:pages',args=["profile"])
        self.assertEquals(resolve(url).func,pages)
     #to add friend
    def test_beatX_addfriend_urls_resolved(self):
        #since the url pattern takes 1 argument as str and integer
        url=reverse('BeatXMusic:addfriend',args=["profile",2])
        self.assertEquals(resolve(url).func,addfriend)

from django.urls import path
from . import views
app_name='BeatXMusic'

urlpatterns=[
    path('',views.index,name='index'),
    path('searchfriend/',views.searchfriend,name='searchfriend'),
    path('uploadprofile/',views.uploadprofile,name='uploadprofile'),
    path('uploadprofilee/',views.uploadprofilee,name='uploadprofilee'),
    path('searchSong/',views.searchSong,name="searchSong"),
    path('updateProfile/',views.updateProfile,name="updateProfile"),
    path('search/<int:songs>/<int:uid>/',views.search,name="search"),
    path('download/<int:path>/',views.download,name='download'),
    path('<str:profile>/',views.pages,name='pages'),
    path('<str:profile>/<int:uid>/',views.addfriend,name='addfriend'),
]

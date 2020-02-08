from django.shortcuts import render,redirect
from django.conf import settings
import os
from django.http import HttpResponse, Http404
from Registration.read import BeatXUsers #imorting the read file for the user
# from  .forms import SongForm
from .musicMetaData import MusicMeta #importing the custom made music metadata
from .models import Song,MusicMetaData
from Registration.read import BeatXUsers
from .upload import UploadSong #class to upload file
from .read import ReadMusic #to read the Songs data
from django.db.models import Q
from Registration.update import UpdateUserData
from .addfriend import Addfriend
from .friendFilter import FriendFilter
from .listfriends import ListFriend
from Registration.models import Registration,Friends

def index(request):
    if request.session.has_key('beatX_user'):
        beat=BeatXUsers() #creating the object of the
        userobj=beat.userProfile(request.session['beatX_user'])
        if userobj == False:
            return redirect('Registration:logout')
        name=userobj.username
        userfriendss=(ListFriend()).listfriend(request.session['beatX_user'])

        if request.POST:
            #saving the files
             songfile=request.FILES['userssongs']
             user=request.session['beatX_user']
             obj=BeatXUsers() #to create the Registration instance
             registration_instance=obj.userProfile(user)
             obj=UploadSong()
             success=obj.uploadSong(songfile,registration_instance)
             if success[0]:
                 songs=Song.objects.get(pk=success[1]) #takes the primary key as a argument
                                  #from the read.py file get the songs file
                 meta=(MusicMeta()).metadata(songs.song.path,user) #extracting metadata
                 musicdata=obj.musicData(songs,meta[0],meta[1],meta[2],meta[3],meta[4]) #sending the music metadata to the database
                 if musicdata:
                     return redirect('BeatXMusic:search',songs=success[1],uid=0)
        return render(request,'BeatXMusic/homepage.html',{'allthefriend':userfriendss,'username':name,'profile':userobj.profile_pic})
    else:
         return render(request,'Registration/login.html')

def pages(request,profile):
    if request.session.has_key('beatX_user'):
        userfriendss=(ListFriend()).listfriend(request.session['beatX_user'])
        a=request.session['beatX_user']
        beat=BeatXUsers() #creating the object of the
        userobj=beat.userProfile(a)
        name=userobj.username
        if profile == "findfriends":
            beat=BeatXUsers() #creating the object of the
            availableusers=beat.users()
            #friend filter
            users=FriendFilter().filter(request.session['beatX_user'])
            if users[0]:
                ans=users[1]
            else:
                ans=1
            objectsForHtmlPages={
            'friends':True,
            'users': availableusers,
            'username':name,
            'profile':userobj.profile_pic,
            'nottofind':request.session['beatX_user'],
            'meto': ans,
            'allthefriend':userfriendss,
            }
            return render(request,'BeatXMusic/homepage.html',objectsForHtmlPages)
        if profile == 'viewProfile':
            a=request.session['beatX_user']
            beat=BeatXUsers() #creating the object of the
            userobj=beat.userProfile(a)
            name=userobj.username
            str=name.split() #converts the user name to the list
            str=''.join(str)
            uid='@'+str
            counter=Registration.register.get(username=request.session['beatX_user'])
            friendCount=Friends.objects.filter(self_user_id=counter.id).count() #returns the total friends
            return render(request,'BeatXMusic/userprofile.html',{'totalfr':friendCount,'allthefriend':userfriendss,'username':name,'uid':uid,'profile':userobj.profile_pic})
        else:
            return render(request,'BeatXMusic/homepage.html',{'allthefriend':userfriendss,'username':name,'profile':userobj.profile_pic})

        return render(request,'BeatXMusic/homepage.html',{'allthefriend':userfriendss,'message': profile })
    else:
         return render(request,'Registration/login.html')


#search for the songs
def search(request,songs,uid):
    userfriendss=(ListFriend()).listfriend(request.session['beatX_user'])
    if songs==1:
        if request.session.has_key('beatX_user'):
            a=request.session['beatX_user']
            beat=BeatXUsers() #creating the object of the
            userobj=beat.userProfile(a)
            name=userobj.username
               #searching music
            musicList=[]
            musicplayable=[] #the music that will really play
            if request.method=='GET':
                query=request.GET.get('searchTerm','')
                queryMatch=MusicMetaData.objects.filter(
                    Q(description__icontains=query.replace(" ","")) |
                    Q(title__icontains=query.replace(" ","")) |
                    Q(user__icontains=query.replace(" ",""))
                )
                #for loop for all the result
                for i in queryMatch:
                    musicList.append(tuple((i.song_id,i.user,i.title,i.artist))) #appending tuple to the list so that it contains all the necessary details
                # res=[]
                # if queryMatch:
                    # for q in queryMatch:
                    #     res.append(Song.objects.get(pk=q.song))
                    #only one music

                  #uploader first ko data change place chai 1
                  #music
                music=Song.objects.get(pk=uid)
                context={
                    'aa': True,
                    'value':query,
                    'username':name,
                    'profile':userobj.profile_pic,
                    'music':music.song,
                    # 'uploader':musicList[][2],
                    # 'title':musicList[0][2],
                    # 'Artist':getdata.artist,
                    'musicl':musicList,
                    'allthefriend':userfriendss,
                }
                # return render(request,'BeatXMusic/aa.html',{'a':musicList})
                return render(request,'BeatXMusic/homepage.html',context)
                # return render(request,'BeatXMusic/homepage.html',{"aa":True})
        else:
             return render(request,'Registration/login.html')
    else:
         if request.session.has_key('beatX_user'):
             a=request.session['beatX_user']
             beat=BeatXUsers() #creating the object of the
             userobj=beat.userProfile(a)
             name=userobj.username

             getMusic=Song.objects.get(pk=songs)
               #sending the metadata of the song
             getdata=MusicMetaData.objects.get(song=getMusic.id)

             playSong=getMusic.song
             if request.GET:
                 val=request.GET['searchTerm']
             else:
                 val=""
             context={
                 'aa': True,
                 'value':val,
                 'username':name,
                 'profile':userobj.profile_pic,
                 'music':playSong,
                 'uploader':getdata.user,
                 'title':getdata.title,
                 'Artist':getdata.artist,
                 'allthefriend':userfriendss,
             }
             return render(request,'BeatXMusic/homepage.html',context)
             # return render(request,'BeatXMusic/homepage.html',{"aa":True})
         else:
              return render(request,'Registration/login.html')


#search the friend
def searchfriend(request):
    userfriendss=(ListFriend()).listfriend(request.session['beatX_user'])
    if request.session.has_key('beatX_user'):
        a=request.session['beatX_user']
        beat=BeatXUsers() #creating the object of the user
        availableusers=beat.users()
        userobj=beat.userProfile(a)
        name=userobj.username
        #friend filterbeat=BeatXUsers() #creating the object of the
        availableusers=beat.users()
        #friend filter
        users=FriendFilter().filter(request.session['beatX_user'])
        if users[0]:
            ans=users[1]
        else:
            ans=1
        objectsForHtmlPages={
        'friends':True,
        'users': availableusers,
        'username':name,
        'profile':userobj.profile_pic,
        'nottofind':request.session['beatX_user'],
        'meto': ans,
        'allthefriend':userfriendss,
        }
        return render(request,'BeatXMusic/homepage.html',objectsForHtmlPages)
    else:
         return render(request,'Registration/login.html')
#updats the profile pic
def uploadprofile(request):
     userfriendss=(ListFriend()).listfriend(request.session['beatX_user'])
     if request.method=='POST':
         file=request.FILES['ChangeProfilePic']
         profile=(BeatXUsers()).userProfile(request.session['beatX_user'])
         profile.profile_pic=file
         profile.save()
         return redirect('BeatXMusic:index')
#change profile from the profile pic
def uploadprofilee(request):
     userfriendss=(ListFriend()).listfriend(request.session['beatX_user'])
     if request.method=='POST':
         file=request.FILES['ChangeProfilePic']
         profile=(BeatXUsers()).userProfile(request.session['beatX_user'])
         profile.profile_pic=file
         profile.save()
         name=profile.username
         str=name.split() #converts the user name to the list
         str=''.join(str)
         uid='@'+str
         return render(request,'BeatXMusic/userprofile.html',{'allthefriend':userfriendss,'username':name,'uid':uid,'profile':profile.profile_pic})

def playSong(request,songId):
    pass
#search a song
def searchSong(request):
    userfriendss=(ListFriend()).listfriend(request.session['beatX_user'])
    if request.session.has_key('beatX_user'):
        a=request.session['beatX_user']
        beat=BeatXUsers() #creating the object of the
        userobj=beat.userProfile(a)
        name=userobj.username
           #searching music
        musicList=[]
        musicplayable=[] #the music that will really play
        if request.method=='GET':
            query=request.GET.get('searchTerm','')
            queryMatch=MusicMetaData.objects.filter(
                Q(description__icontains=query.replace(" ","_")) |
                Q(title__icontains=query.replace("","")) |
                Q(user__icontains=query.replace(" ",""))

            )
            #for loop for all the result
            for i in queryMatch:
                musicList.append(tuple((i.song_id,i.user,i.title,i.artist))) #appending tuple to the list so that it contains all the necessary details
            # res=[]
            # if queryMatch:
                # for q in queryMatch:
                #     res.append(Song.objects.get(pk=q.song))
                #only one music

              #uploader first ko data change place chai 1
              #music

            context={
                'aa': True,
                'value':query,
                'username':name,
                'profile':userobj.profile_pic,
                'music':'a',
                # 'uploader':musicList[][2],
                # 'title':musicList[0][2],
                # 'Artist':getdata.artist,
                'musicl':musicList,
                'allthefriend':userfriendss,
            }
            # return render(request,'BeatXMusic/aa.html',{'a':musicList})
            return render(request,'BeatXMusic/homepage.html',context)
#functrion to update friend
def updateProfile(request):
    userfriendss=(ListFriend()).listfriend(request.session['beatX_user'])
    if request.method=='POST':
        user=request.POST['username']
        phone_number=request.POST['phone_number']
        password1=request.POST['password']
        password=request.POST['password']
        u=request.session['beatX_user']
        if password1 == password:
            updateres=(UpdateUserData()).update(u,user,phone_number,password)
            if updateres:
                request.session['beatX_user']=user
                return redirect('BeatXMusic:index')
    else:
        a=request.session['beatX_user']
        beat=BeatXUsers() #creating the object of the
        userobj=beat.userProfile(a)
        name=userobj.username
        str=name.split() #converts the user name to the list
        str=''.join(str)
        uid='@'+str
        data={
        'username':name,
        'uid':uid,
        'profile':userobj.profile_pic,
        'update':'update',
        'number':userobj.phone_number,
        'password':userobj.password,
        'allthefriend':userfriendss,
         }
        return render(request,'BeatXMusic/userprofile.html',data)
#downloading files
def download(request, path):

    pathS=Song.objects.get(pk=path)
    a=str(pathS.song)
    file_path = os.path.join(settings.MEDIA_ROOT, a)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as downloadFile:
            response = HttpResponse(downloadFile.read(), content_type="audio/*")
            response['Content-Disposition'] = 'inline; filename='+"BeatX_user_music_" + os.path.basename(file_path)
            return response
    raise Http404

#function to add friend
def addfriend(request,profile,uid):
    userfriendss=(ListFriend()).listfriend(request.session['beatX_user'])
    a=request.session['beatX_user']
    beat=BeatXUsers() #creating the object of the
    userobj=beat.userProfile(a)
    name=userobj.username
    availableusers=beat.users()

    friend=(BeatXUsers().prof(uid))
    user=(BeatXUsers().userProfile(request.session['beatX_user']))

    b=Friends.objects.filter(friend_user_id=friend.id)
    a=Friends.objects.filter(self_user_id=user.id)
    for i in a: #checka wether the user is already friend or not
        for j in b:
            if i.id == j.id:
                return redirect('BeatXMusic:pages',profile='findfriends')


    friendAdded=Addfriend().addfriend(user,friend) #adding friend
    if friendAdded:
        return redirect('BeatXMusic:index')
    return redirect('BeatXMusic:index')

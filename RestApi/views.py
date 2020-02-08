from django.shortcuts import render,get_object_or_404
from BeatXMusic.models import Song,MusicMetaData
from django.http import  JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import TestRest

#CRUD IN Rest

@csrf_exempt
def songs_list(request):
    #1: Create
    if request.method=='POST':
        music=TestRest()
        #for security purpose it encode the joson object which should be decode(utf-8)
        decoded_data = request.body.decode('utf-8')
        musicdata=json.loads(decoded_data) #loading the dencoded data
        music.song=musicdata['song']
        music.playable=musicdata['playable']
        music.totalsong=musicdata['number']
        music.save()
        return JsonResponse({'message':'success'})

    elif request.method=='GET':
        max_data_to_show=30 #maximum number of data to show in the 1st page
        music=MusicMetaData.objects.all()[:max_data_to_show] #slicing
        data={
        "Song Detail": list(music.values("id","description","title",'user','artist','song_id')),
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'Err':'unknown error'})
#if the objects request the details
@csrf_exempt
def songs_detail(request,pk):
        #2: Read
    if request.method=='GET':
        music=get_object_or_404(MusicMetaData, pk=pk)
        data={
             'Song Detail':{
             'id': music.id,
             'Description':music.description,
             'Title':music.title,
             'User':music.user,
             'artist':music.artist,
             'song_id':music.song_id
             }
        }
        return JsonResponse(data)

        #3:update
        # updating api data which is basically music metadata
    elif request.method=='PUT':
        music=get_object_or_404(MusicMetaData, pk=pk)
        decoded_data = request.body.decode('utf-8')
        musicdata=json.loads(decoded_data) #loading the dencoded data
        #any data that user want to update they can do so
        # keycontent=list(musicdata.keys())
        # valuecontent=list(musicdata.values())
        # input=[keycontent,valuecontent]
        # a=[]
        # b=[]
        # for i in input:
        #     music.i[0]
        #     music.save()
        music.description=musicdata['description']
        music.save()
        return JsonResponse({'message':'success'})

        #4: Delete
    elif request.method=='DELETE':
        try:
            music=get_object_or_404(TestRest, pk=pk)
            music.delete()
            return JsonResponse({'messaage':'deleted'})
        except:
            test=TestRest.objects.all()
            data=list(test.values("id","song","playable","totalsong"))
            return JsonResponse({'message':'please resend the Id from','availableid': data})

#pagination for RestApi
def pagination_rest_test(request,pagenumber,size):
    if request.method=='GET':
        #here pagenumber defines the npage number and size defines the number of item to display
        music=MusicMetaData.objects.all()[(pagenumber-1):size+(pagenumber-1)]
        data={
        "Song Detail": list(music.values("id","description","title",'user','artist','song_id')),
        }
        return JsonResponse({'music':data})

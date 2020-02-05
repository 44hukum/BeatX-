from django.db import models
from Registration.models import Registration
class Song(models.Model):
     uploadedby=models.ForeignKey(Registration,on_delete=models.CASCADE, related_name="uploadsongs")
     song=models.FileField(upload_to='uploaded/')
     class Meta:
        db_table="Songs"

#where the metadata of the music resides and the music is searched from here
class MusicMetaData(models.Model):
     song=models.ForeignKey(Song,on_delete=models.CASCADE, related_name="songs_data")
     description=models.TextField('music_description')
     title=models.CharField(max_length=200)
     user=models.CharField(max_length=200)
     artist=models.CharField(max_length=200)
     
     class Meta:
         db_table="Musicdata"

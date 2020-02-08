from django.db import models

class TestRest(models.Model):
    song=models.CharField(max_length=20)
    playable=models.BooleanField()
    totalsong=models.IntegerField(default=0)

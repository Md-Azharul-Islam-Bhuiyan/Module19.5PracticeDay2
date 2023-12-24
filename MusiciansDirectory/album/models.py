from django.db import models
from musician.models import MusicianModel

class AlbumModel(models.Model):
    album_name = models.CharField(max_length=50)
    musician = models.ForeignKey(MusicianModel, on_delete=models.CASCADE)
    album_relase_date = models.DateField()
    RATING_CHOICES = [(1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),
    ]
    rating = models.IntegerField(choices=RATING_CHOICES)
    
    def __str__(self):
        return self.album_name
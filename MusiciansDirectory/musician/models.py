from django.db import models


class MusicianModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_no = models.CharField(max_length=12)
    instrument_type = models.CharField(max_length=50, default=None)
    

    def __str__(self):
        return self.first_name +' '+ self.last_name

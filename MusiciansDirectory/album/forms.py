from django import forms
from album.models import AlbumModel

class AlbumForm(forms.ModelForm):
    class Meta:
        model = AlbumModel
        fields = '__all__'
        widgets={
            'album_relase_date':forms.DateInput(attrs={'type':'date'})
        }
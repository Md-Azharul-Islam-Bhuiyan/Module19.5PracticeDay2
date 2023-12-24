from django.shortcuts import render
from album.models import AlbumModel
from django.views.generic import ListView

class HomepageView(ListView):
  model = AlbumModel
  template_name ='home.html'
  context_object_name = 'data'
  
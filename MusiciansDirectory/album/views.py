from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from  album.forms import AlbumForm
from album.models import AlbumModel
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib import messages

class AddAlbumView(CreateView):
    model = AlbumModel
    form_class = AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('add_album')
    
    def form_valid(self, form):
        messages.success(self.request, 'Album Successfully Added')
        return super().form_valid(form)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Create'
        return context


class EditAlbumView(UpdateView):
    model = AlbumModel
    form_class = AlbumForm
    pk_url_kwarg = 'id'
    template_name = 'add_album.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Album Successfully Updated')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Edit'
        return context
    


class DeleteAlbumView(DeleteView):
    model = AlbumModel
    template_name = 'delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')

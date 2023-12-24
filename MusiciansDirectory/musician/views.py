from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from musician.forms import MusicianForm, RegisterForm
from musician.models import MusicianModel
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, UpdateView, View
from django.contrib.auth.models import User


class RegisterationView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('register')

    def form_valid(self, form):
        messages.success(self.request, 'Account Successfully Created')
        return super().form_valid(form)
    

class UserLoginView(LoginView):
    template_name='login.html'
    
    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Logged in successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

class AddMusicianCreateView(CreateView):
    model = MusicianModel
    form_class = MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('add_musician')

    def form_valid(self, form):
        messages.success(self.request, 'Musician Successfully Created')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Create Musician'
        return context
    

class EditMusicianView(UpdateView):
    model = MusicianModel
    form_class = MusicianForm
    pk_url_kwarg = 'id'
    template_name ='add_musician.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'Profile Updated Successfully')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Edit Musician'
        return context


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(self.request, 'Logged Out Successfully')
        return redirect('login')


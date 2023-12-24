from django.urls import path
from . import views


urlpatterns = [
    
    path('register/', views.RegisterationView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('add/', views.AddMusicianCreateView.as_view(), name='add_musician'),
    path('edit/<int:id>', views.EditMusicianView.as_view(), name='edit_musician')
]

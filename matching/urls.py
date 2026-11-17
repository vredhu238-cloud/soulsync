from django.urls import path
from . import views

urlpatterns = [
    path('', views.discover_view, name='discover'),
    path('matches/', views.matches_list_view, name='matches_list'),
    path('chat/<int:match_id>/', views.chat_view, name='chat'),
    path('video-call/<int:match_id>/', views.video_call_view, name='video_call'), # Naya
    path('party-room/', views.party_room_view, name='party_room'), # Naya
]
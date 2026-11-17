from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from accounts.models import User
from .models import Swipe, Match, Message

@login_required
def discover_view(request):
    swiped_users = Swipe.objects.filter(swiper=request.user).values_list('target_id', flat=True)
    profiles = User.objects.exclude(id=request.user.id).exclude(id__in=swiped_users).order_by('?')
    profile = profiles.first()

    if request.method == 'POST':
        action = request.POST.get('action')
        target_id = request.POST.get('target_id')
        
        if action and target_id:
            target_user = User.objects.get(id=target_id)
            Swipe.objects.create(swiper=request.user, target=target_user, direction=action)
            
            if action == 'right':
                reverse_like = Swipe.objects.filter(swiper=target_user, target=request.user, direction='right').exists()
                if reverse_like:
                    Match.objects.get_or_create(
                        user_a=min(request.user, target_user, key=lambda u: u.id),
                        user_b=max(request.user, target_user, key=lambda u: u.id)
                    )
            return redirect('discover')

    return render(request, 'matching/discover.html', {'profile': profile})

@login_required
def matches_list_view(request):
    matches = Match.objects.filter(Q(user_a=request.user) | Q(user_b=request.user)).order_by('-created_at')
    return render(request, 'matching/matches_list.html', {'matches': matches})

@login_required
def chat_view(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    if request.user != match.user_a and request.user != match.user_b:
        return redirect('matches_list')
    
    other_user = match.user_b if match.user_a == request.user else match.user_a
    messages = match.messages.all().order_by('created_at')

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(match=match, sender=request.user, content=content)
            return redirect('chat', match_id=match.id)

    return render(request, 'matching/chat.html', {'match': match, 'other_user': other_user, 'messages': messages})

# NAYA: 1-on-1 Video Call View
@login_required
def video_call_view(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    # Ek unique room name banayein taaki sirf wahi 2 log jud sakein
    room_name = f"SoulSync_Match_{match.id}"
    return render(request, 'matching/video_call.html', {'room_name': room_name, 'title': 'Private Video Date'})

# NAYA: Public Party Room View
@login_required
def party_room_view(request):
    # Ye ek public room hai jahan sab log aa sakte hain
    room_name = "SoulSync_Public_Party_Room"
    return render(request, 'matching/video_call.html', {'room_name': room_name, 'title': 'SoulSync Party Room'})
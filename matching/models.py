from django.db import models
from django.conf import settings

class Swipe(models.Model):
    swiper = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='swipes_made', on_delete=models.CASCADE)
    target = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='swipes_received', on_delete=models.CASCADE)
    direction = models.CharField(max_length=5, choices=[("right", "Like"), ("left", "Pass")])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("swiper", "target")

class Match(models.Model):
    user_a = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='matches_as_a', on_delete=models.CASCADE)
    user_b = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='matches_as_b', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user_a", "user_b")

class Message(models.Model):
    match = models.ForeignKey(Match, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'bio', 'gender', 'interests']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
            'interests': forms.TextInput(attrs={'placeholder': 'e.g. music, travel, coding'}),
        }
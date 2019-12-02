from django import forms
from .models import Profile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
        )


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = (
            'city',
            'phone'
        )

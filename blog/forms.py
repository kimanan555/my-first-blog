from django import forms
from django.db import transaction
from .models import Post, dt, dt2

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class dtForm(forms.ModelForm):
    """pH=forms.IntegerField()
    temp=forms.IntegerField()
    Ec=forms.IntegerField()
    Water=forms.IntegerField()"""
    class Meta:
        model = dt
        fields = (
            'pH',
            'temp',
            'Ec',
            'Water',
        )
class dtForm2(forms.ModelForm):
    """pH=forms.IntegerField()
    temp=forms.IntegerField()
    Ec=forms.IntegerField()
    Water=forms.IntegerField()"""
    class Meta:
        model = dt2
        fields = (
            'pH',
            'temp',
            'Ec',
            'Water',
        )
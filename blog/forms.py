from django import forms
from django.db import transaction
from .models import Post, dt, dt2

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class dtForm(forms.ModelForm):
    """pH=forms.DecimalField()
    temp=forms.DecimalField()
    Ec=forms.DecimalField()
    Water=forms.DecimalField()"""
    class Meta:
        model = dt
        fields = (
            'pH',
            'temp',
            'Ec',
            'Water',
        )
class dtForm2(forms.ModelForm):
    """pH=forms.DecimalField()
    temp=forms.DecimalField()
    Ec=forms.DecimalField()
    Water=forms.DecimalField()"""
    # pH=forms.DecimalField(..., max_digits=1, decimal_places=2)
    # pH=forms.IntegerField(required=True)
    # temp=forms.IntegerField(required=False)
    # Ec=forms.IntegerField(required=False)
    # Water=forms.IntegerField(required=False)
    class Meta:
        model = dt2
        fields = (
            'pH',
            'temp',
            'Ec',
            'Water',
        )
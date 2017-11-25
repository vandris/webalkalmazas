#-*- coding: utf-8 -*-
from django import forms
from .models import Adds

class AddForm(forms.Form):
   picture = forms.ImageField()

class AddsForm(forms.ModelForm):
    class Meta:
        model = Adds
        fields = ('owner', 'country','address','squaremeter','price','type','wall','heating','state','rooms','parking','year','furnitured','lift','view','description','picture' )
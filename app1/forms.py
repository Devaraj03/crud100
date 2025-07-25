from .models import book
from django import forms

class bookform(forms.ModelForm):
    class Meta:
        model=book
        fields=['name','author']    
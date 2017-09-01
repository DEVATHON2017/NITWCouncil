from django import forms

from .models import GrievancePost

class GrievanceForm(forms.ModelForm):

    class Meta:
        model = GrievancePost
        fields = ('heading','department','complaint',)
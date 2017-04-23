from django import forms
from .models import Feedback, Zone, District, Politicaldiv, Post

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = {'whatyouweredoing','whathappened'}

class WpZoneForm(forms.ModelForm):
    class Meta:
        model = Zone
        fields = {'name'}

class WpDistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields = {'name','zone'}

class WpPoliticaldivForm(forms.ModelForm):
    class Meta:
        model = Politicaldiv
        fields = {'zone','district','name','group'}

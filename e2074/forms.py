from django import forms
from .models import Feedback, Zone, District, Vdc, Municipality

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

class WpVdcForm(forms.ModelForm):
    class Meta:
        model = Vdc
        fields = {'zone','district','name','ward'}

class WpMunicipalityForm(forms.ModelForm):
    class Meta:
        model = Municipality
        fields = {'zone','district','name','ward'}

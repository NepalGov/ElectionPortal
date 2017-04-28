from django import forms
from .models import Feedback, Zone, District, Politicaldiv, Post, Candidate

from markdownx.fields import MarkdownxFormField

class FeedbackForm(forms.ModelForm):
    field_order = ['whatyouweredoing','whathappened']
    class Meta:
        model = Feedback
        fields = {'whatyouweredoing','whathappened'}

class WpZoneForm(forms.ModelForm):
    class Meta:
        model = Zone
        fields = {'name'}

class WpDistrictForm(forms.ModelForm):
    field_order = ['name','zone','vdc','municipality','submetropolitan','metropolitan','population','voters']
    class Meta:
        model = District
        fields = {'name','zone','vdc','municipality','submetropolitan','metropolitan','population','voters'}

class WpPoliticaldivForm(forms.ModelForm):
    field_order = ['name','zone','district','group']
    class Meta:
        model = Politicaldiv
        fields = {'zone','district','name','group'}

class WpCandidateForm(forms.ModelForm):
    about = MarkdownxFormField()
    field_order = ['name','party','zone','district','politicaldiv','gender','votes','status','age','criminalcase','photo','about']
    class Meta:
        model = Candidate
        fields = {'name','party','zone','district','politicaldiv','gender','votes','status','age','criminalcase','photo','about'}

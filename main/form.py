from django import forms
from main.models import *
from main.widgets import Redactor

class AddCase(forms.ModelForm):
    class Meta:
        model = Case
        widgets = {
            'image': forms.TextInput(attrs={'class':'image'}),
            'requirements': forms.TextInput(attrs={'class':'requirements'}),
            'description': forms.TextInput(attrs={'class':'description'}),
            'name': forms.TextInput(attrs={'class':'name'}),
            'step': Redactor(attrs={'cols': 85, 'rows': 20})
        }

class AddSuite(forms.ModelForm):
    cases=forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=Case.objects.all(), required=False)
    class Meta:
        model = Suite
        widgets = {
            'cases': CheckboxSelectMultiple(attrs={'class':'cases'}),
            'name': forms.TextInput(attrs={'class':'name'}),
            'features': forms.Textarea(attrs={'class':'features'})
        }


class EditSuite(forms.ModelForm):
    cases=forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=Case.objects.all(), required=False)
    class Meta:
        model = Suite
        widgets = {
            'cases': CheckboxSelectMultiple(attrs={'class':'cases'}),
            'name': forms.TextInput(attrs={'class':'name'}),
            'features': forms.Textarea(attrs={'class':'features'})
        }

class AddResult(forms.ModelForm):
    class Meta:
        model = Result

class AddRun(forms.ModelForm):
    class Meta:
        model = Run


class AbilitiesForm(forms.ModelForm):
    class Meta:
        model = Abilities

class AddUser(forms.ModelForm):
    abilities   =   forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=Abilities.objects.all())
    class Meta:
        model   =   UserProfile


class EditCase (forms.ModelForm):
    class Meta:
        model = Case
        widgets = {
            'image': forms.TextInput(attrs={'class':'image'}),
            'requirements': forms.TextInput(attrs={'class':'requirements'}),
            'description': forms.TextInput(attrs={'class':'description'}),
            'name': forms.TextInput(attrs={'class':'name'}),
            'step': Redactor(attrs={'cols': 80, 'rows': 20}),
        }

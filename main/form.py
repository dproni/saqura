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
    cases=forms.ModelMultipleChoiceField(queryset=Case.objects.all(), required=False)
    class Meta:
        model = Suite
        widgets = {
            'cases': CheckboxSelectMultiple(attrs={'class':'cases'}),
            'name': forms.TextInput(attrs={'class':'name'}),
            'features': forms.Textarea(attrs={'class':'features'})
        }


class EditSuite(forms.ModelForm):
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

#class EditCase (forms.Form):
#    Priority = (
#        (0, 'Blocker'),
#        (1, 'High'),
#        (2, 'Medium'),
#        (3, 'Low'),
#    )
#
#    name = forms.CharField()
#    description = forms.CharField(widget=forms.Textarea)
#    priority = forms.ChoiceField(choices=Priority)
#    image = forms.URLField()
#    requirements = forms.URLField()
#    step = forms.CharField(widget=forms.Textarea)
#
#    class Meta:
#        model = Case
#        widgets = {
#            'step': Redactor(attrs={'cols': 80, 'rows': 20}),
#        }

class EditCase (forms.ModelForm):
    class Meta:
        model = Case
        widgets = {
            'step': Redactor(attrs={'cols': 80, 'rows': 20}),
        }

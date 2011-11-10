from django import forms
from main.models import *
from main.widgets import Redactor

class AddCase(forms.ModelForm):
    class Meta:
        model = Case

class AddSuiteForm(forms.ModelForm):
    cases=forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=Case.objects.all(), required=False)
    class Meta:
        model = Suite

class EditSuiteForm(forms.ModelForm):
    cases=forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=Case.objects.all(), required=False)
    class Meta:
        model = Suite

class EditCaseForm (forms.ModelForm):
    class Meta:
        model = Case


class SuiteEditForm (forms.Form):
    suiteName = forms.CharField(max_length=100)

class AddSuiteNameForm(forms.Form):
    suiteName = forms.CharField(max_length=100)


class TestCase(forms.Form):
    caseName   = forms.CharField(max_length=10)
    caseDescription = forms.CharField(max_length=100)
    caseText = forms.CharField(max_length=100)

from django import forms
from main.models import *
from main.widgets import Redactor

class AddCase(forms.ModelForm):
    caseType=forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=CaseType.objects.all(), required=False)
    class Meta:
        model = Case

class AddSuite(forms.ModelForm):
    cases=forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=Case.objects.all(), required=False)
    class Meta:
        model = Suite

class AddCaseType(forms.ModelForm):
    class Meta:
        model = CaseType

class EditSuite(forms.ModelForm):
    cases=forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=Case.objects.all(), required=False)
    class Meta:
        model = Suite

class AddResult(forms.ModelForm):
    class Meta:
        model = Result

class AddBuild(forms.ModelForm):
    class Meta:
        model = Build

class AddTestRun(forms.ModelForm):
#    suites=forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=Suite.objects.all(), required=False)
    class Meta:
        model = TestRun


class AbilitiesForm(forms.ModelForm):
    class Meta:
        model = Abilities

class AddUser(forms.ModelForm):
    abilities   =   forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=Abilities.objects.all())
    class Meta:
        model   =   UserProfile


class EditCase (forms.ModelForm):
    caseType=forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=CaseType.objects.all(), required=False)
    class Meta:
        model = Case
#        widgets = {
#            'image': forms.TextInput(attrs={'class':'image'}),
#            'requirements': forms.TextInput(attrs={'class':'requirements'}),
#            'description': forms.TextInput(attrs={'class':'description'}),
#            'name': forms.TextInput(attrs={'class':'name'}),
#            'step': Redactor(attrs={'cols': 80, 'rows': 20}),
#        }


class SuiteEdit(forms.Form):
    suiteName = forms.CharField(max_length=100)



# TEST


class ContactForm(forms.Form):
    suiteName = forms.CharField(max_length=100)


class TestCase(forms.Form):
    caseName   = forms.CharField(max_length=10)
    caseDescription = forms.CharField(max_length=100)
    caseText = forms.CharField(max_length=100)
from django.shortcuts import render_to_response, get_list_or_404, HttpResponse, HttpResponseRedirect
from main.models import *
from main.form import *



def test(request):
    testValue = ""
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            subject = form.cleaned_data['subject']
            testValue = subject
            return render_to_response('test.html', {
        'form'      : form,
        'testValue' : testValue,
    })
    else:
        form = ContactForm() # An unbound form

    return render_to_response('test.html', {
        'form'      : form,
        'testValue' : testValue,
    })
from django.shortcuts import render_to_response, get_list_or_404, HttpResponse, HttpResponseRedirect
from main.models import *
from main.form import *
from django.views.decorators.csrf import csrf_exempt
try:
    import json
except ImportError:
    import simplejson

@csrf_exempt
def test(request):
    if request.is_ajax():
        print "dsdadas"
        caseID = request.POST.get('caseID','')
        caseTitle = request.POST.get('caseName','')
        return render_to_response('addcase.html', {
            "caseID": caseID,
            "caseTitle": caseTitle,
        })
    return render_to_response('test.html', {})

@csrf_exempt
def caseWorker(request):
    if request.is_ajax():
#        case_name = request.POST.get('caseName','')
#        case_name = "ddddd"
#        print case_name
        case = testtestcase()
        case.caseName = request.POST.get('caseName','')
        case.save()
        print "dsdadas"
        return HttpResponse("ddd")
#        caseID = request.POST.get('caseID','')
#        caseTitle = request.POST.get('caseName','')
#        return render_to_response('addcase.html', {
#            "caseID": caseID,
#            "caseTitle": caseTitle,
#        })
    return render_to_response('test.html', {})

@csrf_exempt
def addSuite(request):
    form = AddSuiteNameForm()
    if request.method == 'POST':
        suite = Suite()
        suite.name= request.POST.get('suiteName','')
        suite.save()
        return HttpResponseRedirect('/editsuite/%s' % suite.id)
    return render_to_response('addsuite.html', {
        "form": form
    })


@csrf_exempt
def editSuite (request, suite):
    suite = Suite.objects.get(id = suite)

    form = EditSuiteForm()
    if request.method == 'POST':
        suite.caseName = request.POST.get('caseName', '')
        suite.save()
        return HttpResponseRedirect('/editsuite/%s' % suite.id)

    return render_to_response('editsuite.html', {
    "form": form,
    "suite": suite
    })
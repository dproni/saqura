from django.shortcuts import render_to_response, get_list_or_404, HttpResponse, HttpResponseRedirect
from main.models import *
from main.form import *
from django.views.decorators.csrf import csrf_exempt

try:
    import json
except ImportError:
    import simplejson

@csrf_exempt
def addCase(request):
    case = Case()
    if request.is_ajax():
        case.id = request.POST.get('caseId', '')
        print case.id
        return render_to_response('addcase.html', {
            "case": case,
            })
    return render_to_response('test.html', {})

@csrf_exempt
def caseWorker(request):
    try:
        caseId          = request.POST.get('caseId', '')
        suiteID         = request.POST.get('suiteID', '')
        caseName        = request.POST.get('caseName', '')
        caseDescription = request.POST.get('caseDescription', '')
        caseStep        = request.POST.get('caseStep', '')
    except:
        print "ddddddd"
    request.POST.get('caseStep', '')
    if request.is_ajax():
        caseStep = "dsdsadasdasdasd"
        caseDescription = "sadsdadasda"
        suiteID = 3
        print caseId
        try:
            case = Case.objects.get(id = caseId)
            print caseId
        except:
            case = Case()
        suite = Suite.objects.get(id = suiteID)
        case.name = caseName
        case.description = caseDescription
        case.step = caseStep
        case.suite_id = suite.id
        case.save()
        return HttpResponse(case.name)
    return render_to_response('test.html', {})

@csrf_exempt
def addSuite(request):
    form = AddSuiteNameForm()
    if request.method == 'POST':
        suite = Suite()
        suite.name = request.POST.get('suiteName', '')
        suite.save()
        return HttpResponseRedirect('/editsuite/%s' % suite.id)
    return render_to_response('addsuite.html', {
        "form": form
        })


@csrf_exempt
def editSuite (request, suite):
    suite = Suite.objects.get(id=suite)
    cases = Case.objects.filter(suite=suite)
    form = EditSuiteForm()
    if request.method == 'POST':
        suite.caseName = request.POST.get('caseName', '')
        suite.save()
        return HttpResponseRedirect('/editsuite/%s' % suite.id)

    return render_to_response('editsuite.html', {
        "form": form,
        "suite": suite,
        "cases": cases
        })
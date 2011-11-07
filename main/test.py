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
#        case_name = request.POST.get('caseName','')
#        case_name = "ddddd"
#        print case_name
        print "dsdadas"
#        return HttpResponse(test)
        caseID = request.POST.get('caseID','')
        return render_to_response('addcase.html', {
            "caseID": caseID,
        })
    return render_to_response('test.html', {})
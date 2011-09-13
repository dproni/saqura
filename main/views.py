# Create your views here.
# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response, get_list_or_404, HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from main.models import *
from main.form import *
import datetime

def login_page(request):
    return render_to_response('login.html',{
                                            'host' : request.get_host(),
                                            })
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Правильный пароль и пользователь "активен"
        auth.login(request, user)
        # Перенаправление на "правильную" страницу
        return HttpResponseRedirect('/')
    else:
        # Отображение страницы с ошибкой
        return HttpResponse("/invalid/")

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def addCase(request):
    c = {}
    c.update(csrf(request))
    user = auth.get_user(request)
    if request.method == 'POST': 
        form = AddCase(data = request.POST) 
        if form.is_valid():
            form.save()
    else:
        form = AddCase() 

    return render_to_response('addcase.html', {
                                                    'form': form,
                                                    'js': c.items(),
                                                    'host' : request.get_host(),
                                                    'user' : user
                                                })
def addSuite(request):
    c = {}
    c.update(csrf(request))
    user = auth.get_user(request)
    if request.method == 'POST': # If the form has been submitted...
        form = AddSuite(data = request.POST) 
        if form.is_valid():
            form.save()
    else:
        form = AddSuite() 

    return render_to_response('addsuite.html', {
                                                    'form': form,
                                                    'js': c.items(),
                                                    'host' : request.get_host(),
                                                    'user' : user
                                                })
def addResult(request):
    c = {}
    c.update(csrf(request))
    user = auth.get_user(request)
    if request.method == 'POST': # If the form has been submitted...
        form = AddResult(data = request.POST) 
        if form.is_valid():
            form.save()
    else:
        form = AddResult() 

    return render_to_response('addresult.html', {
                                                    'form': form,
                                                    'js': c.items(),
                                                    'host' : request.get_host(),
                                                    'user' : user
                                                })

def addRun(request):
    c = {}
    c.update(csrf(request))
    user = auth.get_user(request)
    if request.method == 'POST': # If the form has been submitted...
        form = AddResult(data = request.POST) 
        if form.is_valid():
            form.save()
    else:
        form = AddResult() 

    return render_to_response('addrun.html', {
                                                    'form': form,
                                                    'js': c.items(),
                                                    'host' : request.get_host(),
                                                    'user' : user
                                                })


def index (request):
    title = 'Welcome to main application'
    cases = Case.objects.order_by('id')
    suites = Suite.objects.order_by('id')
    user = auth.get_user(request)
    return render_to_response('index.html',{
                                            'host' : request.get_host(), 
                                            'cases' : cases,
                                            'suites': suites,
                                            'user': user
                                            })

def create (request):
    title = 'Welcome to main application'
    return render_to_response('create.html',{
                                            'title': title,
                                            })

#@login_required
def info (request):
    title = 'Welcome to main application'
    cases = Case.objects.order_by('id')
    suites = Suite.objects.order_by('id')
    user = auth.get_user(request)
    return render_to_response('info.html',{
                                            'host' : request.get_host(),
                                            'cases' : cases,
                                            'suites': suites,
                                            'user': user
                                            })

def main (request, suite_id, case_id, job_id): #the main executeble workflow
    title = 'Welcome to main application'
    suites = Suite.objects.order_by('id')
    suite = Suite.objects.get(id=suite_id)
#    cases = Case.objects.order_by('id')
    cases = suite.cases

#    job = Jobs(is_active=True, user=request.user)
#    job.save()
    case = Case.objects.get(id=case_id)
    user = auth.get_user(request)
    return render_to_response('main.html', {
                                             'suite' : suite, 
                                             'suites': suites,
                                             'job_id': job_id,
                                             'case' : case,
                                             'cases': cases,
                                             'title' : title,
                                             'host' : request.get_host(),
                                             'user': user
                                             })

def main_begin (request, suite_id): #show the test cases and show activity chooser
    title = 'Welcome to main application'
    suites = Suite.objects.order_by('id')
    suite = Suite.objects.get(id=suite_id)
    #TODO remove duplicated job
    job = Jobs(user=request.user, is_active=True)
    job.save()
    cases = suite.cases
    user = auth.get_user(request)
    return render_to_response('main.html', {
                                             'suite' : suite,
                                             'suites': suites,
                                             'cases': cases,
                                             'title' : title,
                                             })

def main_show_suites (request): #display all suites to execute
    title = 'Welcome to main application'
    suites = Suite.objects.order_by('id')
    user = auth.get_user(request)
    return render_to_response('main_show_suites.html', {
                                             'suites': suites,
                                             'host' : request.get_host(),
                                             'user': user,
                                             'title': title
                                             })

def show_suite (request, suite_id):
    item = Suite.objects.get(id=suite_id)
    return render_to_response('moresuite.html', {
                                             'item' : item
                                             })
def show_case(request, case_id):
    item = Case.objects.get(id=case_id)
    return render_to_response('morecase.html', {
                                             'item' : item
                                             })

def execute (request, pass_id, suite_id, case_id):

    suites = Suite.objects.order_by('id')
    suite = Suite.objects.get(id=suite_id)
    cases = Case.objects.order_by('id')
    case = Case.objects.get(id=case_id)
    title = 'Welcome to main application %s' % (suite.name)
    c = {}
    what_result = 0
    c.update(csrf(request))
    user = auth.get_user(request)
    task_id = pass_id
    #pas = Pass.objects.get(id=task_id) #check if the pass with result already exist
    #TODO create lock for current user, if user already se result for case
    #make it via coockies or checking db
    
    if request.method == 'POST':
        if 'pass' in request.POST.keys():
            result = Result(id=None,result='Pass', Pass = Pass.objects.get(id=pass_id), case=case, suite=suite)
            result.save()

#            pass_process(task_id, result.id, user.id)
            what_result = 1

        elif 'failed' in request.POST.keys():
            result = Result(id=None, result='Failed', Pass = Pass.objects.get(id=pass_id), case=case, suite=suite )
            result.save()
#            pass_process(task_id, result.id, user.id)
            what_result = 2

    return render_to_response('main.html', {
                                             'suite' : suite,
                                             'task_id' : task_id,
                                             'pass_id' : pass_id,
                                             'suites': suites,
                                             'case' : case,
                                             'cases': cases,
                                             'what_result': what_result,
                                             'check': user.id,
                                             'user'     : user,
                                             'host' : request.get_host()
                                             })

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def search(request):
    if 'q' in request.GET:
        title = 'Welcome to main application'
        cases = Case.objects.filter(id=request.GET['q'])
        return render_to_response('main.html', {
                                             'title' : title,
                                             'cases': cases,
                                             'host' : request.get_host()
                                             })
    else:
        message = 'You sucks'
    return HttpResponse(message)

def editCase (request, case_id):
    case = Case.objects.get(id=case_id)
    name = case.name
    description = case.description
    priority = case.priority
    image = case.image
    requirements = case.requirements
    step = case.step
    c = {}
    c.update(csrf(request))
    if request.method == 'POST': # If the form has been submitted...
        form = EditCase(data = request.POST) 
        if form.is_valid():
            case = Case(
                        id          = case_id,
                        modified    = datetime.datetime.today(),
                        name        = form.cleaned_data['name'],
                        description = form.cleaned_data['description'],
                        priority    = form.cleaned_data['priority'],
                        image       = form.cleaned_data['image'],
                        requirements= form.cleaned_data['requirements'],
                        step        = form.cleaned_data['step']
                        )
            case.save()
    else:
        form = EditCase(initial={'name': name,
                                 'description': description,
                                 'priority': priority,
                                 'image': image,
                                 'requirements': requirements,
                                 'step': step,}) 

    return render_to_response('editcase.html', {
        'form': form,
        'case': case,
    })

def editSuite (request, suite_id):
    suite = Suite.objects.get(id=suite_id)
    name = suite.name
    features = suite.features
    cases = suite.cases
    c = {}
    c.update(csrf(request))
    if request.method == 'POST': # If the form has been submitted...
        form = EditSuite(data = request.POST) 
        if form.is_valid():
            suite = Suite(
                        id        = suite_id,
                        name      = form.cleaned_data['name'],
                        features  = form.cleaned_data['features'],
                        cases     = request.POST.getlist('cases')
                        )
            suite.save()
#            form.save()
    else:
#        a = Case.objects.get(suite = suite_id)
#        initialValues =  {
#                            'name'      : name,
#                            'features'  : features,
#                            'cases'     : a
#                        }
#        form = EditSuite(initialValues)
        form = EditSuite(instance = suite)



    return render_to_response('editsuite.html', {
        'form': form,
        'suite': suite,
#        'cases' : a
    })
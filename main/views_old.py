# Create your views here.
# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response, get_list_or_404, HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib import auth
from django.http import Http404
from django.contrib.auth.decorators import login_required
from main.models import *
from main.form import *
from main.test import *
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
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
#            form.save()
    else:
        form = AddCase() 

    return render_to_response('addcase.html', {
                                                    'form': form,
                                                    'js': c.items(),
                                                    'host' : request.get_host(),
                                                    'user' : user
                                                })

def addCaseType(request):
    c = {}
    c.update(csrf(request))
    user = auth.get_user(request)
    if request.method == 'POST':
        form = AddCaseType(data = request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
#            form.save()
    else:
        form = AddCaseType()

    return render_to_response('addcasetype.html', {
                                                    'form': form,
                                                    'js': c.items(),
                                                    'host' : request.get_host(),
                                                    'user' : user
                                                })

def xaddSuite(request):
    c = {}
    c.update(csrf(request))
    user = auth.get_user(request)
    if request.method == 'POST':
        form = AddSuite(data = request.POST) 
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            cases = request.POST.getlist('cases')
            obj.save()
            form.save_m2m()
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
    if request.method == 'POST':
        form = AddResult(data = request.POST) 
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
#            form.save()
    else:
        form = AddResult() 

    return render_to_response('addresult.html', {
                                                    'form': form,
                                                    'js': c.items(),
                                                    'host' : request.get_host(),
                                                    'user' : user
                                                })
def addUser(request):
    c = {}
    c.update(csrf(request))
    user = auth.get_user(request)
    if request.method == 'POST':
        form = AddUser(data = request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
#            form.save()
    else:
        form = AddUser()

    return render_to_response('adduser.html', {
                                                    'form': form,
                                                    'js': c.items(),
                                                    'host' : request.get_host(),
                                                    'user' : user
                                                })


def addRun(request):
    c = {}
    c.update(csrf(request))
    user = auth.get_user(request)
    if request.method == 'POST':
        form = AddTestRun(data = request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
#            form.save()
    else:
        form = AddTestRun()

    return render_to_response('addrun.html', {
                                                    'form': form,
                                                    'js': c.items(),
                                                    'host' : request.get_host(),
                                                    'user' : user
                                                })

def addBuild(request):
    c = {}
    c.update(csrf(request))
    user = auth.get_user(request)
    if request.method == 'POST':
        form = AddBuild(data = request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
#            form.save()
    else:
        form = AddBuild()

    return render_to_response('addbuild.html', {
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

def edit (request):
    title = 'Welcome to main application'
    return render_to_response('edit.html',{
                                            'title': title,
                                            })
#@login_required
def info (request):
    title   = 'Welcome to main application'
    cases   = Case.objects.order_by('id')
    suites  = Suite.objects.order_by('id')
    users   = User.objects.order_by('id')
#    builds  = Build.objects.order_by('build')
#    runs    = TestRun.objects.order_by('id')
#    caseTypes    = CaseType.objects.order_by('id')
    user = auth.get_user(request)
    return render_to_response('info.html',{
                                            'host' : request.get_host(),
                                            'cases' : cases,
#                                            'caseTypes' : caseTypes,
                                            'suites': suites,
                                            'users':users,
#                                            'runs':runs,
#                                            'builds':builds,
                                            'user': user
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


def editAbilities (request):
    abilities = Abilities.objects.all()
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = AbilitiesForm(data = request.POST)
        if form.is_valid():
           pass
    else:
        form = AbilitiesForm(instance = abilities)
        
    return render_to_response('abilities.html', {
        'form': form,
    })

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
    if request.method == 'POST':
#        form = EditCase(data = request.POST)
        form = EditCase(request.POST, instance = case)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            caseType = request.POST.getlist('caseType')
            obj.save()
            form.save_m2m()
#            form.save()
    else:
        form = EditCase(instance = case)

    return render_to_response('editcase.html', {
        'form': form,
        'case': case,
    })

#def editSuite (request, suite_id):
#    try:
#        suite = Suite.objects.get(id=suite_id)
#    except Suite.DoesNotExist:
#        raise Http404
#    c = {}
#    c.update(csrf(request))
#    if request.method == 'POST':
#        form        = EditSuite(request.POST, instance = suite)
#        if form.is_valid():
#            obj             = form.save(commit=False)
#            obj.user        = request.user
#            cases           = request.POST.getlist('cases')
#            obj.save()
#            form.save_m2m()
#
#    else:
#        form        = EditSuite(instance = suite)
#        caseForm    = AddCase()
#    return render_to_response('editsuite.html', {
#        'form'      : form,
#        'suite'     : suite,
##        'cases' : a
#    })
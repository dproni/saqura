# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from django.contrib.auth.models import User
from django.contrib import auth
from django.forms import CheckboxSelectMultiple, Widget
from main.models import *
from main.widgets import Redactor
import datetime

format = "%a %b %d %H:%M:%S %Y"

class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
        models.TextField: {'widget': Redactor(attrs={'cols': 120, 'rows': 25})},
    }
    def save_model(self, request, obj, form, change):
        obj.boss = request.user
        obj.save()

class Case(models.Model):
    Priority = ( 
                        ('Blocker', 'Blocker'),
                        ('High', 'High'),
                        ('Medium', 'Medium'),
                        ('Low', 'Low'),
                )
    name = models.CharField(max_length=200)
    image = models.URLField(blank=True)
    requirements = models.URLField(blank=True)
    priority = models.CharField(max_length=10, choices=Priority)
    description = models.CharField(max_length=200)
    step = models.TextField()
    modified = models.DateTimeField(editable=False)
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.modified = datetime.datetime.today()
        super(Case, self).save(*args, **kwargs)
        
    def __unicode__(self):
        return self.name
        return self.description

class Suite (models.Model):
    name = models.CharField(max_length=200)
    features=models.TextField()
    modified = models.DateTimeField(editable=False, null=True)
    cases = models.ManyToManyField(Case, null=True, blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.modified = datetime.datetime.today()
        super(Suite, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
        return self.description

class Run (models.Model):
    is_active = models.BooleanField()
    modified = models.DateTimeField(editable=False)
    user = models.CharField(max_length=10, null=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.modified = datetime.datetime.today()
        super(Jobs, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

        
class Result (models.Model):
    results = ( 
                        ('Pass', 'Pass'),
                        ('N/A', 'N/A'),
                        ('Failed', 'Failed'),
                        ('Postponed', 'Postponed'),
                        ('Issue', 'Issue1'),
            )
    result = models.CharField(max_length=10, choices=results, null=True)
    case = models.ForeignKey(Case, null=True)
    suite = models.ForeignKey(Suite, null=True)
    job = models.ForeignKey(Jobs, null=True)
    modified = models.DateTimeField(editable=False)
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.modified = datetime.datetime.today()
        super(Result, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name



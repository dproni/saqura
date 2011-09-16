# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from django.contrib.auth.models import User
from django.contrib import auth
from django.forms import CheckboxSelectMultiple, Widget
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

class Abilities (models.Model):
    is_active   = models.BooleanField()
    modified    = models.DateTimeField(editable=False)
    create_cases    = models.BooleanField()
    create_suites   = models.BooleanField()
    edit_cases      = models.BooleanField()
    edit_suites     = models.BooleanField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.modified = datetime.datetime.today()
        super(Run, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.user


class UserProfile (models.Model):
    is_active   = models.BooleanField()
    modified    = models.DateTimeField(editable=False)
    user        = models.OneToOneField(User)
    abilities   = models.ManyToManyField(Abilities, null=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.modified = datetime.datetime.today()
        super(Run, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.user

    def __str__(self):
          return "%s's profile" % self.user  
    
class Case(models.Model):
    Priority = ( 
                        ('Blocker', 'Blocker'),
                        ('High', 'High'),
                        ('Medium', 'Medium'),
                        ('Low', 'Low'),
                )
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=200)
    image       = models.URLField(blank=True)
    requirements = models.URLField(blank=True)
    priority    = models.CharField(max_length=10, choices=Priority)
    description = models.CharField(max_length=200)
    step        = models.TextField()
    modified    = models.DateTimeField(editable=False)
    user        = models.ForeignKey(User, editable=False)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.modified = datetime.datetime.today()
        super(Case, self).save(*args, **kwargs)
    def __unicode__(self):
        return self.name
        return self.description

class Suite (models.Model):
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=200)
    features    = models.TextField()
    modified    = models.DateTimeField(editable=False, null=True)
    cases       = models.ManyToManyField(Case, null=True)
    user        = models.ForeignKey(User, editable=False)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.modified = datetime.datetime.today()
        super(Suite, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
        return self.description

class Run (models.Model):
    is_active   = models.BooleanField()
    modified    = models.DateTimeField(editable=False)
    user        = models.ForeignKey(User, null=True)
    cases       = models.ManyToManyField(Case, null=True)
    suites      = models.ManyToManyField(Suite, null=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.modified = datetime.datetime.today()
        super(Run, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.user
        
class Result (models.Model):
    results = ( 
                        ('Pass', 'Pass'),
                        ('N/A', 'N/A'),
                        ('Failed', 'Failed'),
                        ('Postponed', 'Postponed'),
                        ('Issue', 'Issue1'),
            )
    result      = models.CharField(max_length=10, choices=results, null=True)
    case        = models.ForeignKey(Case, null=True)
    suite       = models.ForeignKey(Suite, null=True)
    run         = models.ForeignKey(Run, null=True)
    modified    = models.DateTimeField(editable=False)
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.modified = datetime.datetime.today()
        super(Result, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name



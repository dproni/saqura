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

class Case (models.Model):
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200)
    step        = models.TextField()
    modified    = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.modified = datetime.datetime.today()
        super(Case, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return self.name
        return self.description

class Suite (models.Model):
    id          = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=200, unique=True)
    features    = models.TextField()
    modified    = models.DateTimeField(editable=False, null=True)
    cases       = models.ManyToManyField(Case, null=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.modified = datetime.datetime.today()
        super(Suite, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
        return self.description

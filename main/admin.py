from django.contrib import admin
from main.models import *


admin.site.register(Case, MyModelAdmin)
admin.site.register(Suite, MyModelAdmin)
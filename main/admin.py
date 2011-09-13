from django.contrib import admin
from main.models import *


admin.site.register(Case, MyModelAdmin)
admin.site.register(Suite, MyModelAdmin)
admin.site.register(Result, MyModelAdmin)
admin.site.register(Run, MyModelAdmin)
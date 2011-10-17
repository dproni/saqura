from django.conf.urls.defaults import *
from main.views import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       (r'^login_in/$',  'main.views.login_page'),
                       (r'^login/$',  'main.views.login'),
                       (r'^logout/$', 'main.views.logout'),
                       (r'^create/', 'main.views.create'),
                       (r'^meta/', 'main.views.display_meta'),
                       (r'^search/', 'main.views.search'),
                       (r'^$', 'main.views.info'), #TBD set to info, not index
                       (r'^pass/', 'main.views.execute'),
                       (r'^editcase/(\d{1,8})/', 'main.views.editCase'),
                       (r'^editsuite/(\d{1,8})/', 'main.views.editSuite'),
                       (r'^info/', 'main.views.info'),
                       (r'^case/(\d{1,8})/', 'main.views.show_case'),
                       (r'^suite/(\d{1,8})/', 'main.views.show_suite'),
                       (r'^edit/', 'main.views.edit'),
                       (r'^addcase/', 'main.views.addCase'),
                       (r'^addcasetype/', 'main.views.addCaseType'),
                       (r'^addsuite/', 'main.views.addSuite'),
                       (r'^addresult/', 'main.views.addResult'),
                       (r'^adduser/', 'main.views.addUser'),
                       (r'^abilities/', 'main.views.editAbilities'),
                       (r'^addrun/', 'main.views.addRun'),
                       (r'^addbuild/', 'main.views.addBuild'),
                       (r'^admin/', include(admin.site.urls)),
                       (r'^test/', 'main.views.test'),
                       (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
                       )

from django.conf.urls.defaults import *
from main.views import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()


#from django.conf.urls.defaults import *

urlpatterns = patterns('',
                       (r'^tinymce/', include('tinymce.urls')),
                       #(r'^result/', 'QA.main.views.result'),
                       (r'^login_in/$',  'main.views.login_page'),
                       (r'^login/$',  'main.views.login'),
                       (r'^logout/$', 'main.views.logout'),
                       (r'^create/', 'main.views.create'),
                       (r'^meta/', 'main.views.display_meta'),
                       (r'^search/', 'main.views.search'),
                       (r'^main/(\d{1,8})/(\d{1,8})/(\d{1,8})', 'main.views.main'),
                       (r'^main/(\d{1,8})/', 'main.views.main_begin'),
                       (r'^main/', 'main.views.main_show_suites'),
                       (r'^grappelli/', include('grappelli.urls')),
                       (r'^$', 'main.views.index'),
                       (r'^pass/(\d{1,8})/suite/(\d{1,8})/case/(\d{1,8})/', 'main.views.execute'),
                       (r'^editcase/(\d{1,8})/', 'main.views.edit_case'),
                       (r'^editsuite/(\d{1,8})/', 'main.views.edit_suite'),
                       (r'^info/', 'main.views.info'),
                       (r'^case/(\d{1,8})/', 'main.views.show_case'),
                       (r'^suite/(\d{1,8})/', 'main.views.show_suite'),
                       (r'^edit/', 'main.views.edit'),
                       (r'^addcase/', 'main.views.addCase'),
                       (r'^addsuite/', 'main.views.addSuite'),
                       (r'^addresult/', 'main.views.addResult'),
                       (r'^addrun/', 'main.views.addRun'),
                       (r'^admin/', include(admin.site.urls)),
                       (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
                       )

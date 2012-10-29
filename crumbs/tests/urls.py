from __future__ import unicode_literals

from django.http import HttpResponseNotFound, HttpResponseServerError
try:
    # Django 1.4+
    from django.conf.urls import include, patterns, url, handler404, handler500
except ImportError: # pragma: no cover
    # Django 1.3
    from django.conf.urls.defaults import include, patterns, url, handler404, handler500

def view(request):
    pass

urlpatterns = patterns('',
    url(r'^list_view/$', view, name='list_view'),
    url(r'^detail_view/(?P<pk>\d+)/$', view, name='detail_view'),
)

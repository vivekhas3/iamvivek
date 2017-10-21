from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView

from views import Home,download
admin.autodiscover()
import settings
urlpatterns = patterns('',
    # Examples:
    url(r'^$', Home.as_view(), name='home'),
    url(r'^download/?$', download, name='download'),
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),

    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve',  # NOQA
    #    {'document_root': settings.MEDIA_ROOT, 'show_indexes': True})
)
if not settings.ON_OPENSHIFT:
    urlpatterns += patterns('', url(r'^static/(?P<path>.*)$', 'django.views.static.serve',  # NOQA
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}))

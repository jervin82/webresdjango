from django.conf.urls import patterns, include, url



from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'webres.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^webresume/$', 'webres.views.webresume'),
    url(r'^hellothere/$', 'webres.views.hello'),
    url(r'^aboutme/$', 'webres.views.aboutme'),
    url(r'^projects/$', 'webres.views.projects'),
)

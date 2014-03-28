#from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.defaults import *
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

handler404 = 'xsxsblog.views.handler404'
handler500 = 'xsxsblog.views.handler500'

urlpatterns = patterns('',
	#url(r'^blog', include('xsxsblog.blog.urls')),
	url('^hello','views.hello'),
	url('^$','views.home'),
	url('^archive/$','views.archive'),
	url('^project/$','views.project'),
	url('^about/$','views.about'),
	url('^tag/(?P<name>.+/$)','views.tag'),
	url('^post/(?P<pid>\d+/)','views.post'),
    # Examples:
    # url(r'^$', 'xsxsblog.views.home', name='home'),
    # url(r'^xsxsblog/', include('xsxsblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),

	# add markdown
	url(r'^markdown/',include('django_markdown.urls')),
)

urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)


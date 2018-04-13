from django.conf.urls import url, include
from django.conf import settings
from django.views.static import serve

from . import views

urlpatterns = [
    url(r'^$', views.about, name='about'),
    url(r'^publications$', views.publications, name='publications'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

# serving media files only on debug mode
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT
        }),
    ]

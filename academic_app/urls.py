from django.conf.urls import url, include
from django.conf import settings
from django.views.static import serve

from . import views

urlpatterns = [
    url(r'^$', views.publications, name='publications'),
    url(r'^about$', views.about, name='about'),
    url(r'^conference$', views.colloques, name='conferences'),
    url(r'^expertise$', views.expertises, name='expertises'),
    url(r'^teaching$', views.enseignements, name='teaching'),
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

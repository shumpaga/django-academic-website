from django.conf.urls import url, include
from django.conf import settings
from django.views.static import serve

from . import views

urlpatterns = [
    url(r'^$', views.publications, name='publications'),
    url(r'^about$', views.about, name='about'),
    url(r'^colloques$', views.colloques, name='colloques'),
    url(r'^expertises$', views.expertises, name='expertises'),
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

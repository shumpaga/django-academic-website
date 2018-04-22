from django.conf.urls import url, include
from django.conf import settings
from django.views.static import serve

from . import views

urlpatterns = [
    url(r'^$', views.publications, name='publications'),
]

# serving media files only on debug mode
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT
        }),
    ]

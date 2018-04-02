from django.conf.urls import url, include
from django.conf import settings
from django.views.static import serve

from . import views

urlpatterns = [
    url(r'^$', views.about, name='about'),
    url(r'^work$', views.work, name='work'),
    url(r'^music$', views.music, name='music'),
    url(r'^thoughts$', views.thoughts, name='thoughts'),
    url(r'^trips$', views.trips, name='trips'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve,
        name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove,
        name='comment_remove'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^comment/', include('django_comments.urls')),
]

# serving media files only on debug mode
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT
        }),
    ]

from django.contrib import admin

from .models import OccupiedPost, Post, StaticText

admin.site.register(OccupiedPost)
admin.site.register(Post)
admin.site.register(StaticText)

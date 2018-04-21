from django.contrib import admin

from .models import OccupiedPost, AcademyTitle, Education, Colloque, Expertise, Post, StaticText

admin.site.register(AcademyTitle)
admin.site.register(Education)
admin.site.register(OccupiedPost)
admin.site.register(Colloque)
admin.site.register(Expertise)
admin.site.register(Post)
admin.site.register(StaticText)

from django.contrib import admin
from .models import Conference, Article, Livre, RapportTechnique, TheseDoctorale, TheseMaster, AutrePublication

admin.site.register(Conference)
admin.site.register(Article)
admin.site.register(Livre)
admin.site.register(RapportTechnique)
admin.site.register(TheseDoctorale)
admin.site.register(TheseMaster)
admin.site.register(AutrePublication)

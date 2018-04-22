# Django
from django.shortcuts import render, get_object_or_404, redirect
# Models
from django.apps import apps
from .models import Conference, Article, Livre, RapportTechnique, TheseDoctorale, TheseMaster, AutrePublication

def publications(request):
    StaticText = apps.get_model('academic_app', 'StaticText')
    if request.LANGUAGE_CODE == 'fr':
        publication = StaticText.objects.get(category = "publication_page").french
    else:
        publication = StaticText.objects.get(category = "publication_page").english

    lat = []
    lat.extend([x.to_latex() for x in Conference.objects.order_by('-annee')])
    lat.extend([x.to_latex() for x in Article.objects.order_by('-annee')])
    lat.extend([x.to_latex() for x in Livre.objects.order_by('-annee')])
    lat.extend([x.to_latex() for x in RapportTechnique.objects.order_by('-annee')])
    lat.extend([x.to_latex() for x in TheseDoctorale.objects.order_by('-annee')])
    lat.extend([x.to_latex() for x in TheseMaster.objects.order_by('-annee')])
    lat.extend([x.to_latex() for x in AutrePublication.objects.order_by('-annee')])

    return render(request, 'academic_app/publications.html',
            { 'publication': publication, 'lat': lat})

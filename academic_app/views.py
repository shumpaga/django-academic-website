# Django
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
# Forms
# Models
from .models import OccupiedPost, Education, Colloque, Expertise, ExpertiseStatistique, Enseignement, AcademyTitle, StaticText
# Python packages
from math import ceil

###############################################################################
#                                 About
###############################################################################
def about(request):
    if request.LANGUAGE_CODE == 'fr':
        about = StaticText.objects.get(category = "about_page").french
    else:
        about = StaticText.objects.get(category = "about_page").english

    post_list = OccupiedPost.objects.order_by('-date')
    edu_list = Education.objects.order_by('-date')
    aca_list = AcademyTitle.objects.order_by('-date')
    language = request.LANGUAGE_CODE

    return render(request, 'academic_app/index.html',
            {'about': about, 'post': post_list, 'edu': edu_list,
                'aca': aca_list, 'language': language})

            ###############################################################################
#                            Publications
###############################################################################
def publications(request):
    if request.LANGUAGE_CODE == 'fr':
        publication = StaticText.objects.get(category = "publication_page").french
    else:
        publication = StaticText.objects.get(category = "publication_page").english
    return render(request, 'academic_app/publications.html',
            { 'publication': publication })


###############################################################################
#                           Colloques-conférences
###############################################################################
def colloques(request):
    coll_list = Colloque.objects.order_by('-date_debut')
    return render(request, 'academic_app/conferences.html',
            { 'coll': coll_list })


###############################################################################
#                              Expertises
###############################################################################
def expertises(request):
    exp_list = Expertise.objects.order_by('-year')
    stats = ExpertiseStatistique.objects.order_by('-year')

    count = 0
    for s in stats:
        count += s.number

    return render(request, 'academic_app/expertises.html',
            { 'exp': exp_list , 'count' : count })


###############################################################################
#                             Enseignements
###############################################################################
def enseignements(request):
    ens_list = Enseignement.objects.order_by('-date_debut')
    if request.LANGUAGE_CODE == 'fr':
        descr = StaticText.objects.get(category = "enseignement_page").french
    else:
        descr = StaticText.objects.get(category = "enseignement_page").english
    return render(request, 'academic_app/teaching.html',
            { 'ens': ens_list, 'descr': descr })

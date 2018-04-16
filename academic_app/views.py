# Django
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
# Forms
from .forms import ContactForm
# Models
from .models import Post, OccupiedPost, Education, Colloque, AcademyTitle, StaticText
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

    return render(request, 'shumpaga_app/index.html',
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
    return render(request, 'shumpaga_app/publications.html',
            { 'publication': publication })


###############################################################################
#                           Colloques-conférences
###############################################################################
def colloques(request):
    coll_list = Colloque.objects.order_by('-date_debut')
    return render(request, 'shumpaga_app/colloques.html',
            { 'coll': coll_list })

###############################################################################
#                           Article categories
###############################################################################
NB_ART_PAGE = 3

def work(request):
    if request.LANGUAGE_CODE == 'fr':
        descr = StaticText.objects.get(category = "work_cat").french
        empty = StaticText.objects.get(category = "empty_cat").french
    else:
        descr = StaticText.objects.get(category = "work_cat").english
        empty = StaticText.objects.get(category = "empty_cat").english

    post_list = Post.objects.filter(category="Work")\
            .filter(published_date__lte=timezone.now())\
            .order_by('-published_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, NB_ART_PAGE)
    language = request.LANGUAGE_CODE

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'shumpaga_app/category.html',
            {'posts': posts, 'descr': descr,
                'cat': 'work', 'empty': empty, 'language': language})


###############################################################################
#                               Contact
###############################################################################
def contact(request):
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():

            subject = request.POST.get('subject', '')
            from_email = request.POST.get('contact_email', '')
            to_email = [settings.EMAIL_HOST_USER]

            contact_name = request.POST.get('contact_name', '')
            content = request.POST.get('content', '')
            message = '{} sent you this message:\n{}'\
                    .format(contact_name, content)

            send_mail(subject=subject, from_email=from_email,
                    recipient_list=to_email, message=message,
                    fail_silently=False)
            messages.success(request, 'Your email has been successfully sent')
            return redirect('contact')
    return render(request, 'shumpaga_app/contact.html', {'form': form_class,})

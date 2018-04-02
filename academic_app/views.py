# Django
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
# Forms
from .forms import ContactForm, CommentForm
# Models
from .models import Comment, Post, StaticText
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
    return render(request, 'shumpaga_app/index.html',
        {'about': about})


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

def music(request):
    if request.LANGUAGE_CODE == 'fr':
        descr = StaticText.objects.get(category = "music_cat").french
        empty = StaticText.objects.get(category = "empty_cat").french
    else:
        descr = StaticText.objects.get(category = "music_cat").english
        empty = StaticText.objects.get(category = "empty_cat").english

    post_list = Post.objects.filter(category="Music")\
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
                'cat': 'music', 'empty': empty, 'language': language})

def thoughts(request):
    if request.LANGUAGE_CODE == 'fr':
        descr = StaticText.objects.get(category = "thoughts_cat").french
        empty = StaticText.objects.get(category = "empty_cat").french
    else:
        descr = StaticText.objects.get(category = "thoughts_cat").english
        empty = StaticText.objects.get(category = "empty_cat").english

    post_list = Post.objects.filter(category="Thoughts")\
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
                'cat': 'thought sketches', 'empty': empty,
                'language': language})

def trips(request):
    if request.LANGUAGE_CODE == 'fr':
        descr = StaticText.objects.get(category = "trips_cat").french
        empty = StaticText.objects.get(category = "empty_cat").french
    else:
        descr = StaticText.objects.get(category = "trips_cat").english
        empty = StaticText.objects.get(category = "empty_cat").english

    post_list = Post.objects.filter(category="Trips")\
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
                'cat': 'trips', 'empty': empty, 'language': language})


###############################################################################
#                               Article
###############################################################################
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            if request.LANGUAGE_CODE == 'fr':
                msg = StaticText.objects.get(category = "comment_post").french
            else:
                msg = StaticText.objects.get(category = "comment_post").english
            messages.info(request, msg)
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()

    nb = len(post.comments.all())
    language = request.LANGUAGE_CODE

    return render(request, 'shumpaga_app/post_detail.html',
            {'post': post, 'nb': nb, 'form': form,
                'language': language})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)


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

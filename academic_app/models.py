from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    WORK = 'Work'
    MUSIC = 'Music'
    THOUGHTS = 'Thoughts'
    TRIPS = 'Trips'
    TAG_CHOICES = (
        (WORK, 'Work'),
        (MUSIC, 'Music'),
        (THOUGHTS, 'Thoughts'),
        (TRIPS, 'Trips'),
    )

    author = models.ForeignKey('auth.User')
    category = models.CharField(max_length=8, choices=TAG_CHOICES, default=WORK)
    title_en = models.CharField(max_length=200)
    title_fr = models.CharField(max_length=200, blank=True)
    youtube_url = models.CharField(max_length=200, default='', blank=True)
    display_it = models.BooleanField(default=False)
    text_en = RichTextUploadingField()
    text_fr = RichTextUploadingField(blank=True)
    abstract = models.CharField(max_length=300)
    abstract_fr = models.CharField(max_length=300, blank=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title_en


class OccupiedPost(models.Model):
    institution = models.CharField(max_length=200)
    description_en = RichTextUploadingField()
    description_fr = RichTextUploadingField()
    date = models.DateField()


    def __str__(self):
        return self.description_fr


class AcademyTitle(models.Model):
    titre_en = models.CharField(max_length=200)
    titre_fr = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.titre_fr


class Education(models.Model):
    diplome_en = models.CharField(max_length=200)
    diplome_fr = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.diplome_fr


class Colloque(models.Model):
    date_debut = models.DateField()
    date_fin = models.DateField()
    lieu = models.CharField(max_length=200)
    description_en = RichTextUploadingField()
    description_fr = RichTextUploadingField()

    def __str__(self):
        return self.description_fr


class StaticText(models.Model):
    TAG_CHOICES = (
        ('about_page', 'about_page'),
        ('publication_page', 'publication_page')
    )
    category = models.CharField(max_length=16, choices=TAG_CHOICES, default='about_page')
    english = RichTextField()
    french = RichTextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.category

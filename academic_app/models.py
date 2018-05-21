from django.db import models
from django.utils import timezone
from django.utils.html import strip_tags
from django.utils.encoding import smart_text
from ckeditor.fields import RichTextField
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

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
    text_en = RichTextField()
    text_fr = RichTextField(blank=True)
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
    description_en = RichTextField()
    description_fr = RichTextField()
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
    description_en = RichTextField()
    description_fr = RichTextField()

    def __str__(self):
        return self.description_fr


class ExpertiseStatistique(models.Model):
    year = models.PositiveIntegerField(
            validators=[
                MinValueValidator(1900),
                MaxValueValidator(datetime.datetime.now().year)],
            help_text="Utilisez le format suivant: YYYY")
    number = models.PositiveIntegerField(help_text="Nombre d'expertises "
            "effectuées l'année considérée.")

    def __str__(self):
        return self.year

    def save(self, *args, **kwargs):
        exp_list = ExpertiseStatistique.objects.order_by('-year')

        # Fill years and count with what is needed
        years = []
        count = []
        for e in exp_list:
            years.append(e.year)
            count.append(e.number)
        if len(years) < 2 :
            return models.Model.save(self)

        # Prepare plot
        import matplotlib
        matplotlib.use('Agg')
        from matplotlib import pyplot as plt
        plt.figure(figsize=(14, 9))
        ax = plt.subplot(111)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.get_xaxis().tick_bottom()
        ax.get_yaxis().tick_left()
        ax.set_facecolor('#D7CEC7')
        plt.rcParams['axes.facecolor'] = 'black'
        plt.xticks(range(min(years), max(years) + 1, 1), fontsize=13)
        plt.yticks(range(min(count), max(count) + 1, 1), fontsize=14)

        path = 'academic_app/static/images/' #FIXME: Use env var.

        # Fr
        plt.xlabel("Années", fontsize=16)
        plt.ylabel("Nombre d'expertises ou études techniques", fontsize=16)
        plt.bar(years, count, 1 / (max(years) - min(years)), color="#76323F")
        plt.savefig(path + 'expFR.png', bbox_inches="tight");

        # En
        plt.xlabel("Years", fontsize=16)
        plt.ylabel("Expertises or technical studies count", fontsize=16)
        plt.bar(years, count, 1 / (max(years) - min(years)), color="#76323F")
        plt.savefig(path + 'expEN.png', bbox_inches="tight");
        plt.close()

        return models.Model.save(self)


class Expertise(models.Model):
    year = models.PositiveIntegerField(
            validators=[
                MinValueValidator(1900),
                MaxValueValidator(datetime.datetime.now().year)],
            help_text="Utilisez le format suivant: YYYY")
    description_fr = RichTextField()
    description_en = RichTextField()

    def __str__(self):
        return self.description_fr


class Enseignement(models.Model):
    date_debut = models.DateField()
    date_fin = models.DateField(blank=True, null=True)
    lieu = models.CharField(max_length=200)
    description = RichTextField()

    def __str__(self):
        a = strip_tags(self.description)
        print(a)
        return a


class StaticText(models.Model):
    TAG_CHOICES = (
        ('about_page', 'about_page'),
        ('publication_page', 'publication_page'),
        ('enseignement_page', 'enseignement_page')
    )
    category = models.CharField(max_length=32, choices=TAG_CHOICES, default='about_page')
    english = RichTextField()
    french = RichTextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.category

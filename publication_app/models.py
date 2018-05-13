from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime


class Conference(models.Model):
    auteurs = models.CharField(max_length=300,
            help_text="Suivre le format suivant:"
            " Prenom1 Nom1 and Prénom2 Nom2 and ...")
    titre = models.CharField(max_length=300,
            help_text="Le titre de l'article")
    titre_livre = models.CharField(max_length=300,
            help_text="Le nom de la conférence dans laquelle l'article a été publié")
    annee = models.PositiveIntegerField(
            validators=[
                MinValueValidator(1900),
                MaxValueValidator(datetime.datetime.now().year)],
            help_text="Utilisez le format suivant: YYYY")
    editeur = models.CharField(max_length=300, blank=True)
    series = models.CharField(max_length=300, blank=True)
    adresse = models.CharField(max_length=300, blank=True,
            help_text="Suivre le format suivant: Ville, Pays")
    maison_edition = models.CharField(max_length=300, blank=True)
    volume = models.CharField(max_length=300, blank=True)
    pages = models.CharField(max_length=300, blank=True,
            help_text="Suire le format suivant: debut--fin, \
                    par exemple pour la page 9 à 16: 9--16")
    url = models.CharField(max_length=300, blank=True)
    isbn = models.CharField(max_length=300, blank=True)


    def to_latex(self):
        return """@inproceedings{{{},
        Author    = {{{}}},
        Title     = {{{}}},
        BookTitle = {{{}}},
        Year      = {{{}}},
        Editor    = {{{}}},
        Series    = {{{}}},
        Address   = {{{}}},
        Publisher = {{{}}},
        Volume    = {{{}}},
        Pages     = {{{}}},
        URL       = {{{}}},
        isbn      = {{{}}},
    }}""".format(self.auteurs[:4] + ':' + self.titre[:10].replace(' ', ''),
            self.auteurs,
            self.titre,
            self.titre_livre,
            self.annee,
            self.editeur,
            self.series,
            self.adresse,
            self.maison_edition,
            self.volume,
            self.pages,
            self.url,
            self.isbn
            )

    def __str__(self):
        return self.titre


class Article(models.Model):
    auteurs = models.CharField(max_length=300,
            help_text="Suivre le format suivant:"
            " Prenom1 Nom1 and Prénom2 Nom2 and ...")
    titre = models.CharField(max_length=300,
            help_text="Le titre de l'article")
    journal = models.CharField(max_length=300,
            help_text="Le nom du journal dans lequel l'article a été publié")
    moi = models.PositiveIntegerField(
            validators=[
                MinValueValidator(1),
                MaxValueValidator(12)],
            help_text="De Janvier(1) à Décembre(12)")
    annee = models.PositiveIntegerField(
            validators=[
                MinValueValidator(1900),
                MaxValueValidator(datetime.datetime.now().year)],
            help_text="Utilisez le format suivant: YYYY")
    pages = models.CharField(max_length=300, blank=True,
            help_text="Suire le format suivant: debut--fin, \
                    par exemple pour la page 9 à 16: 9--16")
    volume = models.CharField(max_length=300, blank=True)
    url = models.CharField(max_length=300, blank=True)
    issn = models.CharField(max_length=300, blank=True)


    def to_latex(self):
        return """@article{{{},
        Author    = {{{}}},
        Title     = {{{}}},
        Journal   = {{{}}},
        Month     = {{{}}},
        Year      = {{{}}},
        Pages     = {{{}}},
        Volume    = {{{}}},
        URL       = {{{}}},
        issn      = {{{}}},
    }}""".format(self.auteurs[:4] + ':' + self.titre[:10].replace(' ', ''),
            self.auteurs,
            self.titre,
            self.journal,
            self.moi,
            self.annee,
            self.pages,
            self.volume,
            self.url,
            self.issn
            )

    def __str__(self):
        return self.titre


class Livre(models.Model):
    auteurs = models.CharField(max_length=300,
            help_text="Suivre le format suivant:"
            " Prenom1 Nom1 and Prénom2 Nom2 and ...")
    titre = models.CharField(max_length=300,
            help_text="Le titre du livre dans lequel l'article est publié")
    maison_edition = models.CharField(max_length=300)
    annee = models.PositiveIntegerField(
            validators=[
                MinValueValidator(1900),
                MaxValueValidator(datetime.datetime.now().year)],
            help_text="Utilisez le format suivant: YYYY")
    chapitre = models.CharField(max_length=300, blank=True)
    pages = models.CharField(max_length=300, blank=True,
            help_text="Suire le format suivant: debut--fin, \
                    par exemple pour la page 9 à 16: 9--16")
    volume = models.CharField(max_length=300, blank=True)
    adresse = models.CharField(max_length=300, blank=True,
            help_text="Suivre le format suivant: Ville, Pays")
    edition = models.IntegerField(blank=True,
            help_text="Mettre 1 pour première édition, 2 pour deuxième, etc.")
    url = models.CharField(max_length=300, blank=True)


    def to_latex(self):
        return """@inbook{{{},
        Author    = {{{}}},
        Title     = {{{}}},
        Publisher = {{{}}},
        Year      = {{{}}},
        Chapter   = {{{}}},
        Pages     = {{{}}},
        Volume    = {{{}}},
        Address   = {{{}}},
        Edition   = {{{}}},
        URL       = {{{}}},
    }}""".format(self.auteurs[:4] + ':' + self.titre[:10].replace(' ', ''),
            self.auteurs,
            self.titre,
            self.maison_edition,
            self.annee,
            self.chapitre,
            self.pages,
            self.volume,
            self.adresse,
            self.edition,
            self.url
            )

    def __str__(self):
        return self.titre


class RapportTechnique(models.Model):
    auteurs = models.CharField(max_length=300,
            help_text="Suivre le format suivant:"
            " Prenom1 Nom1 and Prénom2 Nom2 and ...")
    titre = models.CharField(max_length=300,
            help_text="Le titre du livre dans lequel l'article est publié")
    institution = models.CharField(max_length=300,
            help_text="L'institution qui publie le rapport technique")
    annee = models.PositiveIntegerField(
            validators=[
                MinValueValidator(1900),
                MaxValueValidator(datetime.datetime.now().year)],
            help_text="Utilisez le format suivant: YYYY")
    adresse = models.CharField(max_length=300, blank=True,
            help_text="Suivre le format suivant: Ville, Pays")
    url = models.CharField(max_length=300, blank=True)


    def to_latex(self):
        return """@TechReport{{{},
        Author      = {{{}}},
        Title       = {{{}}},
        Institution = {{{}}},
        Year        = {{{}}},
        Address     = {{{}}},
        URL         = {{{}}},
    }}""".format(self.auteurs[:4] + ':' + self.titre[:10].replace(' ', ''),
            self.auteurs,
            self.titre,
            self.institution,
            self.annee,
            self.adresse,
            self.url
            )

    def __str__(self):
        return self.titre


class TheseDoctorale(models.Model):
    auteur = models.CharField(max_length=300,
            help_text="Suivre le format suivant:"
            " Prenom1 Nom1 and Prénom2 Nom2 and ...")
    titre = models.CharField(max_length=300,
            help_text="Le titre du livre dans lequel l'article est publié")
    ecole = models.CharField(max_length=300)
    departement = models.CharField(max_length=300)
    annee = models.PositiveIntegerField(
            validators=[
                MinValueValidator(1900),
                MaxValueValidator(datetime.datetime.now().year)],
            help_text="Utilisez le format suivant: YYYY")
    url = models.CharField(max_length=300, blank=True)


    def to_latex(self):
        return """@PhdThesis{{{},
        Author       = {{{}}},
        Title        = {{{}}},
        School       = {{{}}},
        Organization = {{{}}},
        Year         = {{{}}},
        URL          = {{{}}},
    }}""".format(self.auteur[:4] + ':' + self.titre[:10].replace(' ', ''),
            self.auteur,
            self.titre,
            self.ecole,
            self.departement,
            self.annee,
            self.url
            )

    def __str__(self):
        return self.titre


class TheseMaster(models.Model):
    auteur = models.CharField(max_length=300,
            help_text="Suivre le format suivant:"
            " Prenom1 Nom1 and Prénom2 Nom2 and ...")
    titre = models.CharField(max_length=300,
            help_text="Le titre du livre dans lequel l'article est publié")
    ecole = models.CharField(max_length=300)
    departement = models.CharField(max_length=300)
    annee = models.PositiveIntegerField(
            validators=[
                MinValueValidator(1900),
                MaxValueValidator(datetime.datetime.now().year)],
            help_text="Utilisez le format suivant: YYYY")
    url = models.CharField(max_length=300, blank=True)


    def to_latex(self):
        return """@MasterThesis{{{},
        Author       = {{{}}},
        Title        = {{{}}},
        School       = {{{}}},
        Organization = {{{}}},
        Year         = {{{}}},
        URL          = {{{}}},
    }}""".format(self.auteur[:4] + ':' + self.titre[:10].replace(' ', ''),
            self.auteur,
            self.titre,
            self.ecole,
            self.departement,
            self.annee,
            self.url
            )

    def __str__(self):
        return self.titre


class AutrePublication(models.Model):
    auteurs = models.CharField(max_length=300,
            help_text="Suivre le format suivant:"
            " Prenom1 Nom1 and Prénom2 Nom2 and ...")
    titre = models.CharField(max_length=300,
            help_text="Le titre du livre dans lequel l'article est publié")
    annee = models.PositiveIntegerField(
            validators=[
                MinValueValidator(1900),
                MaxValueValidator(datetime.datetime.now().year)],
            help_text="Utilisez le format suivant: YYYY")
    url = models.CharField(max_length=300, blank=True)


    def to_latex(self):
        return """@misc{{{},
        Author       = {{{}}},
        Title        = {{{}}},
        Year         = {{{}}},
        URL          = {{{}}},
    }}""".format(self.auteurs[:4] + ':' + self.titre[:10].replace(' ', ''),
            self.auteurs,
            self.titre,
            self.annee,
            self.url
            )

    def __str__(self):
        return self.titre

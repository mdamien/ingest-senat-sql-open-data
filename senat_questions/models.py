# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Etatquestion(models.Model):
    etaquecod = models.CharField(primary_key=True, max_length=12, verbose_name='Code état')
    etaquelib = models.CharField(max_length=255, blank=True, null=True, verbose_name="Libellé de l'état")
    etaquenumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Critère de tri')

    class Meta:
        managed = False
        db_table = 'etatquestion'


class Legquestion(models.Model):
    legislature = models.BigIntegerField(primary_key=True, verbose_name='Numéro de législature')
    republique = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de république')
    leglib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé de la législature')
    legdatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date de début de la législature')
    legdatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin de la législature')

    class Meta:
        managed = False
        db_table = 'legquestion'


class Naturequestion(models.Model):
    natquecod = models.CharField(primary_key=True, max_length=12, verbose_name='Code nature')
    natquelib = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé de la nature')
    natquenumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Critère de tri')

    class Meta:
        managed = False
        db_table = 'naturequestion'


class Sortquestion(models.Model):
    sorquecod = models.CharField(primary_key=True, max_length=12, verbose_name='Code sort')
    sorquelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé du sort')
    sorquenumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Critère de tri')

    class Meta:
        managed = False
        db_table = 'sortquestion'


class TamMinisteres(models.Model):
    minid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant du ministère')
    minidremp = models.BigIntegerField(blank=True, null=True, verbose_name='Identifiant du ministère de remplacement')
    datedebut = models.DateTimeField(blank=True, null=True, verbose_name='Date de début du ministère')
    datefin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin du ministère')
    ordreprotocolaire = models.BigIntegerField(blank=True, null=True, verbose_name='Ordre protocolaire')
    libelle = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé du ministère')
    libellelong = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long du ministère')
    titreministre = models.CharField(max_length=255, blank=True, null=True, verbose_name='Titre du ministre')
    intitulejo = models.CharField(max_length=255, blank=True, null=True, verbose_name='Intitulé JO du ministère')
    nomministre = models.CharField(max_length=255, blank=True, null=True, verbose_name='Nom du ministre')

    class Meta:
        managed = False
        db_table = 'tam_ministeres'


class TamQuestions(models.Model):
    id = models.BigIntegerField(primary_key=True, verbose_name='Identifiant de base')
    sorquecod = models.BigIntegerField(blank=True, null=True, verbose_name='Code sort')
    matricule = models.CharField(max_length=6, verbose_name="Matricule du sénateur à l'origine de la question")
    natquecod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code nature')
    legislature = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de législature')
    etaquecod = models.BigIntegerField(blank=True, null=True, verbose_name='Code état')
    uuid = models.CharField(max_length=120, blank=True, null=True, verbose_name='Identifiant unique')
    numero = models.CharField(max_length=12, blank=True, null=True, verbose_name='Numéro public')
    reference = models.CharField(max_length=12, blank=True, null=True, verbose_name='Référence unique')
    titre = models.CharField(max_length=255, blank=True, null=True, verbose_name='Titre')
    version = models.BigIntegerField(blank=True, null=True, verbose_name='Version')
    datecloture = models.DateTimeField(blank=True, null=True, verbose_name='Date de clôture')
    delaijours = models.BigIntegerField(blank=True, null=True, verbose_name='Délai de clôture')
    nom = models.CharField(max_length=35, blank=True, null=True, verbose_name='Nom du sénateur')
    prenom = models.CharField(max_length=35, blank=True, null=True, verbose_name='Prénom du sénateur')
    nomtechnique = models.CharField(max_length=35, blank=True, null=True, verbose_name='Nom technique')
    codequalite = models.CharField(max_length=12, blank=True, null=True, verbose_name='Civilité du sénateur')
    cirnum = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de circonscription')
    circonscription = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé de la circonscription')
    groupe = models.CharField(max_length=60, blank=True, null=True, verbose_name='Groupe politique du sénateur')
    rubrique = models.CharField(max_length=255, blank=True, null=True, verbose_name='Rubrique')
    datejodepot = models.DateTimeField(blank=True, null=True, verbose_name='Date de publication au JO')
    mindepotid = models.ForeignKey(TamMinisteres, models.DO_NOTHING, db_column='mindepotid', blank=True, null=True, related_name='+', verbose_name='Identifiant du ministère auprès duquel la question a été déposée')
    mindepotlib = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé du ministère auprès duquel la question a été déposée')
    datejotran = models.DateTimeField(blank=True, null=True, verbose_name='Date de parution du JO faisant état de la transmission de la question')
    mintranid = models.BigIntegerField(blank=True, null=True, verbose_name='Identifiant du ministère auprès duquel la question a été transmise')
    mintranlib = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé du ministère auprès duquel la question a été transmise')
    minreplib1 = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé du ministère ayant repondu à la question')
    minrepid1 = models.BigIntegerField(blank=True, null=True, verbose_name='Identifiant du ministère ayant repondu à la question')
    delaijoursrep1 = models.BigIntegerField(blank=True, null=True, verbose_name='Libellé du ministère ayant repondu à la question')
    datejorep1 = models.DateTimeField(blank=True, null=True, verbose_name='Date de publication JO de la réponse')
    datesynctam = models.DateTimeField(blank=True, null=True, verbose_name='Date technique (obsolète)')
    natqueord = models.BigIntegerField(blank=True, null=True, verbose_name='Ordre de tri des natures des questions')
    repub = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de la république')
    uuidtransori = models.CharField(max_length=120, blank=True, null=True, verbose_name="Identifiant unique de la question d'origine (avant transmission)")
    dattransori = models.DateTimeField(blank=True, null=True, verbose_name="Date de la question d'origine (avant transmission)")
    uuidtrans = models.CharField(max_length=120, blank=True, null=True, verbose_name='Identifiant unique de la question crée après transmission')
    dattrans = models.DateTimeField(blank=True, null=True, verbose_name='Date de la transformation de la question')
    uuidquerappelee = models.CharField(max_length=120, blank=True, null=True, verbose_name="Identifiant unique de la question à l'origine de cette question de rappel")
    refquerappelee = models.CharField(max_length=12, blank=True, null=True, verbose_name="Référence unique de la question à l'origine de cette question de rappel")
    daterappel = models.DateTimeField(blank=True, null=True, verbose_name='Date du rappel')
    txtque = models.TextField(blank=True, null=True, verbose_name='Texte de la question')
    themes = models.CharField(max_length=200, blank=True, null=True, verbose_name='Thème(s)')
    renvoi1 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Renvoi de rubrique 1')
    renvoi2 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Renvoi de rubrique 2')
    renvoi3 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Renvoi de rubrique 3')
    datesignal = models.DateTimeField(blank=True, null=True, verbose_name='Date de signalement de la question')
    pagejodepot = models.BigIntegerField(blank=True, null=True, verbose_name='Page de publication JO de la question')
    pageerr = models.BigIntegerField(blank=True, null=True, verbose_name="Page de publication JO de l'erratum question")
    dateerr = models.DateTimeField(blank=True, null=True, verbose_name="Date publication JO de l'erratum question")
    ratgrp = models.CharField(max_length=2, blank=True, null=True, verbose_name='Type Appartenance')
    thecrible = models.CharField(max_length=255, blank=True, null=True, verbose_name='Thème QCT')
    txterrque = models.TextField(blank=True, null=True, verbose_name="Texte de l'erratum question")
    tranisreattr = models.CharField(max_length=1, blank=True, null=True, verbose_name="Vaut N s'il s'agit d'une réaffectation ou O s'il s'agit d'une réattribution")
    compub = models.TextField(blank=True, null=True, verbose_name='Commentaire public')
    dateseance = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tam_questions'


class TamReponses(models.Model):
    idque = models.ForeignKey(TamQuestions, models.DO_NOTHING, db_column='idque', related_name='+', verbose_name='Identifiant de base de la question')
    datejorep = models.DateTimeField(blank=True, null=True, verbose_name='Date publication JO de la réponse')
    txtrep = models.TextField(blank=True, null=True, verbose_name='Texte de la réponse')
    delaijoursrep = models.BigIntegerField(blank=True, null=True, verbose_name='Délai en jours de la réponse')
    minrepid = models.BigIntegerField(blank=True, null=True, verbose_name='Identifiant du ministère ayant repondu à la question')
    minreplib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé du ministère ayant repondu à la question')
    pagejorep = models.BigIntegerField(blank=True, null=True, verbose_name='Page de publication JO de la réponse')
    urlrep = models.CharField(max_length=255, blank=True, null=True, verbose_name='URL du compte rendu où figure la réponse sur senat.fr')
    errpage = models.BigIntegerField(blank=True, null=True, verbose_name="Page de publication JO de l'erratum réponse")
    errdate = models.DateTimeField(blank=True, null=True, verbose_name="Date publication JO de l'erratum réponse")
    idrepunique = models.CharField(max_length=120, blank=True, null=True, verbose_name='Identifiant de base de la réponse dans le cas de réponses communes')
    txterrrep = models.TextField(blank=True, null=True, verbose_name="Texte de l'erratum réponse")

    class Meta:
        managed = False
        db_table = 'tam_reponses'


class The(models.Model):
    thecle = models.SmallIntegerField(primary_key=True, verbose_name='Code thème')
    thelib = models.CharField(max_length=80, verbose_name='Libellé du thème')
    theali = models.CharField(max_length=80, blank=True, null=True, verbose_name="Libellé d'édition thème")
    thenouidt = models.BigIntegerField(blank=True, null=True, verbose_name='Critère de tri')

    class Meta:
        managed = False
        db_table = 'the'

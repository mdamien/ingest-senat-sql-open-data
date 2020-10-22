# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Etatquestion(models.Model):
    etaquecod = models.CharField(primary_key=True, max_length=12)
    etaquelib = models.CharField(max_length=255, blank=True, null=True)
    etaquenumtri = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.etaquelib

    class Meta:
        managed = False
        db_table = 'etatquestion'


class Legquestion(models.Model):
    legislature = models.BigIntegerField(primary_key=True)
    republique = models.BigIntegerField(blank=True, null=True)
    leglib = models.CharField(max_length=120, blank=True, null=True)
    legdatdeb = models.DateTimeField(blank=True, null=True)
    legdatfin = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.leglib

    class Meta:
        managed = False
        db_table = 'legquestion'


class Naturequestion(models.Model):
    natquecod = models.CharField(primary_key=True, max_length=12)
    natquelib = models.CharField(max_length=255, blank=True, null=True)
    natquenumtri = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.natquelib

    class Meta:
        managed = False
        db_table = 'naturequestion'


class Sortquestion(models.Model):
    sorquecod = models.CharField(primary_key=True, max_length=12)
    sorquelib = models.CharField(max_length=120, blank=True, null=True)
    sorquenumtri = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.sorquelib

    class Meta:
        managed = False
        db_table = 'sortquestion'


class TamMinisteres(models.Model):
    minid = models.BigIntegerField(primary_key=True)
    minidremp = models.BigIntegerField(blank=True, null=True)
    datedebut = models.DateTimeField(blank=True, null=True)
    datefin = models.DateTimeField(blank=True, null=True)
    ordreprotocolaire = models.BigIntegerField(blank=True, null=True)
    libelle = models.CharField(max_length=255, blank=True, null=True)
    libellelong = models.CharField(max_length=255, blank=True, null=True)
    titreministre = models.CharField(max_length=255, blank=True, null=True)
    intitulejo = models.CharField(max_length=255, blank=True, null=True)
    nomministre = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.libellelong or self.libelle

    class Meta:
        managed = False
        db_table = 'tam_ministeres'


class TamQuestions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sorquecod = models.BigIntegerField(blank=True, null=True)
    matricule = models.CharField(max_length=6)
    natquecod = models.CharField(max_length=12, blank=True, null=True)
    legislature = models.BigIntegerField(blank=True, null=True)
    etaquecod = models.BigIntegerField(blank=True, null=True)
    uuid = models.CharField(max_length=120, blank=True, null=True)
    numero = models.CharField(max_length=12, blank=True, null=True)
    reference = models.CharField(max_length=12, blank=True, null=True)
    titre = models.CharField(max_length=255, blank=True, null=True)
    version = models.BigIntegerField(blank=True, null=True)
    datecloture = models.DateTimeField(blank=True, null=True)
    delaijours = models.BigIntegerField(blank=True, null=True)
    nom = models.CharField(max_length=35, blank=True, null=True)
    prenom = models.CharField(max_length=35, blank=True, null=True)
    nomtechnique = models.CharField(max_length=35, blank=True, null=True)
    codequalite = models.CharField(max_length=12, blank=True, null=True)
    cirnum = models.BigIntegerField(blank=True, null=True)
    circonscription = models.CharField(max_length=255, blank=True, null=True)
    groupe = models.CharField(max_length=60, blank=True, null=True)
    rubrique = models.CharField(max_length=255, blank=True, null=True)
    datejodepot = models.DateTimeField(blank=True, null=True)
    mindepotid = models.ForeignKey(TamMinisteres, models.DO_NOTHING, db_column='mindepotid', blank=True, null=True)
    mindepotlib = models.CharField(max_length=255, blank=True, null=True)
    datejotran = models.DateTimeField(blank=True, null=True)
    mintranid = models.BigIntegerField(blank=True, null=True)
    mintranlib = models.CharField(max_length=255, blank=True, null=True)
    minreplib1 = models.CharField(max_length=255, blank=True, null=True)
    minrepid1 = models.BigIntegerField(blank=True, null=True)
    delaijoursrep1 = models.BigIntegerField(blank=True, null=True)
    datejorep1 = models.DateTimeField(blank=True, null=True)
    datesynctam = models.DateTimeField(blank=True, null=True)
    natqueord = models.BigIntegerField(blank=True, null=True)
    repub = models.BigIntegerField(blank=True, null=True)
    uuidtransori = models.CharField(max_length=120, blank=True, null=True)
    dattransori = models.DateTimeField(blank=True, null=True)
    uuidtrans = models.CharField(max_length=120, blank=True, null=True)
    dattrans = models.DateTimeField(blank=True, null=True)
    uuidquerappelee = models.CharField(max_length=120, blank=True, null=True)
    refquerappelee = models.CharField(max_length=12, blank=True, null=True)
    daterappel = models.DateTimeField(blank=True, null=True)
    txtque = models.TextField(blank=True, null=True)
    themes = models.CharField(max_length=200, blank=True, null=True)
    renvoi1 = models.CharField(max_length=200, blank=True, null=True)
    renvoi2 = models.CharField(max_length=200, blank=True, null=True)
    renvoi3 = models.CharField(max_length=200, blank=True, null=True)
    datesignal = models.DateTimeField(blank=True, null=True)
    pagejodepot = models.BigIntegerField(blank=True, null=True)
    pageerr = models.BigIntegerField(blank=True, null=True)
    dateerr = models.DateTimeField(blank=True, null=True)
    ratgrp = models.CharField(max_length=2, blank=True, null=True)
    thecrible = models.CharField(max_length=255, blank=True, null=True)
    txterrque = models.TextField(blank=True, null=True)
    tranisreattr = models.CharField(max_length=1, blank=True, null=True)
    compub = models.TextField(blank=True, null=True)
    dateseance = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tam_questions'


class TamReponses(models.Model):
    idque = models.ForeignKey(TamQuestions, models.DO_NOTHING, db_column='idque', primary_key=True)
    datejorep = models.DateTimeField(blank=True, null=True)
    txtrep = models.TextField(blank=True, null=True)
    delaijoursrep = models.BigIntegerField(blank=True, null=True)
    minrepid = models.BigIntegerField(blank=True, null=True)
    minreplib = models.CharField(max_length=120, blank=True, null=True)
    pagejorep = models.BigIntegerField(blank=True, null=True)
    urlrep = models.CharField(max_length=255, blank=True, null=True)
    errpage = models.BigIntegerField(blank=True, null=True)
    errdate = models.DateTimeField(blank=True, null=True)
    idrepunique = models.CharField(max_length=120, blank=True, null=True)
    txterrrep = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tam_reponses'


class The(models.Model): # Theme
    thecle = models.SmallIntegerField(primary_key=True)
    thelib = models.CharField(max_length=80)
    theali = models.CharField(max_length=80, blank=True, null=True)
    thenouidt = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.thelib

    class Meta:
        managed = False
        db_table = 'the'

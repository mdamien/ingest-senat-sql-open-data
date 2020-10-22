# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Debats(models.Model):
    datsea = models.DateTimeField(primary_key=True)
    debsyn = models.CharField(max_length=1, blank=True, null=True)
    autinc = models.CharField(max_length=1, blank=True, null=True)
    deburl = models.CharField(max_length=80, blank=True, null=True)
    numero = models.BigIntegerField(blank=True, null=True)
    estcongres = models.CharField(max_length=1, blank=True, null=True)
    libspec = models.CharField(max_length=256, blank=True, null=True)
    etavidcod = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'debats'


class Intdivers(models.Model):
    intdiverscle = models.BigIntegerField(primary_key=True)
    autcod = models.CharField(max_length=6)
    secdiverscle = models.BigIntegerField()
    intana = models.CharField(max_length=2048, blank=True, null=True)
    intfon = models.CharField(max_length=254, blank=True, null=True)
    intdiversordid = models.BigIntegerField(blank=True, null=True)
    inturl = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intdivers'


class Intpjl(models.Model):
    intpjlcle = models.BigIntegerField(primary_key=True)
    autcod = models.CharField(max_length=6)
    secdiscle = models.BigIntegerField()
    intana = models.CharField(max_length=2048, blank=True, null=True)
    intfon = models.CharField(max_length=254, blank=True, null=True)
    inturl = models.CharField(max_length=80, blank=True, null=True)
    intordid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'intpjl'


class Lecassdeb(models.Model):
    lecassidt = models.CharField(primary_key=True, max_length=15)
    datsea = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'lecassdeb'
        unique_together = (('lecassidt', 'datsea'),)


class Secdis(models.Model):
    secdiscle = models.BigIntegerField(primary_key=True)
    lecassidt = models.CharField(max_length=255)
    typseccod = models.ForeignKey('Typsec', models.DO_NOTHING, db_column='typseccod')
    datsea = models.DateTimeField()
    secdisnum = models.CharField(max_length=512, blank=True, null=True)
    secdisobj = models.CharField(max_length=2048, blank=True, null=True)
    secdisurl = models.CharField(max_length=80, blank=True, null=True)
    secdisordid = models.BigIntegerField(blank=True, null=True)
    secdispere = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'secdis'


class Secdivers(models.Model):
    secdiverscle = models.BigIntegerField(primary_key=True)
    typseccod = models.ForeignKey('Typsec', models.DO_NOTHING, db_column='typseccod')
    datsea = models.DateTimeField()
    secdiverslibelle = models.CharField(max_length=254, blank=True, null=True)
    secdiversobj = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'secdivers'


class Syndeb(models.Model):
    debsyn = models.CharField(primary_key=True, max_length=1)
    syndeblib = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'syndeb'


class Typsec(models.Model):
    typseccod = models.CharField(primary_key=True, max_length=32)
    typseclib = models.CharField(max_length=64)
    typseccat = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typsec'

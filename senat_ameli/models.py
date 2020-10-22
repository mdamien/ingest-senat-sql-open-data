# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Amd(models.Model):
    id = models.IntegerField(primary_key=True)
    subid = models.ForeignKey('Sub', models.DO_NOTHING, db_column='subid', blank=True, null=True)
    amdperid = models.ForeignKey('self', models.DO_NOTHING, db_column='amdperid', blank=True, null=True)
    motid = models.ForeignKey('Mot', models.DO_NOTHING, db_column='motid', blank=True, null=True)
    etaid = models.IntegerField()
    nomentid = models.ForeignKey('Ent', models.DO_NOTHING, db_column='nomentid')
    sorid = models.ForeignKey('Sor', models.DO_NOTHING, db_column='sorid', blank=True, null=True)
    avcid = models.ForeignKey('Avicom', models.DO_NOTHING, db_column='avcid', blank=True, null=True)
    avgid = models.ForeignKey('Avigvt', models.DO_NOTHING, db_column='avgid', blank=True, null=True)
    irrid = models.ForeignKey('Irr', models.DO_NOTHING, db_column='irrid', blank=True, null=True)
    txtid = models.ForeignKey('TxtAmeli', models.DO_NOTHING, db_column='txtid')
    opmid = models.ForeignKey('Ent', models.DO_NOTHING, db_column='opmid', blank=True, null=True, related_name="ent2")
    ocmid = models.ForeignKey('Ent', models.DO_NOTHING, db_column='ocmid', blank=True, null=True, related_name="ent3")
    ideid = models.IntegerField(blank=True, null=True)
    discomid = models.IntegerField(blank=True, null=True)
    num = models.CharField(max_length=8, blank=True, null=True)
    rev = models.BigIntegerField()
    typ = models.CharField(max_length=1)
    dis = models.TextField(blank=True, null=True)
    obj = models.TextField(blank=True, null=True)
    datdep = models.DateTimeField(blank=True, null=True)
    obs = models.CharField(max_length=512, blank=True, null=True)
    ord = models.BigIntegerField(blank=True, null=True)
    autext = models.CharField(max_length=1)
    subpos = models.BigIntegerField(blank=True, null=True)
    mot = models.CharField(max_length=255, blank=True, null=True)
    numabs = models.BigIntegerField(blank=True, null=True)
    subidder = models.ForeignKey('Sub', models.DO_NOTHING, db_column='subidder', blank=True, null=True, related_name="sub2")
    libgrp = models.CharField(max_length=512, blank=True, null=True)
    alinea = models.IntegerField(blank=True, null=True)
    accgou = models.CharField(max_length=16, blank=True, null=True)
    colleg = models.CharField(max_length=1)
    typrectid = models.ForeignKey('Typrect', models.DO_NOTHING, db_column='typrectid', blank=True, null=True)
    islu = models.CharField(max_length=1, blank=True, null=True)
    motposexa = models.CharField(max_length=1)
    irrlo1113valid = models.CharField(max_length=1, blank=True, null=True)
    datenvemairrasoc = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amd'


class Amdsen(models.Model):
    amdid = models.OneToOneField(Amd, models.DO_NOTHING, db_column='amdid', primary_key=True)
    senid = models.ForeignKey('SenAmeli', models.DO_NOTHING, db_column='senid')
    rng = models.BigIntegerField(blank=True, null=True)
    qua = models.CharField(max_length=12, blank=True, null=True)
    nomuse = models.CharField(max_length=64, blank=True, null=True)
    prenomuse = models.CharField(max_length=64, blank=True, null=True)
    hom = models.CharField(max_length=1, blank=True, null=True)
    grpid = models.ForeignKey('GrppolAmeli', models.DO_NOTHING, db_column='grpid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'amdsen'
        unique_together = (('amdid', 'senid'),)


class Avicom(models.Model):
    id = models.CharField(primary_key=True, max_length=1)
    lib = models.CharField(max_length=80)
    cod = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'avicom'


class Avigvt(models.Model):
    id = models.CharField(primary_key=True, max_length=1)
    lib = models.CharField(max_length=80)
    cod = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'avigvt'


class Cab(models.Model):
    entid = models.OneToOneField('Ent', models.DO_NOTHING, db_column='entid', primary_key=True)
    codint = models.CharField(max_length=6)
    lil = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cab'


class ComAmeli(models.Model):
    entid = models.OneToOneField('Ent', models.DO_NOTHING, db_column='entid', primary_key=True)
    cod = models.CharField(max_length=12)
    lib = models.CharField(max_length=80)
    lil = models.CharField(max_length=255)
    spc = models.CharField(max_length=1)
    codint = models.CharField(max_length=12)
    tri = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'com_ameli'


class Ent(models.Model):
    id = models.IntegerField(primary_key=True)
    typ = models.CharField(max_length=1)
    act = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ent'


class Etatxt(models.Model):
    id = models.BigIntegerField(primary_key=True)
    lic = models.CharField(max_length=255)
    lib = models.CharField(max_length=255)
    txttyp = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'etatxt'


class Fbu(models.Model):
    id = models.IntegerField(primary_key=True)
    lib = models.CharField(max_length=128)
    lic = models.CharField(max_length=16)
    sesid = models.ForeignKey('Ses', models.DO_NOTHING, db_column='sesid')

    class Meta:
        managed = False
        db_table = 'fbu'


class GrppolAmeli(models.Model):
    entid = models.OneToOneField(Ent, models.DO_NOTHING, db_column='entid', primary_key=True)
    cod = models.CharField(max_length=12)
    libcou = models.CharField(max_length=80)
    lilcou = models.CharField(max_length=255)
    codint = models.CharField(max_length=60)
    tri = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grppol_ameli'


class Gvt(models.Model):
    entid = models.OneToOneField(Ent, models.DO_NOTHING, db_column='entid', primary_key=True)
    nom = models.CharField(max_length=64)
    pre = models.CharField(max_length=64)
    qua = models.CharField(max_length=12)
    tit = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'gvt'


class Intora(models.Model):
    id = models.IntegerField(primary_key=True)
    subid = models.ForeignKey('Sub', models.DO_NOTHING, db_column='subid', blank=True, null=True)
    entid = models.ForeignKey(Ent, models.DO_NOTHING, db_column='entid')
    entid2 = models.ForeignKey(Ent, models.DO_NOTHING, db_column='entid2', blank=True, null=True, related_name="intora2")
    txtid = models.ForeignKey('TxtAmeli', models.DO_NOTHING, db_column='txtid')
    seaid = models.ForeignKey('Sea', models.DO_NOTHING, db_column='seaid', blank=True, null=True)
    mom = models.CharField(max_length=1)
    ord = models.BigIntegerField()
    rolcod = models.ForeignKey('Orarol', models.DO_NOTHING, db_column='rolcod')
    temps = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'intora'


class Irr(models.Model):
    id = models.IntegerField(primary_key=True)
    lib = models.CharField(max_length=255)
    cod = models.CharField(max_length=4)
    libirr = models.CharField(max_length=255, blank=True, null=True)
    art = models.CharField(max_length=32, blank=True, null=True)
    lilmin = models.CharField(max_length=512, blank=True, null=True)
    par = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'irr'


class LecAmeli(models.Model):
    id = models.IntegerField(primary_key=True)
    lib = models.CharField(max_length=80)
    lecpreid = models.ForeignKey('self', models.DO_NOTHING, db_column='lecpreid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lec_ameli'


class Mot(models.Model):
    id = models.IntegerField(primary_key=True)
    lib = models.CharField(max_length=255)
    int = models.CharField(max_length=255, blank=True, null=True)
    cod = models.CharField(max_length=8, blank=True, null=True)
    ord = models.BigIntegerField()
    libnbe = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mot'


class Nat(models.Model):
    id = models.IntegerField(primary_key=True)
    lib = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'nat'


class Orarol(models.Model):
    cod = models.CharField(primary_key=True, max_length=10)
    lib = models.CharField(max_length=128, blank=True, null=True)
    entreq = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'orarol'


class Sai(models.Model):
    id = models.IntegerField(primary_key=True)
    txtid = models.ForeignKey('TxtAmeli', models.DO_NOTHING, db_column='txtid')
    comid = models.ForeignKey(ComAmeli, models.DO_NOTHING, db_column='comid')
    sesid = models.ForeignKey('Ses', models.DO_NOTHING, db_column='sesid')
    numrap = models.BigIntegerField(blank=True, null=True)
    saityp = models.CharField(max_length=1)
    isdelegfond = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'sai'


class Saisen(models.Model):
    id = models.OneToOneField(Sai, models.DO_NOTHING, db_column='id', primary_key=True)
    senid = models.ForeignKey('SenAmeli', models.DO_NOTHING, db_column='senid')
    ord = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'saisen'
        unique_together = (('id', 'senid'),)


class Sea(models.Model):
    id = models.IntegerField(primary_key=True)
    sesid = models.ForeignKey('Ses', models.DO_NOTHING, db_column='sesid')
    dat = models.DateTimeField(blank=True, null=True)
    num = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sea'


class SenAmeli(models.Model):
    entid = models.OneToOneField(Ent, models.DO_NOTHING, db_column='entid', primary_key=True)
    grpid = models.ForeignKey(GrppolAmeli, models.DO_NOTHING, db_column='grpid')
    comid = models.ForeignKey(ComAmeli, models.DO_NOTHING, db_column='comid', blank=True, null=True)
    comspcid = models.ForeignKey(ComAmeli, models.DO_NOTHING, db_column='comspcid', blank=True, null=True, related_name="senameli2")
    mat = models.CharField(max_length=6)
    qua = models.CharField(max_length=12)
    nomuse = models.CharField(max_length=64)
    prenomuse = models.CharField(max_length=64)
    nomtec = models.CharField(max_length=64, blank=True, null=True)
    hom = models.CharField(max_length=1, blank=True, null=True)
    app = models.CharField(max_length=1, blank=True, null=True)
    ratt = models.CharField(max_length=1, blank=True, null=True)
    nomusemin = models.CharField(max_length=64)
    senfem = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sen_ameli'


class Ses(models.Model):
    id = models.IntegerField(primary_key=True)
    typid = models.ForeignKey('Typses', models.DO_NOTHING, db_column='typid')
    ann = models.BigIntegerField()
    lil = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ses'


class Sor(models.Model):
    id = models.CharField(primary_key=True, max_length=1)
    lib = models.CharField(max_length=80)
    cod = models.CharField(max_length=4)
    typ = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'sor'


class Sub(models.Model):
    id = models.IntegerField(primary_key=True)
    txtid = models.ForeignKey('TxtAmeli', models.DO_NOTHING, db_column='txtid')
    merid = models.ForeignKey('self', models.DO_NOTHING, db_column='merid', blank=True, null=True)
    typid = models.ForeignKey('Typsub', models.DO_NOTHING, db_column='typid', blank=True, null=True)
    lic = models.CharField(max_length=32, blank=True, null=True)
    lib = models.CharField(max_length=512, blank=True, null=True)
    pos = models.BigIntegerField(blank=True, null=True)
    sig = models.CharField(max_length=1024, blank=True, null=True)
    posder = models.BigIntegerField(blank=True, null=True)
    prires = models.BigIntegerField(blank=True, null=True)
    dupl = models.CharField(max_length=1)
    subamd = models.CharField(max_length=1)
    sorid = models.CharField(max_length=1, blank=True, null=True)
    txtidder = models.IntegerField(blank=True, null=True)
    style = models.CharField(max_length=10)
    islec = models.CharField(max_length=1)
    comdelid = models.ForeignKey(ComAmeli, models.DO_NOTHING, db_column='comdelid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub'


class TxtAmeli(models.Model):
    id = models.IntegerField(primary_key=True)
    natid = models.ForeignKey(Nat, models.DO_NOTHING, db_column='natid')
    lecid = models.ForeignKey(LecAmeli, models.DO_NOTHING, db_column='lecid')
    sesinsid = models.ForeignKey(Ses, models.DO_NOTHING, db_column='sesinsid', blank=True, null=True)
    sesdepid = models.ForeignKey(Ses, models.DO_NOTHING, db_column='sesdepid', related_name="txtameli2")
    fbuid = models.ForeignKey(Fbu, models.DO_NOTHING, db_column='fbuid', blank=True, null=True)
    num = models.CharField(max_length=32)
    int = models.CharField(max_length=80)
    inl = models.CharField(max_length=720, blank=True, null=True)
    datdep = models.DateTimeField()
    urg = models.CharField(max_length=1)
    dis = models.CharField(max_length=1)
    secdel = models.CharField(max_length=1)
    loifin = models.CharField(max_length=1)
    loifinpar = models.BigIntegerField(blank=True, null=True)
    txtamd = models.CharField(max_length=1)
    datado = models.DateTimeField(blank=True, null=True)
    numado = models.BigIntegerField(blank=True, null=True)
    txtexa = models.CharField(max_length=1, blank=True, null=True)
    pubdellim = models.DateTimeField(blank=True, null=True)
    numabs = models.IntegerField(blank=True, null=True)
    libdelim = models.CharField(max_length=512, blank=True, null=True)
    libcplnat = models.CharField(max_length=256, blank=True, null=True)
    doslegsignet = models.CharField(max_length=48, blank=True, null=True)
    proacc = models.CharField(max_length=1)
    txttyp = models.CharField(max_length=1)
    ordsnddelib = models.CharField(max_length=5, blank=True, null=True)
    txtetaid = models.ForeignKey(Etatxt, models.DO_NOTHING, db_column='txtetaid')
    fusderid = models.ForeignKey('self', models.DO_NOTHING, db_column='fusderid', blank=True, null=True)
    fusder = models.CharField(max_length=1)
    fusderord = models.IntegerField()
    fusdertyp = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'txt_ameli'


class Typrect(models.Model):
    id = models.IntegerField(primary_key=True)
    lib = models.CharField(max_length=120)
    ord = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'typrect'


class Typses(models.Model):
    id = models.IntegerField(primary_key=True)
    lib = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typses'


class Typsub(models.Model):
    id = models.IntegerField(primary_key=True)
    lib = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'typsub'


class WNivrec(models.Model):
    num = models.BigIntegerField(primary_key=True)
    lib = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'w_nivrec'

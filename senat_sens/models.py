# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Activite(models.Model):
    actid = models.BigIntegerField(primary_key=True)
    typactcod = models.CharField(max_length=30)
    catactcod = models.CharField(max_length=20)
    scrid = models.BigIntegerField(blank=True, null=True)
    comcod = models.CharField(max_length=12, blank=True, null=True)
    delegacod = models.CharField(max_length=12, blank=True, null=True)
    actlic = models.CharField(max_length=90, blank=True, null=True)
    actlib = models.CharField(max_length=120, blank=True, null=True)
    datdeb = models.DateTimeField()
    datfin = models.DateTimeField()
    validdat = models.DateTimeField(blank=True, null=True)
    envjodat = models.DateTimeField(blank=True, null=True)
    nb_participants = models.BigIntegerField()
    nb_delegations = models.BigIntegerField()
    giacod = models.CharField(max_length=12, blank=True, null=True)
    gecod = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activite'


class ActiviteDelegation(models.Model):
    delegactid = models.BigIntegerField(primary_key=True)
    actid = models.BigIntegerField()
    senmat = models.CharField(max_length=6)
    senmat_delegue = models.CharField(max_length=6, blank=True, null=True)
    delegidx = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'activite_delegation'
        unique_together = (('actid', 'senmat', 'delegidx'), ('actid', 'senmat', 'delegidx'), ('actid', 'senmat', 'delegidx'),)


class ActiviteLoi(models.Model):
    actid = models.BigIntegerField(primary_key=True)
    loicod = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'activite_loi'
        unique_together = (('actid', 'loicod'),)


class ActiviteParticipant(models.Model):
    actparid = models.BigIntegerField(primary_key=True)
    actid = models.BigIntegerField()
    senmat = models.CharField(max_length=6)
    fapcod = models.CharField(max_length=30)
    fapidx = models.BigIntegerField(blank=True, null=True)
    typactparcod = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'activite_participant'
        unique_together = (('actid', 'senmat'), ('actid', 'senmat'), ('actid', 'senmat'),)


class ActiviteSenateur(models.Model):
    actsenid = models.BigIntegerField(primary_key=True)
    senmat = models.CharField(max_length=6)
    typactsencod = models.CharField(max_length=20)
    datdeb = models.DateTimeField()
    datfin = models.DateTimeField()
    libelle = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activite_senateur'


class ActivitesLiees(models.Model):
    gauche = models.BigIntegerField(primary_key=True)
    droite = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'activites_liees'
        unique_together = (('gauche', 'droite'),)


class Actpro(models.Model):
    actprocod = models.CharField(primary_key=True, max_length=12)
    actprolib = models.CharField(max_length=60)
    actpronumtri = models.BigIntegerField(blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actpro'


class Adresse(models.Model):
    adrid = models.BigIntegerField(primary_key=True)
    poiconid = models.BigIntegerField()
    typbistercod = models.CharField(max_length=12)
    typvoicod = models.CharField(max_length=12)
    adrcmp = models.CharField(max_length=38, blank=True, null=True)
    adrcmp2 = models.CharField(max_length=38, blank=True, null=True)
    adrnumvoi = models.CharField(max_length=38, blank=True, null=True)
    adrnomvoi = models.CharField(max_length=38, blank=True, null=True)
    adrcom = models.CharField(max_length=38, blank=True, null=True)
    adrcodpos = models.CharField(max_length=5, blank=True, null=True)
    adrburdis = models.CharField(max_length=38, blank=True, null=True)
    adrcdxcod = models.CharField(max_length=5, blank=True, null=True)
    adrcdxlib = models.CharField(max_length=38, blank=True, null=True)
    adrnumtri = models.BigIntegerField(blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adresse'


class Asster(models.Model):
    asstercod = models.CharField(primary_key=True, max_length=12)
    assterlib = models.CharField(max_length=120, blank=True, null=True)
    assterlic = models.CharField(max_length=60, blank=True, null=True)
    assternumtri = models.BigIntegerField(blank=True, null=True)
    assterurlcmp = models.CharField(max_length=255, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)
    assterart = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asster'


class Bur(models.Model):
    burcod = models.CharField(primary_key=True, max_length=12)
    burlib = models.CharField(max_length=120, blank=True, null=True)
    burlic = models.CharField(max_length=60, blank=True, null=True)
    burnumtri = models.BigIntegerField(blank=True, null=True)
    burlil = models.CharField(max_length=255, blank=True, null=True)
    burlibhon = models.CharField(max_length=120, blank=True, null=True)
    burlicfem = models.CharField(max_length=60, blank=True, null=True)
    burlibfem = models.CharField(max_length=120, blank=True, null=True)
    burlilfem = models.CharField(max_length=255, blank=True, null=True)
    burlicplu = models.CharField(max_length=60, blank=True, null=True)
    burlibplu = models.CharField(max_length=120, blank=True, null=True)
    burlilplu = models.CharField(max_length=255, blank=True, null=True)
    burlibhonfem = models.CharField(max_length=120, blank=True, null=True)
    burlibhonplu = models.CharField(max_length=120, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)
    burlicfemplu = models.CharField(max_length=60, blank=True, null=True)
    burlibfemplu = models.CharField(max_length=120, blank=True, null=True)
    burlilfemplu = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bur'


class CategorieActivite(models.Model):
    catactcod = models.CharField(primary_key=True, max_length=20)
    catactlic = models.CharField(max_length=60)
    catactlib = models.CharField(max_length=120)
    pleniere = models.SmallIntegerField(blank=True, null=True)
    catactlibtap = models.CharField(max_length=120, blank=True, null=True)
    publiee_jo = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorie_activite'


class Com(models.Model):
    typorgcod = models.CharField(max_length=12)
    orgcod = models.CharField(primary_key=True, max_length=12)
    orgnumtri = models.BigIntegerField(blank=True, null=True)
    orgdatcre = models.DateTimeField(blank=True, null=True)
    orgdatfin = models.DateTimeField(blank=True, null=True)
    orgnumtie = models.CharField(max_length=12, blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=500, blank=True, null=True)
    orgart = models.CharField(max_length=60, blank=True, null=True)
    comlilmin = models.CharField(max_length=500, blank=True, null=True)
    orgurlsim = models.CharField(max_length=500, blank=True, null=True)
    orgurlcmp = models.CharField(max_length=500, blank=True, null=True)
    comlibameli = models.CharField(max_length=120, blank=True, null=True)
    comcodameli = models.CharField(max_length=12, blank=True, null=True)
    divcod = models.CharField(max_length=12, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'com'


class Csp(models.Model):
    cspcod = models.CharField(primary_key=True, max_length=12)
    catprocod = models.CharField(max_length=12)
    cspfamcod = models.CharField(max_length=12)
    csplib = models.CharField(max_length=120, blank=True, null=True)
    cspnumtri = models.BigIntegerField(blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'csp'


class Delega(models.Model):
    typorgcod = models.CharField(max_length=12)
    orgcod = models.CharField(primary_key=True, max_length=12)
    orgnumtri = models.BigIntegerField(blank=True, null=True)
    orgdatcre = models.DateTimeField(blank=True, null=True)
    orgdatfin = models.DateTimeField(blank=True, null=True)
    orgnumtie = models.CharField(max_length=12, blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    orgart = models.CharField(max_length=60, blank=True, null=True)
    orgurlsim = models.CharField(max_length=255, blank=True, null=True)
    orgurlcmp = models.CharField(max_length=255, blank=True, null=True)
    orgregjur = models.CharField(max_length=255, blank=True, null=True)
    orgmoddes = models.CharField(max_length=255, blank=True, null=True)
    orgmemdep = models.CharField(max_length=12, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delega'


class Design(models.Model):
    designcod = models.CharField(primary_key=True, max_length=12)
    moddescod = models.CharField(max_length=12)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    orgcod = models.CharField(max_length=12)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    designnumtri = models.BigIntegerField(blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'design'


class Designoep(models.Model):
    designcod = models.CharField(max_length=12)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    orgcod = models.CharField(max_length=12)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    designoepnumtri = models.BigIntegerField(blank=True, null=True)
    designoepnbrtit = models.BigIntegerField(blank=True, null=True)
    designoepnbrsup = models.BigIntegerField(blank=True, null=True)
    designoepdatdeb = models.DateTimeField(blank=True, null=True)
    designoepdatfin = models.DateTimeField(blank=True, null=True)
    designoepid = models.BigIntegerField(primary_key=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)
    fonmemextparcod = models.CharField(max_length=20)
    fontemrem = models.CharField(max_length=12, blank=True, null=True)
    fonremlil = models.CharField(max_length=512, blank=True, null=True)
    incompat = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'designoep'


class Designorg(models.Model):
    designcod = models.CharField(primary_key=True, max_length=12)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    designnumtri = models.BigIntegerField(blank=True, null=True)
    designlib = models.CharField(max_length=120, blank=True, null=True)
    designlic = models.CharField(max_length=60, blank=True, null=True)
    designlil = models.CharField(max_length=255, blank=True, null=True)
    designlibfem = models.CharField(max_length=120, blank=True, null=True)
    designlicfem = models.CharField(max_length=60, blank=True, null=True)
    designlilfem = models.CharField(max_length=255, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'designorg'


class Dpt(models.Model):
    dptnum = models.BigIntegerField(primary_key=True)
    dptcod = models.CharField(max_length=12)
    dptlib = models.CharField(max_length=120)
    dptnbrsen = models.BigIntegerField(blank=True, null=True)
    dptmodscrsen = models.CharField(max_length=12, blank=True, null=True)
    dptser = models.CharField(max_length=1)
    regcod = models.CharField(max_length=12)
    dptnumtri = models.BigIntegerField()
    dptlic = models.CharField(max_length=60, blank=True, null=True)
    dptart = models.CharField(max_length=60, blank=True, null=True)
    dptlibtri = models.CharField(max_length=120, blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    dptser2004 = models.CharField(max_length=1, blank=True, null=True)
    dptcmt = models.CharField(max_length=255, blank=True, null=True)
    dptdatdeb = models.DateTimeField(blank=True, null=True)
    dptdatfin = models.DateTimeField(blank=True, null=True)
    dpturlcmp = models.CharField(max_length=255, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dpt'


class Dptele(models.Model):
    dptnum = models.BigIntegerField()
    dptelenbrsie = models.BigIntegerField(blank=True, null=True)
    dpteleid = models.BigIntegerField(primary_key=True)
    typelecod = models.CharField(max_length=12)
    validcod = models.CharField(max_length=32)
    valid2cod = models.CharField(max_length=32)
    participaidt1 = models.BigIntegerField(blank=True, null=True)
    participaidt2 = models.BigIntegerField(blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)
    eleid = models.BigIntegerField()
    dptelenbrsiepvr = models.BigIntegerField(blank=True, null=True)
    dptelecmt = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dptele'


class Dpttypman(models.Model):
    dptnum = models.BigIntegerField()
    typmancod = models.CharField(max_length=12)
    dpttypmanid = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'dpttypman'


class Ele(models.Model):
    typmancod = models.CharField(max_length=12)
    eleann = models.CharField(max_length=12)
    eledat = models.DateTimeField(blank=True, null=True)
    eledatdeb = models.DateTimeField(blank=True, null=True)
    eledatfinpre = models.DateTimeField(blank=True, null=True)
    eleser = models.CharField(max_length=1, blank=True, null=True)
    elelic = models.CharField(max_length=60, blank=True, null=True)
    elelib = models.CharField(max_length=120, blank=True, null=True)
    elelil = models.CharField(max_length=255, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)
    eleid = models.BigIntegerField(primary_key=True)
    elepar = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ele'


class Elucan(models.Model):
    eluid = models.BigIntegerField(primary_key=True)
    eludatdeb = models.DateTimeField(blank=True, null=True)
    eludatelu = models.DateTimeField(blank=True, null=True)
    eludatfin = models.DateTimeField(blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    eluanndeb = models.BigIntegerField(blank=True, null=True)
    eluannfin = models.BigIntegerField(blank=True, null=True)
    elunbrhab = models.BigIntegerField(blank=True, null=True)
    typmancod = models.CharField(max_length=12, blank=True, null=True)
    dptnum = models.BigIntegerField(blank=True, null=True)
    senmat = models.CharField(max_length=6)
    canart = models.CharField(max_length=60, blank=True, null=True)
    eludatcum = models.DateTimeField(blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elucan'


class Eludep(models.Model):
    eluid = models.BigIntegerField(primary_key=True)
    eludatdeb = models.DateTimeField(blank=True, null=True)
    depcod = models.CharField(max_length=12, blank=True, null=True)
    eludatelu = models.DateTimeField(blank=True, null=True)
    eludatfin = models.DateTimeField(blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    eluanndeb = models.BigIntegerField(blank=True, null=True)
    eluannfin = models.BigIntegerField(blank=True, null=True)
    elunbrhab = models.BigIntegerField(blank=True, null=True)
    typmancod = models.CharField(max_length=12, blank=True, null=True)
    senmat = models.CharField(max_length=6)
    eludatcum = models.DateTimeField(blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)
    id_organe_assnat = models.CharField(max_length=50, blank=True, null=True)
    circo = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eludep'


class Eludiv(models.Model):
    eluid = models.BigIntegerField(primary_key=True)
    eludatdeb = models.DateTimeField(blank=True, null=True)
    eludatelu = models.DateTimeField(blank=True, null=True)
    eludatfin = models.DateTimeField(blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    eluanndeb = models.BigIntegerField(blank=True, null=True)
    eluannfin = models.BigIntegerField(blank=True, null=True)
    elunbrhab = models.BigIntegerField(blank=True, null=True)
    typmancod = models.CharField(max_length=12, blank=True, null=True)
    senmat = models.CharField(max_length=6)
    eludatcum = models.DateTimeField(blank=True, null=True)
    eludivurlcmp = models.CharField(max_length=255, blank=True, null=True)
    eludivart = models.CharField(max_length=60, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eludiv'


class Elueur(models.Model):
    eluid = models.BigIntegerField(primary_key=True)
    eludatdeb = models.DateTimeField(blank=True, null=True)
    eludatelu = models.DateTimeField(blank=True, null=True)
    eludatfin = models.DateTimeField(blank=True, null=True)
    nationcod = models.CharField(max_length=12, blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    eluanndeb = models.BigIntegerField(blank=True, null=True)
    eluannfin = models.BigIntegerField(blank=True, null=True)
    elunbrhab = models.BigIntegerField(blank=True, null=True)
    typmancod = models.CharField(max_length=12, blank=True, null=True)
    senmat = models.CharField(max_length=6)
    eludatcum = models.DateTimeField(blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elueur'


class Elureg(models.Model):
    eluid = models.BigIntegerField(primary_key=True)
    eludatdeb = models.DateTimeField(blank=True, null=True)
    regcod = models.CharField(max_length=12, blank=True, null=True)
    eludatelu = models.DateTimeField(blank=True, null=True)
    eludatfin = models.DateTimeField(blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    eluanndeb = models.BigIntegerField(blank=True, null=True)
    eluannfin = models.BigIntegerField(blank=True, null=True)
    elunbrhab = models.BigIntegerField(blank=True, null=True)
    typmancod = models.CharField(max_length=12, blank=True, null=True)
    senmat = models.CharField(max_length=6)
    eludatcum = models.DateTimeField(blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elureg'


class Elusen(models.Model):
    eluid = models.BigIntegerField(primary_key=True)
    dptnum = models.BigIntegerField()
    eludatdeb = models.DateTimeField(blank=True, null=True)
    eludatelu = models.DateTimeField(blank=True, null=True)
    eludatfin = models.DateTimeField(blank=True, null=True)
    etadebmancod = models.CharField(max_length=12)
    etafinmancod = models.CharField(max_length=12, blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eluanndeb = models.BigIntegerField(blank=True, null=True)
    eluannfin = models.BigIntegerField(blank=True, null=True)
    typmancod = models.CharField(max_length=12, blank=True, null=True)
    senmat = models.CharField(max_length=6)
    eludatcum = models.DateTimeField(blank=True, null=True)
    turelucod = models.CharField(max_length=12)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elusen'


class Eluter(models.Model):
    eluid = models.BigIntegerField(primary_key=True)
    asstercod = models.CharField(max_length=12, blank=True, null=True)
    typmancod = models.CharField(max_length=12, blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    eludatdeb = models.DateTimeField(blank=True, null=True)
    eluanndeb = models.BigIntegerField(blank=True, null=True)
    eludatelu = models.DateTimeField(blank=True, null=True)
    eludatfin = models.DateTimeField(blank=True, null=True)
    eluannfin = models.BigIntegerField(blank=True, null=True)
    elunbrhab = models.BigIntegerField(blank=True, null=True)
    senmat = models.CharField(max_length=6)
    eludatcum = models.DateTimeField(blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eluter'


class Elutit(models.Model):
    eluid = models.BigIntegerField()
    titeluid = models.BigIntegerField(primary_key=True)
    titelecod = models.CharField(max_length=12)
    titeludatdeb = models.DateTimeField(blank=True, null=True)
    titeluanndeb = models.BigIntegerField(blank=True, null=True)
    titeludatfin = models.DateTimeField(blank=True, null=True)
    titeluannfin = models.BigIntegerField(blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    titeluhon = models.CharField(max_length=12, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elutit'


class Eluvil(models.Model):
    eluid = models.BigIntegerField(primary_key=True)
    eludatdeb = models.DateTimeField(blank=True, null=True)
    eludatelu = models.DateTimeField(blank=True, null=True)
    eludatfin = models.DateTimeField(blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    eluanndeb = models.BigIntegerField(blank=True, null=True)
    eluannfin = models.BigIntegerField(blank=True, null=True)
    elunbrhab = models.BigIntegerField(blank=True, null=True)
    typmancod = models.CharField(max_length=12, blank=True, null=True)
    senmat = models.CharField(max_length=6)
    vilart = models.CharField(max_length=60, blank=True, null=True)
    eludatcum = models.DateTimeField(blank=True, null=True)
    vilurlcmp = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=120, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eluvil'


class Etadebman(models.Model):
    etadebmancod = models.CharField(primary_key=True, max_length=12)
    etadebmanlic = models.CharField(max_length=60)
    etadebmanlib = models.CharField(max_length=120)
    etadebmannumtri = models.BigIntegerField(blank=True, null=True)
    etadebmanlil = models.CharField(max_length=255, blank=True, null=True)
    etadebmanlicfem = models.CharField(max_length=120, blank=True, null=True)
    etadebmanlibfem = models.CharField(max_length=120, blank=True, null=True)
    etadebmanlilfem = models.CharField(max_length=255, blank=True, null=True)
    etadebmanlicplu = models.CharField(max_length=60, blank=True, null=True)
    etadebmanlibplu = models.CharField(max_length=255, blank=True, null=True)
    etadebmanlilplu = models.CharField(max_length=255, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'etadebman'


class Etafinman(models.Model):
    etafinmancod = models.CharField(primary_key=True, max_length=12)
    etafinmanlic = models.CharField(max_length=60)
    etafinman = models.CharField(max_length=120)
    etafinmannumtri = models.BigIntegerField(blank=True, null=True)
    etafinmanlil = models.CharField(max_length=255, blank=True, null=True)
    etafinmanlicfem = models.CharField(max_length=60, blank=True, null=True)
    etafinmanlibfem = models.CharField(max_length=120, blank=True, null=True)
    etafinmanlilfem = models.CharField(max_length=255, blank=True, null=True)
    etafinmanlicplu = models.CharField(max_length=60, blank=True, null=True)
    etafinmanlibplu = models.CharField(max_length=120, blank=True, null=True)
    etafinmanlilplu = models.CharField(max_length=255, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'etafinman'


class Etasen(models.Model):
    etasencod = models.CharField(primary_key=True, max_length=12)
    etasenlic = models.CharField(max_length=60)
    etasenlib = models.CharField(max_length=120, blank=True, null=True)
    etasennumtri = models.BigIntegerField(blank=True, null=True)
    etasenlil = models.CharField(max_length=255, blank=True, null=True)
    etasenlicfem = models.CharField(max_length=60, blank=True, null=True)
    etasenlibfem = models.CharField(max_length=120, blank=True, null=True)
    etasenlilfem = models.CharField(max_length=255, blank=True, null=True)
    etasenlicplu = models.CharField(max_length=60, blank=True, null=True)
    etasenlibplu = models.CharField(max_length=120, blank=True, null=True)
    etasenlilplu = models.CharField(max_length=255, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'etasen'


class FonactParticipant(models.Model):
    fapcod = models.CharField(primary_key=True, max_length=30)
    faplic = models.CharField(max_length=60)
    faplicfem = models.CharField(max_length=60)
    faplib = models.CharField(max_length=120)
    faplibfem = models.CharField(max_length=120)
    faplicplu = models.CharField(max_length=60)
    faplicfemplu = models.CharField(max_length=60)
    faplibplu = models.CharField(max_length=120)
    faplibfemplu = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'fonact_participant'


class Foncom(models.Model):
    foncomcod = models.CharField(primary_key=True, max_length=12)
    foncomlib = models.CharField(max_length=120)
    foncomlic = models.CharField(max_length=60)
    foncomnumtri = models.BigIntegerField(blank=True, null=True)
    foncomlil = models.CharField(max_length=255, blank=True, null=True)
    foncomlicfem = models.CharField(max_length=60, blank=True, null=True)
    foncomlibfem = models.CharField(max_length=120, blank=True, null=True)
    foncomlilfem = models.CharField(max_length=255, blank=True, null=True)
    foncomlicplu = models.CharField(max_length=60, blank=True, null=True)
    foncomlibplu = models.CharField(max_length=120, blank=True, null=True)
    foncomlilplu = models.CharField(max_length=255, blank=True, null=True)
    foncomlicfemplu = models.CharField(max_length=60, blank=True, null=True)
    foncomlibfemplu = models.CharField(max_length=120, blank=True, null=True)
    foncomlilfemplu = models.CharField(max_length=500, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'foncom'


class Fondelega(models.Model):
    fondelcod = models.CharField(primary_key=True, max_length=12)
    fondellib = models.CharField(max_length=120)
    fondellic = models.CharField(max_length=60)
    fondelnumtri = models.BigIntegerField(blank=True, null=True)
    fondellil = models.CharField(max_length=255, blank=True, null=True)
    fondellicfem = models.CharField(max_length=60, blank=True, null=True)
    fondellibfem = models.CharField(max_length=120, blank=True, null=True)
    fondellilfem = models.CharField(max_length=255, blank=True, null=True)
    fondellicplu = models.CharField(max_length=60, blank=True, null=True)
    fondellibplu = models.CharField(max_length=120, blank=True, null=True)
    fondellilplu = models.CharField(max_length=255, blank=True, null=True)
    fondellicfemplu = models.CharField(max_length=60, blank=True, null=True)
    fondellibfemplu = models.CharField(max_length=120, blank=True, null=True)
    fondellilfemplu = models.CharField(max_length=500, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fondelega'


class Fongrppol(models.Model):
    fongrppolcod = models.CharField(primary_key=True, max_length=12)
    fongrppollib = models.CharField(max_length=120)
    fongrppollic = models.CharField(max_length=60)
    fongrppolnumtri = models.BigIntegerField(blank=True, null=True)
    fongrppollil = models.CharField(max_length=255, blank=True, null=True)
    fongrppollibfem = models.CharField(max_length=120, blank=True, null=True)
    fongrppollicfem = models.CharField(max_length=60, blank=True, null=True)
    fongrppollilfem = models.CharField(max_length=255, blank=True, null=True)
    fongrppollibplu = models.CharField(max_length=120, blank=True, null=True)
    fongrppollicplu = models.CharField(max_length=60, blank=True, null=True)
    fongrppollilplu = models.CharField(max_length=255, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)
    fongrppollicfemplu = models.CharField(max_length=60, blank=True, null=True)
    fongrppollibfemplu = models.CharField(max_length=120, blank=True, null=True)
    fongrppollilfemplu = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fongrppol'


class Fongrpsen(models.Model):
    fongrpsencod = models.CharField(primary_key=True, max_length=12)
    fongrpsenlib = models.CharField(max_length=120)
    fongrpsenlic = models.CharField(max_length=60)
    fongrpsennumtri = models.BigIntegerField(blank=True, null=True)
    fongrpsenlil = models.CharField(max_length=255, blank=True, null=True)
    fongrpsenlibfem = models.CharField(max_length=120, blank=True, null=True)
    fongrpsenlicfem = models.CharField(max_length=60, blank=True, null=True)
    fongrpsenlilfem = models.CharField(max_length=255, blank=True, null=True)
    fongrpsenlibplu = models.CharField(max_length=120, blank=True, null=True)
    fongrpsenlicplu = models.CharField(max_length=60, blank=True, null=True)
    fongrpsenlilplu = models.CharField(max_length=255, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)
    fongrpsenlicfemplu = models.CharField(max_length=60, blank=True, null=True)
    fongrpsenlibfemplu = models.CharField(max_length=120, blank=True, null=True)
    fongrpsenlilfemplu = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fongrpsen'


class Fonmemcom(models.Model):
    fonmemcomid = models.BigIntegerField(primary_key=True)
    foncomcod = models.CharField(max_length=12)
    fonmemcomdatdeb = models.DateTimeField(blank=True, null=True)
    fonmemcomdatfin = models.DateTimeField(blank=True, null=True)
    fonmemcomrngprt = models.BigIntegerField(blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    memcomid = models.BigIntegerField()
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fonmemcom'


class Fonmemdelega(models.Model):
    fonmemdelid = models.BigIntegerField(primary_key=True)
    fondelcod = models.CharField(max_length=12)
    fonmemdeldatdeb = models.DateTimeField(blank=True, null=True)
    fonmemdeldatfin = models.DateTimeField(blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    memdelegaid = models.BigIntegerField()
    fonmemdelrngele = models.BigIntegerField(blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fonmemdelega'


class Fonmemgrppol(models.Model):
    fonmemgrppolid = models.BigIntegerField(primary_key=True)
    fongrppolcod = models.CharField(max_length=12)
    fonmemgrppoldatdeb = models.DateTimeField(blank=True, null=True)
    fonmemgrppoldatfin = models.DateTimeField(blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=30, blank=True, null=True)
    evelib = models.CharField(max_length=60, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    memgrppolid = models.BigIntegerField()
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fonmemgrppol'


class Fonmemgrpsen(models.Model):
    fonmemgrpsenid = models.BigIntegerField(primary_key=True)
    fongrpsencod = models.CharField(max_length=12)
    fonmemgrpsendatdeb = models.DateTimeField()
    fonmemgrpsendatfin = models.DateTimeField(blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    memgrpsenid = models.BigIntegerField()
    fonmemgrpsenrngele = models.BigIntegerField(blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fonmemgrpsen'


class Fonmemorg(models.Model):
    fonmemorgid = models.BigIntegerField(primary_key=True)
    memorgid = models.BigIntegerField()
    fonorgcod = models.CharField(max_length=12)
    fonmemorgdatdeb = models.DateTimeField(blank=True, null=True)
    fonmemorganndeb = models.BigIntegerField(blank=True, null=True)
    fonmemorgdatfin = models.DateTimeField(blank=True, null=True)
    fonmemorgannfin = models.BigIntegerField(blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    fonmemorgrngele = models.BigIntegerField(blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fonmemorg'


class Fonorg(models.Model):
    fonorgcod = models.CharField(primary_key=True, max_length=12)
    fonorglib = models.CharField(max_length=120, blank=True, null=True)
    fonorglic = models.CharField(max_length=60, blank=True, null=True)
    fonorgnumtri = models.BigIntegerField(blank=True, null=True)
    fonorglil = models.CharField(max_length=255, blank=True, null=True)
    fonorglibfem = models.CharField(max_length=120, blank=True, null=True)
    fonorglicfem = models.CharField(max_length=60, blank=True, null=True)
    fonorglilfem = models.CharField(max_length=255, blank=True, null=True)
    fonorglibplu = models.CharField(max_length=120, blank=True, null=True)
    fonorglicplu = models.CharField(max_length=60, blank=True, null=True)
    fonorglilplu = models.CharField(max_length=255, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)
    fonorglicfemplu = models.CharField(max_length=60, blank=True, null=True)
    fonorglibfemplu = models.CharField(max_length=120, blank=True, null=True)
    fonorglilfemplu = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fonorg'


class Grppol(models.Model):
    grppolcod = models.CharField(primary_key=True, max_length=12)
    grppolpre = models.CharField(max_length=12, blank=True, null=True)
    grppoldatcre = models.DateTimeField(blank=True, null=True)
    grppoldatfin = models.DateTimeField(blank=True, null=True)
    grppolliccou = models.CharField(max_length=60, blank=True, null=True)
    grppollibcou = models.CharField(max_length=120, blank=True, null=True)
    grppollilcou = models.CharField(max_length=255, blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    typorgcod = models.CharField(max_length=12)
    grppolart = models.CharField(max_length=60, blank=True, null=True)
    grppolurlsim = models.CharField(max_length=255, blank=True, null=True)
    grppolurlcmp = models.CharField(max_length=255, blank=True, null=True)
    grppolcodamelicou = models.CharField(max_length=12, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grppol'


class Grpsenami(models.Model):
    typorgcod = models.CharField(max_length=12)
    orgcod = models.CharField(primary_key=True, max_length=12)
    orgnumtri = models.BigIntegerField(blank=True, null=True)
    orgdatcre = models.DateTimeField()
    orgdatfin = models.DateTimeField(blank=True, null=True)
    grpsenalf = models.CharField(max_length=5, blank=True, null=True)
    scnorgcod = models.CharField(max_length=12, blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    orgart = models.CharField(max_length=60, blank=True, null=True)
    grpsenweb = models.CharField(max_length=12, blank=True, null=True)
    typgrpsencod = models.CharField(max_length=12)
    orgurlsim = models.CharField(max_length=255, blank=True, null=True)
    orgurlcmp = models.CharField(max_length=255, blank=True, null=True)
    comorgcod = models.CharField(max_length=12)
    orgtemannu = models.CharField(max_length=12, blank=True, null=True)
    plaindcod = models.CharField(max_length=12)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)
    type_com_neant = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grpsenami'


class Libcom(models.Model):
    orgcod = models.CharField(max_length=12)
    libcomdatdeb = models.DateTimeField()
    libcomdatfin = models.DateTimeField(blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=500, blank=True, null=True)
    libcomart = models.CharField(max_length=12, blank=True, null=True)
    libcomlilmin = models.CharField(max_length=500, blank=True, null=True)
    libcomlibameli = models.CharField(max_length=120, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)
    libcomid = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'libcom'
        unique_together = (('orgcod', 'libcomdatdeb'),)


class Libdelega(models.Model):
    orgcod = models.CharField(max_length=12)
    libdelegadatdeb = models.DateTimeField()
    libdelegadatfin = models.DateTimeField(blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    libdelegaart = models.CharField(max_length=12, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)
    libdelegaid = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'libdelega'
        unique_together = (('orgcod', 'libdelegadatdeb'),)


class Libgrppol(models.Model):
    grppolcod = models.CharField(max_length=12)
    libgrppoldatdeb = models.DateTimeField()
    libgrppoldatfin = models.DateTimeField(blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    libgrppolart = models.CharField(max_length=60, blank=True, null=True)
    libgrppolcodameli = models.CharField(max_length=12, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)
    libgrppolid = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'libgrppol'
        unique_together = (('grppolcod', 'libgrppoldatdeb'),)


class Libgrpsen(models.Model):
    orgcod = models.CharField(max_length=12)
    libgrpsendatautbur = models.DateTimeField()
    libgrpsendatfin = models.DateTimeField(blank=True, null=True)
    libgrpsenlib = models.CharField(max_length=120)
    libgrpsenlic = models.CharField(max_length=60)
    libgrpsenlil = models.CharField(max_length=255, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)
    libgrpsenid = models.BigIntegerField(primary_key=True)
    libgrpsenart = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'libgrpsen'
        unique_together = (('orgcod', 'libgrpsendatautbur'),)


class Liborg(models.Model):
    orgcod = models.CharField(max_length=12)
    liborgdatdeb = models.DateTimeField()
    liborgdatfin = models.DateTimeField(blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    liborgart = models.CharField(max_length=60, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)
    liborgid = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'liborg'
        unique_together = (('orgcod', 'liborgdatdeb'),)


class Mel(models.Model):
    melid = models.BigIntegerField(primary_key=True)
    poiconid = models.BigIntegerField()
    melema = models.CharField(max_length=255, blank=True, null=True)
    melnumtri = models.BigIntegerField(blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mel'


class Memcom(models.Model):
    memcomid = models.BigIntegerField(primary_key=True)
    orgcod = models.CharField(max_length=12)
    memcomdatdeb = models.DateTimeField(blank=True, null=True)
    memcomdatfin = models.DateTimeField(blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    senmat = models.CharField(max_length=6)
    memcomtitsup = models.CharField(max_length=12, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'memcom'


class Memdelega(models.Model):
    memdelegaid = models.BigIntegerField(primary_key=True)
    orgcod = models.CharField(max_length=12)
    memdelegadatdeb = models.DateTimeField(blank=True, null=True)
    memdelegadatfin = models.DateTimeField(blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    senmat = models.CharField(max_length=6)
    designcod = models.CharField(max_length=12)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'memdelega'


class Memextpar(models.Model):
    memextparid = models.BigIntegerField(primary_key=True)
    orgcod = models.CharField(max_length=12, blank=True, null=True)
    memextpardatdeb = models.DateTimeField(blank=True, null=True)
    memextpardatfin = models.DateTimeField(blank=True, null=True)
    memextpartitsup = models.CharField(max_length=12, blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    senmat = models.CharField(max_length=6)
    memextparrngele = models.BigIntegerField(blank=True, null=True)
    designcod = models.CharField(max_length=12)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)
    fonmemextparcod = models.CharField(max_length=20, blank=True, null=True)
    avis_senat = models.CharField(max_length=20)
    texte_avis_senat = models.CharField(max_length=1024, blank=True, null=True)
    avis_an = models.CharField(max_length=20)
    texte_avis_an = models.CharField(max_length=1024, blank=True, null=True)
    avis_global = models.CharField(max_length=20)
    texte_avis_global = models.CharField(max_length=1024, blank=True, null=True)
    date_saisine_exec = models.DateTimeField(blank=True, null=True)
    date_annonce_seance = models.DateTimeField(blank=True, null=True)
    date_audition_senat = models.DateTimeField(blank=True, null=True)
    date_avis_senat = models.DateTimeField(blank=True, null=True)
    date_avis_an = models.DateTimeField(blank=True, null=True)
    date_avis_global = models.DateTimeField(blank=True, null=True)
    date_reponse_exec = models.DateTimeField(blank=True, null=True)
    date_publication_jo = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'memextpar'


class Memgrppol(models.Model):
    memgrppolid = models.BigIntegerField(primary_key=True)
    grppolcod = models.CharField(max_length=12)
    typapppolcod = models.CharField(max_length=1)
    memgrppoldatdeb = models.DateTimeField(blank=True, null=True)
    memgrppoldatfin = models.DateTimeField(blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    senmat = models.CharField(max_length=6)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'memgrppol'


class Memgrpsen(models.Model):
    memgrpsenid = models.BigIntegerField(primary_key=True)
    orgcod = models.CharField(max_length=12)
    memgrpsendatent = models.DateTimeField()
    memgrpsendatsor = models.DateTimeField()
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    senmat = models.CharField(max_length=6)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'memgrpsen'


class Memorg(models.Model):
    memorgid = models.BigIntegerField(primary_key=True)
    senmat = models.CharField(max_length=6)
    orgcod = models.CharField(max_length=12)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    memorgdatdeb = models.DateTimeField(blank=True, null=True)
    memorganndeb = models.BigIntegerField(blank=True, null=True)
    memorgdatfin = models.DateTimeField(blank=True, null=True)
    memorgannfin = models.BigIntegerField(blank=True, null=True)
    designcod = models.CharField(max_length=12)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'memorg'


class Minind(models.Model):
    minid = models.BigIntegerField(primary_key=True)
    senmat = models.CharField(max_length=6, blank=True, null=True)
    typmincod = models.CharField(max_length=12)
    gvtid = models.BigIntegerField()
    memgvtrngprt = models.BigIntegerField(blank=True, null=True)
    mindatdeb = models.DateTimeField(blank=True, null=True)
    minanndeb = models.BigIntegerField(blank=True, null=True)
    mindatfin = models.DateTimeField(blank=True, null=True)
    minannfin = models.BigIntegerField(blank=True, null=True)
    mincirfin = models.CharField(max_length=120, blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    titmincod = models.CharField(max_length=12)
    mindel = models.CharField(max_length=12, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)
    poicon = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'minind'


class Mismin(models.Model):
    misid = models.BigIntegerField()
    minid = models.BigIntegerField(primary_key=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mismin'
        unique_together = (('minid', 'misid'),)


class Missen(models.Model):
    misid = models.BigIntegerField(primary_key=True)
    senmat = models.CharField(max_length=6)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'missen'
        unique_together = (('misid', 'senmat'),)


class Moddes(models.Model):
    moddescod = models.CharField(primary_key=True, max_length=12)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    moddesnumtri = models.BigIntegerField(blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)
    avis_com_senat = models.CharField(max_length=12, blank=True, null=True)
    avis_com_an = models.CharField(max_length=12, blank=True, null=True)
    typmoddescod = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moddes'


class Nation(models.Model):
    nationcod = models.CharField(primary_key=True, max_length=12)
    nationlibcog = models.CharField(max_length=70, blank=True, null=True)
    nationnumtri = models.BigIntegerField(blank=True, null=True)
    nationactual = models.CharField(max_length=1, blank=True, null=True)
    nationannind = models.CharField(max_length=4, blank=True, null=True)
    nationlibenr = models.CharField(max_length=70, blank=True, null=True)
    nationancnom = models.CharField(max_length=60, blank=True, null=True)
    nationlic = models.CharField(max_length=60, blank=True, null=True)
    zongeocod = models.CharField(max_length=12)
    nationliccap = models.CharField(max_length=60, blank=True, null=True)
    nationlictri = models.CharField(max_length=60, blank=True, null=True)
    nationurlcmp = models.CharField(max_length=255, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nation'


class Nationgrpsen(models.Model):
    nationgrpsenid = models.BigIntegerField(primary_key=True)
    orgcod = models.CharField(max_length=12)
    nationcod = models.CharField(max_length=12)
    nationgpsendatdeb = models.DateTimeField(blank=True, null=True)
    nationgrpsendatfin = models.DateTimeField(blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nationgrpsen'


class Org(models.Model):
    typorgcod = models.CharField(max_length=12)
    orgcod = models.CharField(primary_key=True, max_length=12)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    orgart = models.CharField(max_length=60, blank=True, null=True)
    orgnumtri = models.BigIntegerField(blank=True, null=True)
    orgdatcre = models.DateTimeField(blank=True, null=True)
    orgdatfin = models.DateTimeField(blank=True, null=True)
    orgurlsim = models.CharField(max_length=255, blank=True, null=True)
    orgurlcmp = models.CharField(max_length=255, blank=True, null=True)
    orgregjur = models.CharField(max_length=255, blank=True, null=True)
    orgmoddes = models.CharField(max_length=255, blank=True, null=True)
    orgmemdep = models.CharField(max_length=12, blank=True, null=True)
    orgtemannu = models.CharField(max_length=12, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'org'


class Orgext(models.Model):
    typorgcod = models.CharField(max_length=12)
    orgcod = models.CharField(primary_key=True, max_length=12)
    orgnumtri = models.BigIntegerField(blank=True, null=True)
    orgdatcre = models.DateTimeField(blank=True, null=True)
    orgdatfin = models.DateTimeField(blank=True, null=True)
    orgnumtie = models.CharField(max_length=12, blank=True, null=True)
    orgextregjur = models.CharField(max_length=500, blank=True, null=True)
    orgextrubclas = models.CharField(max_length=255, blank=True, null=True)
    orgextnbrsen = models.BigIntegerField(blank=True, null=True)
    orgextdurman = models.CharField(max_length=120, blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    orgart = models.CharField(max_length=60, blank=True, null=True)
    orgextmoddes = models.CharField(max_length=500, blank=True, null=True)
    orgextminrat = models.CharField(max_length=120, blank=True, null=True)
    orgextrep = models.CharField(max_length=255, blank=True, null=True)
    orgurlsim = models.CharField(max_length=255, blank=True, null=True)
    orgurlcmp = models.CharField(max_length=255, blank=True, null=True)
    orgtemannu = models.CharField(max_length=12, blank=True, null=True)
    stajurcod = models.CharField(max_length=12)
    etaprrcod = models.CharField(max_length=12)
    orgextdatprr = models.DateTimeField(blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)
    basdescod = models.CharField(max_length=12)
    orgparite = models.CharField(max_length=12, blank=True, null=True)
    typorgextcod = models.CharField(max_length=64)
    orgextprescod = models.CharField(max_length=20)
    codesgg = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgext'


class Orgthe(models.Model):
    orgcod = models.CharField(max_length=12)
    thecle = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'orgthe'
        unique_together = (('thecle', 'orgcod'),)


class Pcs(models.Model):
    pcscod = models.CharField(primary_key=True, max_length=4)
    pcslil = models.CharField(max_length=255, blank=True, null=True)
    pcs42cod = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'pcs'


class Pcs24(models.Model):
    pcs24cod = models.CharField(primary_key=True, max_length=2)
    pcs24lib = models.CharField(max_length=95, blank=True, null=True)
    pcs8cod = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'pcs24'


class Pcs42(models.Model):
    pcs42cod = models.CharField(primary_key=True, max_length=2)
    pcs42lib = models.CharField(max_length=84, blank=True, null=True)
    pcs24cod = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'pcs42'


class Pcs8(models.Model):
    pcs8cod = models.CharField(primary_key=True, max_length=1)
    pcs8lil = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcs8'


class Pcscatpro(models.Model):
    catprocod = models.CharField(max_length=12)
    pcscod = models.CharField(max_length=4)
    procatprodef = models.CharField(max_length=12, blank=True, null=True)
    pcscatproid = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'pcscatpro'


class Poicon(models.Model):
    poiconid = models.BigIntegerField(primary_key=True)
    senmat = models.CharField(max_length=6)
    typpoiconcod = models.CharField(max_length=12)
    poiconlib = models.CharField(max_length=120, blank=True, null=True)
    poiconnumtri = models.BigIntegerField(blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poicon'


class Qua(models.Model):
    quacod = models.CharField(primary_key=True, max_length=12)
    qualic = models.CharField(max_length=60)
    quanumtri = models.BigIntegerField(blank=True, null=True)
    quacodsex = models.CharField(max_length=1, blank=True, null=True)
    qualib = models.CharField(max_length=120, blank=True, null=True)
    qualil = models.CharField(max_length=255, blank=True, null=True)
    qualicplu = models.CharField(max_length=60, blank=True, null=True)
    qualibplu = models.CharField(max_length=120, blank=True, null=True)
    qualilplu = models.CharField(max_length=255, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qua'


class Reg(models.Model):
    regcod = models.CharField(primary_key=True, max_length=12)
    territcod = models.CharField(max_length=12)
    reglib = models.CharField(max_length=120)
    regnumtri = models.BigIntegerField(blank=True, null=True)
    regcodparlis = models.CharField(max_length=12, blank=True, null=True)
    artreg = models.CharField(max_length=60, blank=True, null=True)
    regurlcmp = models.CharField(max_length=255, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)
    regcodrpl = models.CharField(max_length=12, blank=True, null=True)
    reglic = models.CharField(max_length=60, blank=True, null=True)
    reglil = models.CharField(max_length=255, blank=True, null=True)
    regdatdeb = models.DateTimeField(blank=True, null=True)
    regdatfin = models.DateTimeField(blank=True, null=True)
    regcodint = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reg'


class Sen(models.Model):
    senmat = models.CharField(primary_key=True, max_length=6)
    quacod = models.CharField(max_length=12)
    sennomuse = models.CharField(max_length=40)
    sennomtec = models.CharField(unique=True, max_length=60)
    senprenomuse = models.CharField(max_length=60)
    sendatnai = models.DateTimeField(blank=True, null=True)
    sendatdec = models.DateTimeField(blank=True, null=True)
    etasencod = models.CharField(max_length=12)
    sendespro = models.CharField(max_length=255, blank=True, null=True)
    pcscod = models.CharField(max_length=4)
    catprocod = models.CharField(max_length=12)
    sengrppolcodcou = models.CharField(max_length=12, blank=True, null=True)
    sengrppolliccou = models.CharField(max_length=60, blank=True, null=True)
    sentypappcou = models.CharField(max_length=60, blank=True, null=True)
    sencomcodcou = models.CharField(max_length=12, blank=True, null=True)
    sencomliccou = models.CharField(max_length=60, blank=True, null=True)
    sencirnumcou = models.BigIntegerField(blank=True, null=True)
    sencircou = models.CharField(max_length=120, blank=True, null=True)
    senburliccou = models.CharField(max_length=60, blank=True, null=True)
    senema = models.CharField(max_length=255, blank=True, null=True)
    sennomusecap = models.CharField(max_length=40)
    senfem = models.CharField(max_length=12, blank=True, null=True)
    sennumsie = models.BigIntegerField(blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)
    sendaiurl = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sen'
        unique_together = (('sennomuse', 'senprenomuse', 'sendatnai'),)


class Senbur(models.Model):
    senburid = models.BigIntegerField(primary_key=True)
    burcod = models.CharField(max_length=12)
    senburdatdeb = models.DateTimeField(blank=True, null=True)
    senburdatfin = models.DateTimeField(blank=True, null=True)
    senburrelint = models.CharField(max_length=12, blank=True, null=True)
    senburrngele = models.BigIntegerField(blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    senmat = models.CharField(max_length=6)
    senburhon = models.CharField(max_length=12, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'senbur'


class Sennom(models.Model):
    senmat = models.CharField(max_length=6)
    sennomdatdeb = models.DateTimeField()
    sennomdatfin = models.DateTimeField(blank=True, null=True)
    quacod = models.CharField(max_length=12)
    sennomuse = models.CharField(max_length=40)
    sennomusecap = models.CharField(max_length=40)
    sennomtec = models.CharField(max_length=60)
    senprenomuse = models.CharField(max_length=60)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)
    sennomid = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'sennom'
        unique_together = (('senmat', 'sennomdatdeb'),)


class Senurl(models.Model):
    senurlid = models.BigIntegerField(primary_key=True)
    senmat = models.CharField(max_length=6)
    typurlcod = models.CharField(max_length=12)
    senurlurl = models.CharField(max_length=255)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    senurlnumtri = models.BigIntegerField(blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'senurl'


class Stajur(models.Model):
    stajurcod = models.CharField(primary_key=True, max_length=12)
    stajurlic = models.CharField(max_length=60, blank=True, null=True)
    stajurlib = models.CharField(max_length=120, blank=True, null=True)
    stajurnumtri = models.BigIntegerField(blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stajur'


class Telephone(models.Model):
    telid = models.BigIntegerField(primary_key=True)
    typtelcod = models.CharField(max_length=12)
    poiconid = models.BigIntegerField()
    telnum = models.CharField(max_length=15, blank=True, null=True)
    telnumtri = models.BigIntegerField(blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'telephone'


class Temval(models.Model):
    temvalcod = models.CharField(primary_key=True, max_length=12)
    temvallic = models.CharField(max_length=60)
    temvallib = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'temval'


class Territ(models.Model):
    territcod = models.CharField(primary_key=True, max_length=12)
    territlib = models.CharField(max_length=120, blank=True, null=True)
    territnumtri = models.BigIntegerField(blank=True, null=True)
    territart = models.CharField(max_length=60, blank=True, null=True)
    territurlcmp = models.CharField(max_length=255, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)
    catterritcod = models.CharField(max_length=12)
    territlic = models.CharField(max_length=60, blank=True, null=True)
    territlil = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'territ'


class Titele(models.Model):
    titelecod = models.CharField(primary_key=True, max_length=12)
    titelelic = models.CharField(max_length=60)
    typmancod = models.CharField(max_length=12)
    titelelib = models.CharField(max_length=120)
    titelelil = models.CharField(max_length=255, blank=True, null=True)
    titelenumtri = models.BigIntegerField(blank=True, null=True)
    titelelicfem = models.CharField(max_length=60, blank=True, null=True)
    titelelibfem = models.CharField(max_length=120, blank=True, null=True)
    titelelilfem = models.CharField(max_length=255, blank=True, null=True)
    titelelicplu = models.CharField(max_length=60, blank=True, null=True)
    titelelibplu = models.CharField(max_length=120, blank=True, null=True)
    titelelilplu = models.CharField(max_length=255, blank=True, null=True)
    titelelibhon = models.CharField(max_length=120, blank=True, null=True)
    titelelibhonfem = models.CharField(max_length=120, blank=True, null=True)
    titelelibhonplu = models.CharField(max_length=120, blank=True, null=True)
    titeleurltempub = models.CharField(max_length=12, blank=True, null=True)
    titeledef = models.CharField(max_length=12, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'titele'


class Typadr(models.Model):
    typadrcod = models.CharField(primary_key=True, max_length=12)
    typadrlic = models.CharField(max_length=60, blank=True, null=True)
    typadrlib = models.CharField(max_length=120, blank=True, null=True)
    typadrnumtri = models.BigIntegerField(blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typadr'


class Typapppol(models.Model):
    typapppolcod = models.CharField(primary_key=True, max_length=1)
    typapppollib = models.CharField(max_length=120, blank=True, null=True)
    typapppollic = models.CharField(max_length=60, blank=True, null=True)
    typapppolnumtri = models.BigIntegerField(blank=True, null=True)
    typapppollil = models.CharField(max_length=255, blank=True, null=True)
    typapppollicfem = models.CharField(max_length=60, blank=True, null=True)
    typapppollibfem = models.CharField(max_length=120, blank=True, null=True)
    typapppollilfem = models.CharField(max_length=255, blank=True, null=True)
    typapppollicplu = models.CharField(max_length=60, blank=True, null=True)
    typapppollibplu = models.CharField(max_length=120, blank=True, null=True)
    typapppollilplu = models.CharField(max_length=255, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typapppol'


class Typbister(models.Model):
    typbistercod = models.CharField(primary_key=True, max_length=12)
    typbisterlic = models.CharField(max_length=60, blank=True, null=True)
    typbisterlib = models.CharField(max_length=120, blank=True, null=True)
    typbisternumtri = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typbister'


class TypeActivite(models.Model):
    typactcod = models.CharField(primary_key=True, max_length=30)
    typactlic = models.CharField(max_length=60)
    typactlib = models.CharField(max_length=120)
    typactlibtap = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type_activite'


class TypeActiviteParticipant(models.Model):
    typactparcod = models.CharField(primary_key=True, max_length=20)
    typactparlib = models.CharField(max_length=60)
    typactparlibfem = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'type_activite_participant'


class TypeActiviteSenateur(models.Model):
    typactsencod = models.CharField(primary_key=True, max_length=30)
    typactsenlic = models.CharField(max_length=60)
    typactsenlib = models.CharField(max_length=120)
    numtri = models.BigIntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'type_activite_senateur'


class TypeCategorie(models.Model):
    typactcod = models.CharField(primary_key=True, max_length=30)
    catactcod = models.CharField(max_length=20)
    par_defaut = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'type_categorie'
        unique_together = (('typactcod', 'catactcod'),)


class Typele(models.Model):
    typelecod = models.CharField(primary_key=True, max_length=12)
    typelelic = models.CharField(max_length=60, blank=True, null=True)
    typelelib = models.CharField(max_length=120, blank=True, null=True)
    typelelil = models.CharField(max_length=500, blank=True, null=True)
    typelenumtri = models.BigIntegerField(blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typele'


class Typgrpsen(models.Model):
    typgrpsencod = models.CharField(primary_key=True, max_length=12)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    typgrpsennumtri = models.BigIntegerField(blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typgrpsen'


class Typman(models.Model):
    typmancod = models.CharField(primary_key=True, max_length=12)
    typmanlib = models.CharField(max_length=120, blank=True, null=True)
    typmantypele = models.CharField(max_length=12, blank=True, null=True)
    typmannumtri = models.BigIntegerField(blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typman'


class Typorg(models.Model):
    typorgcod = models.CharField(primary_key=True, max_length=12)
    typorglib = models.CharField(max_length=120)
    typorglic = models.CharField(max_length=60)
    typorgnumtri = models.BigIntegerField(blank=True, null=True)
    typorgurlsim = models.CharField(max_length=500, blank=True, null=True)
    typorgurlcmp = models.CharField(max_length=500, blank=True, null=True)
    typorglibplu = models.CharField(max_length=120, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typorg'


class Typurl(models.Model):
    typurlcod = models.CharField(primary_key=True, max_length=12)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    typurllogo = models.CharField(max_length=255, blank=True, null=True)
    typurlnumtri = models.BigIntegerField(blank=True, null=True)
    typurllogoref = models.CharField(max_length=255, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typurl'


class Typvoi(models.Model):
    typvoicod = models.CharField(primary_key=True, max_length=12)
    typvoilic = models.CharField(max_length=60, blank=True, null=True)
    typvoilib = models.CharField(max_length=255, blank=True, null=True)
    typvoinumtri = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typvoi'


class Zongeo(models.Model):
    zongeocod = models.CharField(primary_key=True, max_length=12)
    concod = models.CharField(max_length=12)
    zongeolib = models.CharField(max_length=120)
    zongeolic = models.CharField(max_length=60)
    zongeonumtri = models.BigIntegerField(blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zongeo'

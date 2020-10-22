# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Amescr(models.Model):
    sesann = models.BigIntegerField()
    scrnum = models.BigIntegerField()
    amescrnum = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'amescr'


class Ass(models.Model):
    codass = models.CharField(primary_key=True, max_length=1)
    libass = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'ass'


class Aud(models.Model):
    audcle = models.BigIntegerField(primary_key=True)
    lecassidt = models.CharField(max_length=15)
    auddat = models.DateTimeField()
    audtit = models.CharField(max_length=1023)
    audurl = models.CharField(max_length=254)
    orgcod = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'aud'


class Auteur(models.Model):
    autcod = models.CharField(primary_key=True, max_length=6)
    quacod = models.CharField(max_length=2)
    typautcod = models.CharField(max_length=3)
    nomuse = models.CharField(max_length=254)
    prenom = models.CharField(max_length=36, blank=True, null=True)
    nomtec = models.CharField(max_length=254)
    autmat = models.CharField(max_length=12, blank=True, null=True)
    grpapp = models.CharField(max_length=1, blank=True, null=True)
    grprat = models.CharField(max_length=1, blank=True, null=True)
    autfct = models.CharField(max_length=254, blank=True, null=True)
    datdeb = models.DateTimeField(blank=True, null=True)
    datfin = models.DateTimeField(blank=True, null=True)
    senfem = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auteur'


class Ble(models.Model):
    blecod = models.CharField(primary_key=True, max_length=5)
    blelib = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'ble'


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


class Catrap(models.Model):
    catrapcod = models.CharField(primary_key=True, max_length=1)
    catraplib = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'catrap'


class Com(models.Model):
    typorgcod = models.ForeignKey('TyporgSen', models.DO_NOTHING, db_column='typorgcod')
    orgcod = models.CharField(primary_key=True, max_length=12)
    orgnumtri = models.BigIntegerField(blank=True, null=True)
    orgdatcre = models.DateTimeField(blank=True, null=True)
    orgdatfin = models.DateTimeField(blank=True, null=True)
    orgnumtie = models.CharField(max_length=12, blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=500, blank=True, null=True)
    eveobs = models.CharField(max_length=500, blank=True, null=True)
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


class Corscr(models.Model):
    sesann = models.BigIntegerField()
    scrnum = models.BigIntegerField()
    corscrord = models.BigIntegerField(blank=True, null=True)
    corscrtxt = models.CharField(max_length=4000)
    corscrurl = models.CharField(max_length=254, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'corscr'


class DateSeance(models.Model):
    lecidt = models.CharField(max_length=15, blank=True, null=True)
    date_s = models.DateTimeField(blank=True, null=True)
    code = models.BigIntegerField(primary_key=True)
    statut = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'date_seance'


class Deccoc(models.Model):
    deccoccod = models.CharField(primary_key=True, max_length=3)
    deccoclib = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'deccoc'


class Delega(models.Model):
    typorgcod = models.ForeignKey('TyporgSen', models.DO_NOTHING, db_column='typorgcod')
    orgcod = models.CharField(primary_key=True, max_length=12)
    orgnumtri = models.BigIntegerField(blank=True, null=True)
    orgdatcre = models.DateTimeField(blank=True, null=True)
    orgdatfin = models.DateTimeField(blank=True, null=True)
    orgnumtie = models.CharField(max_length=12, blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
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


class Denrap(models.Model):
    coddenrap = models.CharField(primary_key=True, max_length=5)
    typraprap = models.CharField(max_length=5)
    libdenrap = models.CharField(max_length=128)
    ordre = models.BigIntegerField(blank=True, null=True)
    denrapmin = models.CharField(max_length=80, blank=True, null=True)
    denraptit = models.CharField(max_length=128, blank=True, null=True)
    denrapstymin = models.CharField(max_length=40, blank=True, null=True)
    gencod = models.CharField(max_length=1)
    solnatrapcod = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'denrap'


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


class Doc(models.Model):
    docidt = models.BigIntegerField(primary_key=True)
    typdoccod = models.ForeignKey('Typdoc', models.DO_NOTHING, db_column='typdoccod', blank=True, null=True)
    docint = models.CharField(max_length=255, blank=True, null=True)
    docurl = models.CharField(max_length=255, blank=True, null=True)
    lecidt = models.ForeignKey('Lecture', models.DO_NOTHING, db_column='lecidt', blank=True, null=True)
    docdat = models.DateTimeField(blank=True, null=True)
    docnum = models.BigIntegerField(blank=True, null=True)
    sesann = models.ForeignKey('Ses', models.DO_NOTHING, db_column='sesann', blank=True, null=True)
    date_depot = models.DateTimeField(blank=True, null=True)
    doctitcou = models.CharField(max_length=254, blank=True, null=True)
    docdatsea = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doc'


class Docatt(models.Model):
    docattcle = models.BigIntegerField(primary_key=True)
    rapcod = models.BigIntegerField()
    typattcod = models.CharField(max_length=1)
    docatturl = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'docatt'


class Docsea(models.Model):
    evtseacle = models.BigIntegerField()
    docseaurl = models.CharField(max_length=160, blank=True, null=True)
    docseaurltxt = models.CharField(max_length=80, blank=True, null=True)
    docseaurlava = models.CharField(max_length=80, blank=True, null=True)
    docseaurlapr = models.CharField(max_length=80, blank=True, null=True)
    docseaord = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'docsea'


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
    evetempub = models.CharField(max_length=12, blank=True, null=True)
    dpturlcmp = models.CharField(max_length=255, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dpt'


class Dptele(models.Model):
    dptnum = models.ForeignKey(Dpt, models.DO_NOTHING, db_column='dptnum')
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


class Ecr(models.Model):
    rapcod = models.BigIntegerField(blank=True, null=True)
    ecrnumtri = models.BigIntegerField()
    autcod = models.CharField(max_length=6, blank=True, null=True)
    texcod = models.BigIntegerField(blank=True, null=True)
    ecrnum = models.BigIntegerField(primary_key=True)
    typedoc = models.CharField(max_length=1, blank=True, null=True)
    signataire = models.CharField(max_length=1, blank=True, null=True)
    docidt = models.BigIntegerField(blank=True, null=True)
    ecrqua = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecr'


class Elusen(models.Model):
    eluid = models.BigIntegerField(primary_key=True)
    dptnum = models.ForeignKey(Dpt, models.DO_NOTHING, db_column='dptnum')
    eludatdeb = models.DateTimeField(blank=True, null=True)
    eludatelu = models.DateTimeField(blank=True, null=True)
    eludatfin = models.DateTimeField(blank=True, null=True)
    etadebmancod = models.ForeignKey('Etadebman', models.DO_NOTHING, db_column='etadebmancod')
    etafinmancod = models.ForeignKey('Etafinman', models.DO_NOTHING, db_column='etafinmancod', blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eluanndeb = models.BigIntegerField(blank=True, null=True)
    eluannfin = models.BigIntegerField(blank=True, null=True)
    typmancod = models.CharField(max_length=12, blank=True, null=True)
    senmat = models.ForeignKey('Sen', models.DO_NOTHING, db_column='senmat')
    eludatcum = models.DateTimeField(blank=True, null=True)
    turelucod = models.CharField(max_length=12)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'elusen'


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
    etafinmantemsirpas = models.CharField(max_length=12, blank=True, null=True)
    etafinmancodsirpas = models.CharField(max_length=12, blank=True, null=True)
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


class Etaloi(models.Model):
    etaloicod = models.CharField(primary_key=True, max_length=2)
    etaloilib = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'etaloi'


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


class Evtsea(models.Model):
    evtseacle = models.BigIntegerField(primary_key=True)
    loicod = models.CharField(max_length=12, blank=True, null=True)
    typevtcod = models.CharField(max_length=3)
    lecassidt = models.CharField(max_length=15)
    evtseadat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evtsea'


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


class Fonmemcom(models.Model):
    fonmemcomid = models.BigIntegerField(primary_key=True)
    foncomcod = models.ForeignKey(Foncom, models.DO_NOTHING, db_column='foncomcod')
    fonmemcomdatdeb = models.DateTimeField(blank=True, null=True)
    fonmemcomdatfin = models.DateTimeField(blank=True, null=True)
    fonmemcomrngprt = models.BigIntegerField(blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    memcomid = models.ForeignKey('Memcom', models.DO_NOTHING, db_column='memcomid')
    evetempub = models.CharField(max_length=12, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fonmemcom'


class Fonmemdelega(models.Model):
    fonmemdelid = models.BigIntegerField(primary_key=True)
    fondelcod = models.ForeignKey(Fondelega, models.DO_NOTHING, db_column='fondelcod')
    fonmemdeldatdeb = models.DateTimeField(blank=True, null=True)
    fonmemdeldatfin = models.DateTimeField(blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    memdelegaid = models.ForeignKey('Memdelega', models.DO_NOTHING, db_column='memdelegaid')
    fonmemdelrngele = models.BigIntegerField(blank=True, null=True)
    evetempub = models.CharField(max_length=12, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fonmemdelega'


class Fonmemgrppol(models.Model):
    fonmemgrppolid = models.BigIntegerField(primary_key=True)
    fongrppolcod = models.ForeignKey(Fongrppol, models.DO_NOTHING, db_column='fongrppolcod')
    fonmemgrppoldatdeb = models.DateTimeField(blank=True, null=True)
    fonmemgrppoldatfin = models.DateTimeField(blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=30, blank=True, null=True)
    evelib = models.CharField(max_length=60, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    memgrppolid = models.ForeignKey('Memgrppol', models.DO_NOTHING, db_column='memgrppolid')
    evetempub = models.CharField(max_length=12, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fonmemgrppol'


class Forpub(models.Model):
    forpubcod = models.CharField(primary_key=True, max_length=3)
    forpublib = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'forpub'


class Gen(models.Model):
    gencod = models.CharField(max_length=1)
    genlib = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'gen'


class Grppol(models.Model):
    grppolcod = models.CharField(primary_key=True, max_length=12)
    grppolnumtri = models.BigIntegerField(blank=True, null=True)
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
    typorgcod = models.ForeignKey('TyporgSen', models.DO_NOTHING, db_column='typorgcod')
    grppolart = models.CharField(max_length=60, blank=True, null=True)
    grppolurlsim = models.CharField(max_length=255, blank=True, null=True)
    grppolurlcmp = models.CharField(max_length=255, blank=True, null=True)
    grppolcodamelicou = models.CharField(max_length=12, blank=True, null=True)
    evetempub = models.CharField(max_length=12, blank=True, null=True)
    grppolcodscr = models.CharField(max_length=12, blank=True, null=True)
    grppolcodrepro = models.CharField(max_length=12, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grppol'


class Lecass(models.Model):
    lecassidt = models.CharField(primary_key=True, max_length=15)
    lecidt = models.CharField(max_length=15)
    codass = models.CharField(max_length=1)
    ordreass = models.BigIntegerField()
    sesann = models.BigIntegerField(blank=True, null=True)
    ptlnum = models.SmallIntegerField(blank=True, null=True)
    ptlurl = models.CharField(max_length=254, blank=True, null=True)
    ptlnumcpl = models.CharField(max_length=40, blank=True, null=True)
    ptlnot = models.CharField(max_length=254, blank=True, null=True)
    ptlurl2 = models.CharField(max_length=254, blank=True, null=True)
    ptlnot2 = models.CharField(max_length=254, blank=True, null=True)
    ptlurl3 = models.CharField(max_length=254, blank=True, null=True)
    ptlnot3 = models.CharField(max_length=254, blank=True, null=True)
    ptlnumcpl2 = models.CharField(max_length=40, blank=True, null=True)
    ptlnumcpl3 = models.CharField(max_length=40, blank=True, null=True)
    lecassame = models.CharField(max_length=60, blank=True, null=True)
    lecassameses = models.SmallIntegerField(blank=True, null=True)
    orgcod = models.CharField(max_length=4, blank=True, null=True)
    loiintmod = models.CharField(max_length=720, blank=True, null=True)
    reucom = models.CharField(max_length=254, blank=True, null=True)
    debatsurl = models.CharField(max_length=254, blank=True, null=True)
    depot_only = models.CharField(max_length=3)
    lecassamedat = models.DateTimeField(blank=True, null=True)
    lecassamecomdat = models.DateTimeField(blank=True, null=True)
    orippr = models.CharField(max_length=1, blank=True, null=True)
    libppr = models.CharField(max_length=254, blank=True, null=True)
    sesppr = models.BigIntegerField(blank=True, null=True)
    ptlurlcom = models.CharField(max_length=254, blank=True, null=True)
    aliasppr = models.CharField(max_length=254, blank=True, null=True)
    lecassamecom = models.CharField(max_length=60, blank=True, null=True)
    lecassamesescom = models.SmallIntegerField(blank=True, null=True)
    ptlnumcom = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lecass'


class Lecassrap(models.Model):
    lecassidt = models.CharField(primary_key=True, max_length=15)
    rapcod = models.BigIntegerField()
    lecassrapord = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lecassrap'
        unique_together = (('lecassidt', 'rapcod'),)


class Lecture(models.Model):
    lecidt = models.CharField(primary_key=True, max_length=15)
    loicod = models.CharField(max_length=12)
    typleccod = models.CharField(max_length=3)
    leccom = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lecture'


class Libcom(models.Model):
    orgcod = models.ForeignKey(Com, models.DO_NOTHING, db_column='orgcod')
    libcomdatdeb = models.DateTimeField()
    libcomdatfin = models.DateTimeField(blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=500, blank=True, null=True)
    eveobs = models.CharField(max_length=500, blank=True, null=True)
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
    orgcod = models.ForeignKey(Delega, models.DO_NOTHING, db_column='orgcod')
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
    grppolcod = models.ForeignKey(Grppol, models.DO_NOTHING, db_column='grppolcod')
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


class Lnkrap(models.Model):
    rapcodper = models.OneToOneField('Rap', models.DO_NOTHING, db_column='rapcodper', primary_key=True)
    rapcodenf = models.ForeignKey('Rap', models.DO_NOTHING, db_column='rapcodenf', related_name="rap2")
    rapperdsc = models.CharField(max_length=255, blank=True, null=True)
    rapenfdsc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lnkrap'
        unique_together = (('rapcodper', 'rapcodenf'),)


class Loi(models.Model):
    loicod = models.CharField(primary_key=True, max_length=12)
    typloicod = models.CharField(max_length=4)
    etaloicod = models.CharField(max_length=2, blank=True, null=True)
    deccoccod = models.CharField(max_length=3, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)
    signet = models.CharField(max_length=36, blank=True, null=True)
    loient = models.CharField(max_length=80, blank=True, null=True)
    motclef = models.CharField(max_length=255, blank=True, null=True)
    loitit = models.CharField(max_length=255, blank=True, null=True)
    loiint = models.CharField(max_length=1024, blank=True, null=True)
    urgence = models.CharField(max_length=3, blank=True, null=True)
    url_jo = models.CharField(max_length=512, blank=True, null=True)
    loinumjo = models.CharField(max_length=36, blank=True, null=True)
    loidatjo = models.DateTimeField(blank=True, null=True)
    date_loi = models.DateTimeField(blank=True, null=True)
    loititjo = models.CharField(max_length=720, blank=True, null=True)
    url_jo2 = models.CharField(max_length=512, blank=True, null=True)
    loinumjo2 = models.CharField(max_length=36, blank=True, null=True)
    loidatjo2 = models.DateTimeField(blank=True, null=True)
    deccocurl = models.CharField(max_length=512, blank=True, null=True)
    num_decision = models.CharField(max_length=15, blank=True, null=True)
    date_decision = models.DateTimeField(blank=True, null=True)
    loicodmai = models.CharField(max_length=12, blank=True, null=True)
    loinoudelibcod = models.CharField(max_length=12, blank=True, null=True)
    motionloiorigcod = models.CharField(max_length=12, blank=True, null=True)
    objet = models.TextField(blank=True, null=True)
    url_ordonnance = models.CharField(max_length=100, blank=True, null=True)
    saisine_date = models.DateTimeField(blank=True, null=True)
    saisine_par = models.CharField(max_length=128, blank=True, null=True)
    loidatjo3 = models.DateTimeField(blank=True, null=True)
    loinumjo3 = models.CharField(max_length=36, blank=True, null=True)
    url_jo3 = models.CharField(max_length=512, blank=True, null=True)
    url_an = models.CharField(max_length=128, blank=True, null=True)
    url_presart = models.CharField(max_length=100, blank=True, null=True)
    signetalt = models.CharField(max_length=36, blank=True, null=True)
    orgcod = models.CharField(max_length=4, blank=True, null=True)
    doscocurl = models.CharField(max_length=80, blank=True, null=True)
    loiintori = models.CharField(max_length=1024, blank=True, null=True)
    proaccdat = models.DateTimeField(blank=True, null=True)
    proaccoppdat = models.DateTimeField(blank=True, null=True)
    retproaccdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'loi'


class Loithe(models.Model):
    loicod = models.OneToOneField(Loi, models.DO_NOTHING, db_column='loicod', primary_key=True)
    thecle = models.ForeignKey('The', models.DO_NOTHING, db_column='thecle')

    class Meta:
        managed = False
        db_table = 'loithe'
        unique_together = (('loicod', 'thecle'),)


class Memcom(models.Model):
    memcomid = models.BigIntegerField(primary_key=True)
    orgcod = models.ForeignKey(Com, models.DO_NOTHING, db_column='orgcod')
    memcomdatdeb = models.DateTimeField(blank=True, null=True)
    memcomdatfin = models.DateTimeField(blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    senmat = models.ForeignKey('Sen', models.DO_NOTHING, db_column='senmat')
    memcomtitsup = models.CharField(max_length=12, blank=True, null=True)
    evetempub = models.CharField(max_length=12, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'memcom'


class Memdelega(models.Model):
    memdelegaid = models.BigIntegerField(primary_key=True)
    orgcod = models.ForeignKey(Delega, models.DO_NOTHING, db_column='orgcod')
    memdelegadatdeb = models.DateTimeField(blank=True, null=True)
    memdelegadatfin = models.DateTimeField(blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    senmat = models.ForeignKey('Sen', models.DO_NOTHING, db_column='senmat')
    designcod = models.ForeignKey(Designorg, models.DO_NOTHING, db_column='designcod')
    evetempub = models.CharField(max_length=12, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'memdelega'


class Memgrppol(models.Model):
    memgrppolid = models.BigIntegerField(primary_key=True)
    grppolcod = models.ForeignKey(Grppol, models.DO_NOTHING, db_column='grppolcod')
    typapppolcod = models.ForeignKey('Typapppol', models.DO_NOTHING, db_column='typapppolcod')
    memgrppoldatdeb = models.DateTimeField(blank=True, null=True)
    memgrppoldatfin = models.DateTimeField(blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    senmat = models.ForeignKey('Sen', models.DO_NOTHING, db_column='senmat')
    evetempub = models.CharField(max_length=12, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'memgrppol'


class Natloi(models.Model):
    groupe = models.CharField(primary_key=True, max_length=36)
    natloilib = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'natloi'


class Org(models.Model):
    orgcod = models.CharField(primary_key=True, max_length=4)
    typorgcod = models.CharField(max_length=5)
    orgnom = models.CharField(max_length=128)
    orgliblon = models.CharField(max_length=255, blank=True, null=True)
    codass = models.CharField(max_length=1, blank=True, null=True)
    orglibaff = models.CharField(max_length=60, blank=True, null=True)
    orgord = models.SmallIntegerField(blank=True, null=True)
    orgurl = models.CharField(max_length=124, blank=True, null=True)
    orglibcou = models.CharField(max_length=60, blank=True, null=True)
    org_de = models.CharField(max_length=6, blank=True, null=True)
    urltra = models.CharField(max_length=124, blank=True, null=True)
    inttra = models.CharField(max_length=254, blank=True, null=True)
    orgdatdebcop = models.DateTimeField(blank=True, null=True)
    orgdatfincop = models.DateTimeField(blank=True, null=True)
    orgnomcouv = models.CharField(max_length=128, blank=True, null=True)
    senorgcod = models.CharField(max_length=12, blank=True, null=True)
    html_color = models.CharField(max_length=6, blank=True, null=True)
    orgdatdeb = models.DateTimeField(blank=True, null=True)
    orgdatfin = models.DateTimeField(blank=True, null=True)
    orggen = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'org'


class Orgnomhis(models.Model):
    onhnum = models.BigIntegerField(primary_key=True)
    orgcod = models.ForeignKey(Org, models.DO_NOTHING, db_column='orgcod')
    orgnom = models.CharField(max_length=128)
    orglibcou = models.CharField(max_length=60)
    orgliblon = models.CharField(max_length=255)
    org_de = models.CharField(max_length=6)
    intra = models.CharField(max_length=254, blank=True, null=True)
    orgnomcouv = models.CharField(max_length=128, blank=True, null=True)
    onhfin = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'orgnomhis'


class Orippr(models.Model):
    oripprcod = models.CharField(primary_key=True, max_length=1)
    oripprlib = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'orippr'


class Oritxt(models.Model):
    oritxtcod = models.CharField(primary_key=True, max_length=6)
    oritxtlib = models.CharField(max_length=255)
    oriordre = models.CharField(max_length=1, blank=True, null=True)
    codass = models.CharField(max_length=1, blank=True, null=True)
    oritxtlibfem = models.CharField(max_length=255)
    oritxtado = models.CharField(max_length=1, blank=True, null=True)
    oritxtorg = models.CharField(max_length=1, blank=True, null=True)
    oritxtmod = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oritxt'


class Posvot(models.Model):
    posvotcod = models.CharField(primary_key=True, max_length=1)
    posvotlib = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'posvot'


class Qua(models.Model):
    quacod = models.CharField(primary_key=True, max_length=2)
    qualic = models.CharField(max_length=12)
    quaabr = models.CharField(max_length=12)
    quaabrplu = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'qua'


class QuaSen(models.Model):
    quacod = models.CharField(primary_key=True, max_length=12)
    qualic = models.CharField(max_length=60)
    quanumtri = models.BigIntegerField(blank=True, null=True)
    quacodsirpas = models.CharField(max_length=1, blank=True, null=True)
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
        db_table = 'qua_sen'


class Rap(models.Model):
    rapcod = models.BigIntegerField(primary_key=True)
    sesann = models.BigIntegerField()
    coddenrap = models.CharField(max_length=5)
    typurl = models.CharField(max_length=1)
    blecod = models.CharField(max_length=5, blank=True, null=True)
    rapnum = models.BigIntegerField(blank=True, null=True)
    raptom = models.SmallIntegerField(blank=True, null=True)
    rapfac = models.SmallIntegerField(blank=True, null=True)
    rapann = models.SmallIntegerField(blank=True, null=True)
    rapvol = models.SmallIntegerField(blank=True, null=True)
    raptitcou = models.CharField(max_length=254, blank=True, null=True)
    raptil = models.CharField(max_length=600, blank=True, null=True)
    rapurl = models.CharField(max_length=255, blank=True, null=True)
    url2 = models.CharField(max_length=80, blank=True, null=True)
    url3 = models.CharField(max_length=80, blank=True, null=True)
    url4 = models.CharField(max_length=80, blank=True, null=True)
    url2txt = models.CharField(max_length=40, blank=True, null=True)
    url3txt = models.CharField(max_length=40, blank=True, null=True)
    url4txt = models.CharField(max_length=40, blank=True, null=True)
    date_depot = models.DateTimeField()
    prix = models.CharField(max_length=18, blank=True, null=True)
    rapnuman = models.BigIntegerField(blank=True, null=True)
    numerobis = models.CharField(max_length=32, blank=True, null=True)
    rapsoustit = models.CharField(max_length=1024, blank=True, null=True)
    rapdatsea = models.DateTimeField(blank=True, null=True)
    depot_only = models.CharField(max_length=3, blank=True, null=True)
    rapres = models.CharField(max_length=4000, blank=True, null=True)
    forpubcod = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rap'


class Raporg(models.Model):
    rapcod = models.OneToOneField(Rap, models.DO_NOTHING, db_column='rapcod', primary_key=True)
    orgcod = models.ForeignKey(Org, models.DO_NOTHING, db_column='orgcod')

    class Meta:
        managed = False
        db_table = 'raporg'
        unique_together = (('rapcod', 'orgcod'),)


class Rapthe(models.Model):
    rapcod = models.OneToOneField(Rap, models.DO_NOTHING, db_column='rapcod', primary_key=True)
    thecle = models.ForeignKey('The', models.DO_NOTHING, db_column='thecle')

    class Meta:
        managed = False
        db_table = 'rapthe'
        unique_together = (('rapcod', 'thecle'),)


class Rolsig(models.Model):
    signataire = models.CharField(primary_key=True, max_length=1)
    rolsiglib = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'rolsig'


class Scr(models.Model):
    sesann = models.BigIntegerField(primary_key=True)
    scrnum = models.BigIntegerField()
    code = models.BigIntegerField(blank=True, null=True)
    scrint = models.CharField(max_length=4000, blank=True, null=True)
    scrdat = models.DateTimeField(blank=True, null=True)
    scrpou = models.BigIntegerField(blank=True, null=True)
    scrcon = models.BigIntegerField(blank=True, null=True)
    scrvot = models.BigIntegerField(blank=True, null=True)
    scrsuf = models.BigIntegerField(blank=True, null=True)
    scrvotsea = models.BigIntegerField(blank=True, null=True)
    scrsufsea = models.BigIntegerField(blank=True, null=True)
    scrpousea = models.BigIntegerField(blank=True, null=True)
    scrconsea = models.BigIntegerField(blank=True, null=True)
    scrmaj = models.BigIntegerField(blank=True, null=True)
    scrmajsea = models.BigIntegerField(blank=True, null=True)
    soslib = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scr'
        unique_together = (('sesann', 'scrnum'),)


class Sen(models.Model):
    senmat = models.CharField(primary_key=True, max_length=6)
    quacod = models.ForeignKey(QuaSen, models.DO_NOTHING, db_column='quacod')
    sennomuse = models.CharField(max_length=40)
    senprenomuse = models.CharField(max_length=60)
    etasencod = models.ForeignKey(Etasen, models.DO_NOTHING, db_column='etasencod')
    sengrppolcodcou = models.ForeignKey(Grppol, models.DO_NOTHING, db_column='sengrppolcodcou', blank=True, null=True)
    sengrppolliccou = models.CharField(max_length=60, blank=True, null=True)
    sentypappcou = models.CharField(max_length=60, blank=True, null=True)
    sencomcodcou = models.ForeignKey(Com, models.DO_NOTHING, db_column='sencomcodcou', blank=True, null=True)
    sencomliccou = models.CharField(max_length=60, blank=True, null=True)
    sencirnumcou = models.ForeignKey(Dpt, models.DO_NOTHING, db_column='sencirnumcou', blank=True, null=True)
    sencircou = models.CharField(max_length=120, blank=True, null=True)
    senburliccou = models.CharField(max_length=60, blank=True, null=True)
    sendatpreele = models.DateTimeField(blank=True, null=True)
    sennomusecap = models.CharField(max_length=40)
    sencrinom = models.CharField(max_length=40, blank=True, null=True)
    senfem = models.CharField(max_length=12, blank=True, null=True)
    sennomdis = models.CharField(max_length=40, blank=True, null=True)
    sennomdit = models.CharField(max_length=40, blank=True, null=True)
    titnobcod = models.CharField(max_length=12, blank=True, null=True)
    senobs4r1 = models.CharField(max_length=500, blank=True, null=True)
    senobs4r2 = models.CharField(max_length=500, blank=True, null=True)
    senobs3r1 = models.CharField(max_length=500, blank=True, null=True)
    senobs3r2 = models.CharField(max_length=500, blank=True, null=True)
    sendatderele = models.DateTimeField(blank=True, null=True)
    sencirnumcou4r = models.BigIntegerField(blank=True, null=True)
    sencircou4r = models.CharField(max_length=120, blank=True, null=True)
    sencirnumcou3r = models.BigIntegerField(blank=True, null=True)
    sencircou3r = models.CharField(max_length=120, blank=True, null=True)
    sengrppolcodcou4r = models.CharField(max_length=12, blank=True, null=True)
    sentypappcou4r = models.CharField(max_length=60, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)
    catprocod2e = models.CharField(max_length=12, blank=True, null=True)
    sendespro2e = models.CharField(max_length=255, blank=True, null=True)
    sengrppolcommu = models.CharField(max_length=120, blank=True, null=True)
    senobscommu = models.CharField(max_length=120, blank=True, null=True)
    senburcommu = models.CharField(max_length=60, blank=True, null=True)
    identifiant_rne = models.CharField(max_length=50, blank=True, null=True)
    identifiant_assnat = models.CharField(max_length=50, blank=True, null=True)
    titre_pair_france = models.CharField(max_length=120, blank=True, null=True)
    lister_titre_pair_france = models.CharField(max_length=120, blank=True, null=True)
    fonction_pair = models.CharField(max_length=1024, blank=True, null=True)
    credit_portrait = models.CharField(max_length=512, blank=True, null=True)
    lister_autre_titre_pair_france = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sen'


class Senbur(models.Model):
    senburid = models.BigIntegerField(primary_key=True)
    burcod = models.ForeignKey(Bur, models.DO_NOTHING, db_column='burcod')
    senburdatdeb = models.DateTimeField(blank=True, null=True)
    senburdatfin = models.DateTimeField(blank=True, null=True)
    senburrelint = models.CharField(max_length=12, blank=True, null=True)
    senburrngele = models.BigIntegerField(blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True)
    evelic = models.CharField(max_length=60, blank=True, null=True)
    evelib = models.CharField(max_length=120, blank=True, null=True)
    evelil = models.CharField(max_length=255, blank=True, null=True)
    eveobs = models.CharField(max_length=255, blank=True, null=True)
    senmat = models.ForeignKey(Sen, models.DO_NOTHING, db_column='senmat')
    senburhon = models.CharField(max_length=12, blank=True, null=True)
    evetempub = models.CharField(max_length=12, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'senbur'


class Sennom(models.Model):
    senmat = models.ForeignKey(Sen, models.DO_NOTHING, db_column='senmat')
    sennomdatdeb = models.DateTimeField()
    sennomdatfin = models.DateTimeField(blank=True, null=True)
    quacod = models.ForeignKey(QuaSen, models.DO_NOTHING, db_column='quacod')
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


class Ses(models.Model):
    sesann = models.BigIntegerField(primary_key=True)
    seslib = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'ses'


class Stavot(models.Model):
    stavotidt = models.CharField(primary_key=True, max_length=2)
    stavotlib = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'stavot'


class Texte(models.Model):
    texcod = models.BigIntegerField(primary_key=True)
    oritxtcod = models.CharField(max_length=6, blank=True, null=True)
    typtxtcod = models.CharField(max_length=3)
    typurl = models.CharField(max_length=1)
    lecassidt = models.CharField(max_length=15)
    sesann = models.BigIntegerField(blank=True, null=True)
    orgcod = models.CharField(max_length=4, blank=True, null=True)
    texnum = models.BigIntegerField(blank=True, null=True)
    texurl = models.CharField(max_length=255, blank=True, null=True)
    url2 = models.CharField(max_length=36, blank=True, null=True)
    url3 = models.CharField(max_length=80, blank=True, null=True)
    url4 = models.CharField(max_length=256, blank=True, null=True)
    url2txt = models.CharField(max_length=256, blank=True, null=True)
    url3txt = models.CharField(max_length=256, blank=True, null=True)
    url4txt = models.CharField(max_length=256, blank=True, null=True)
    txtoritxtdat = models.DateTimeField()
    prix = models.CharField(max_length=18, blank=True, null=True)
    numerobis = models.CharField(max_length=32, blank=True, null=True)
    texdatsea = models.DateTimeField(blank=True, null=True)
    reserve_comspe = models.CharField(max_length=3, blank=True, null=True)
    datrejet_disc_immediate = models.DateTimeField(blank=True, null=True)
    texace = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'texte'


class TexteAncien(models.Model):
    id = models.BigIntegerField(primary_key=True)
    origine = models.CharField(max_length=2)
    sesann = models.BigIntegerField()
    numero = models.BigIntegerField()
    rectifie = models.BigIntegerField()
    date_effet = models.DateTimeField(blank=True, null=True)
    lecture = models.CharField(max_length=28, blank=True, null=True)
    statut = models.CharField(max_length=40, blank=True, null=True)
    urgence = models.BigIntegerField()
    article_type = models.CharField(max_length=2, blank=True, null=True)
    type_texte = models.CharField(max_length=50, blank=True, null=True)
    libelle = models.CharField(max_length=1024, blank=True, null=True)
    fichier = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'texte_ancien'


class The(models.Model):
    thecle = models.SmallIntegerField(primary_key=True)
    thelib = models.CharField(max_length=80)
    theali = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'the'


class Titsen(models.Model):
    titsencod = models.CharField(primary_key=True, max_length=1)
    titsenlib = models.CharField(max_length=69, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'titsen'


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


class Typatt(models.Model):
    typattcod = models.CharField(primary_key=True, max_length=1)
    typattlib = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'typatt'


class Typaut(models.Model):
    typautcod = models.CharField(primary_key=True, max_length=3)
    typautlib = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'typaut'


class Typdoc(models.Model):
    typdoccod = models.CharField(primary_key=True, max_length=3)
    typdoclib = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typdoc'


class Typevtsea(models.Model):
    typevtcod = models.CharField(primary_key=True, max_length=3)
    typevtlib = models.CharField(max_length=61)

    class Meta:
        managed = False
        db_table = 'typevtsea'


class Typlec(models.Model):
    typleccod = models.CharField(primary_key=True, max_length=3)
    typleclib = models.CharField(max_length=60)
    typlecord = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typlec'


class Typloi(models.Model):
    typloicod = models.CharField(primary_key=True, max_length=4)
    typloilib = models.CharField(max_length=80)
    groupe = models.CharField(max_length=36, blank=True, null=True)
    typloiden = models.CharField(max_length=80, blank=True, null=True)
    typloigen = models.CharField(max_length=1, blank=True, null=True)
    typloitit = models.CharField(max_length=80, blank=True, null=True)
    typloidenplu = models.CharField(max_length=80, blank=True, null=True)
    typloide = models.CharField(max_length=10, blank=True, null=True)
    typloiabr = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typloi'


class Typorg(models.Model):
    typorgcod = models.CharField(primary_key=True, max_length=5)
    typorglib = models.CharField(max_length=60)
    typorgurl = models.CharField(max_length=254, blank=True, null=True)
    typorgtitens = models.CharField(max_length=60, blank=True, null=True)
    typorgvid = models.CharField(max_length=60, blank=True, null=True)
    typorgord = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typorg'


class TyporgSen(models.Model):
    typorgcod = models.CharField(primary_key=True, max_length=12)
    typorglib = models.CharField(max_length=120)
    typorglic = models.CharField(max_length=60)
    typorgnumtri = models.BigIntegerField(blank=True, null=True)
    evetempub = models.CharField(max_length=12, blank=True, null=True)
    typorgurlsim = models.CharField(max_length=500, blank=True, null=True)
    typorgurlcmp = models.CharField(max_length=500, blank=True, null=True)
    typorglibplu = models.CharField(max_length=120, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typorg_sen'


class Typrap(models.Model):
    typraprap = models.CharField(primary_key=True, max_length=5)
    typraplib = models.CharField(max_length=60)
    typrapind = models.CharField(max_length=1)
    typraplibplu = models.CharField(max_length=60, blank=True, null=True)
    typrapurl = models.CharField(max_length=255, blank=True, null=True)
    catrapcod = models.CharField(max_length=1, blank=True, null=True)
    typraprep = models.CharField(max_length=254, blank=True, null=True)
    typrapnot = models.CharField(max_length=1, blank=True, null=True)
    typrapses = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typrap'


class Typtxt(models.Model):
    typtxtcod = models.CharField(primary_key=True, max_length=3)
    typtxtlib = models.CharField(max_length=36)

    class Meta:
        managed = False
        db_table = 'typtxt'


class Typurl(models.Model):
    typurl = models.CharField(primary_key=True, max_length=1)
    libtypurl = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'typurl'


class Votsen(models.Model):
    sesann = models.BigIntegerField(primary_key=True)
    scrnum = models.BigIntegerField()
    senmat = models.CharField(max_length=6)
    posvotcod = models.CharField(max_length=1, blank=True, null=True)
    titsencod = models.CharField(max_length=1)
    stavotidt = models.CharField(max_length=2)
    senmatdel = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'votsen'
        unique_together = (('sesann', 'scrnum', 'senmat'),)

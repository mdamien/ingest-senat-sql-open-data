# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Amd(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Identifiant')
    subid = models.ForeignKey('Sub', models.DO_NOTHING, db_column='subid', blank=True, null=True, related_name='+', verbose_name='Identifiant de la subdivision amendee')
    amdperid = models.ForeignKey('self', models.DO_NOTHING, db_column='amdperid', blank=True, null=True, related_name='+', verbose_name="Identifiant de l'amendement pere pour les sous-amendements")
    motid = models.ForeignKey('Mot', models.DO_NOTHING, db_column='motid', blank=True, null=True, related_name='+', verbose_name='Identifiant de la motion')
    etaid = models.IntegerField(verbose_name="Identifiant de l'etat de l'amendement")
    nomentid = models.ForeignKey('Ent', models.DO_NOTHING, db_column='nomentid', related_name='+', verbose_name="Identifiant de l'entite au nom de laquelle est depose l'amendement")
    sorid = models.ForeignKey('Sor', models.DO_NOTHING, db_column='sorid', blank=True, null=True, related_name='+', verbose_name="Identifiant du sort de l'amendement")
    avcid = models.ForeignKey('Avicom', models.DO_NOTHING, db_column='avcid', blank=True, null=True, related_name='+', verbose_name="Identifiant de l'avis de la commission")
    avgid = models.ForeignKey('Avigvt', models.DO_NOTHING, db_column='avgid', blank=True, null=True, related_name='+', verbose_name="Identifiant de l'avis du gouvernement")
    irrid = models.ForeignKey('Irr', models.DO_NOTHING, db_column='irrid', blank=True, null=True, related_name='+', verbose_name="Identifiant du type d'irrecevabilite")
    txtid = models.ForeignKey('TxtAmeli', models.DO_NOTHING, db_column='txtid', related_name='+', verbose_name='Identifiant du texte amende')
    opmid = models.ForeignKey('Ent', models.DO_NOTHING, db_column='opmid', blank=True, null=True, related_name='+', verbose_name="Identifiant de l'orateur pour (motion)")
    ocmid = models.ForeignKey('Ent', models.DO_NOTHING, db_column='ocmid', blank=True, null=True, related_name='+', verbose_name="Identifiant de l'orateur contre (motion)")
    ideid = models.IntegerField(blank=True, null=True, verbose_name="Identifiant d'amendements identiques")
    discomid = models.IntegerField(blank=True, null=True, verbose_name="Identifiant d'amendements en discussion commune")
    num = models.CharField(max_length=8, blank=True, null=True, verbose_name="Numero de l'amendement (avec prefixe)")
    rev = models.BigIntegerField(verbose_name='Niveau de rectification')
    typ = models.CharField(max_length=1, verbose_name="Type d'amendement")
    dis = models.TextField(blank=True, null=True, verbose_name="Dispositif de l'amendement")
    obj = models.TextField(blank=True, null=True, verbose_name="Objet de l'amendement")
    datdep = models.DateTimeField(blank=True, null=True, verbose_name="Date de depot de l'amendement")
    obs = models.CharField(max_length=512, blank=True, null=True, verbose_name="Observations ou commentaires sur l'amendement (1/2)")
    ord = models.BigIntegerField(blank=True, null=True, verbose_name="Position au sein de l'article")
    autext = models.CharField(max_length=1, verbose_name='Indication de la mention -Et plusieurs de ses collegues-')
    subpos = models.BigIntegerField(blank=True, null=True, verbose_name='Identification des amendements portant sur article additionnel (si different de 0)')
    mot = models.CharField(max_length=255, blank=True, null=True, verbose_name="Observations ou commentaires sur l'amendement (2/2)")
    numabs = models.BigIntegerField(blank=True, null=True, verbose_name="Numero absolu de l'amendement diffuse (en chiffre)")
    subidder = models.ForeignKey('Sub', models.DO_NOTHING, db_column='subidder', blank=True, null=True, related_name='+', verbose_name='Identification de la subdivision de discussion')
    libgrp = models.CharField(max_length=512, blank=True, null=True, verbose_name="Libelle complementaire (type d'appartenance au groupe)")
    alinea = models.IntegerField(blank=True, null=True, verbose_name="Numero du premier alinea modifie par l'amendement")
    accgou = models.CharField(max_length=16, blank=True, null=True, verbose_name="Amendement depose avec l'accord du gouvernement")
    colleg = models.CharField(max_length=1, verbose_name='Indication de la mendion -Et plusieurs de ses collegues- (uniquement pour les amendements de commission)')
    typrectid = models.ForeignKey('Typrect', models.DO_NOTHING, db_column='typrectid', blank=True, null=True, related_name='+', verbose_name='Identifiant du type de rectification')
    islu = models.CharField(max_length=1, blank=True, null=True)
    motposexa = models.CharField(max_length=1, verbose_name='Endroit ou de la motion qui sera examinee. M pour le derouleur de la motion. G pour la discussion generale')
    irrlo1113valid = models.CharField(max_length=1, blank=True, null=True, verbose_name="'I' si Irrecevable LO-111-3 par la commission des affaires sociales, 'R' si recevable, null si non instruit")
    datenvemairrasoc = models.DateTimeField(blank=True, null=True, verbose_name="date d'envoi du mail pour la recevabilité LO-111-3 par les affaires sociales")

    class Meta:
        managed = False
        db_table = 'amd'


class Amdsen(models.Model):
    amdid = models.ForeignKey(Amd, models.DO_NOTHING, db_column='amdid', primary_key=True, related_name='+', verbose_name='Identifiant')
    senid = models.ForeignKey('SenAmeli', models.DO_NOTHING, db_column='senid', related_name='+', verbose_name='Identifiant du signataire')
    rng = models.BigIntegerField(blank=True, null=True, verbose_name="Rang dans l'ordre des signataires")
    qua = models.CharField(max_length=12, blank=True, null=True, verbose_name='Qualite')
    nomuse = models.CharField(max_length=64, blank=True, null=True, verbose_name='Nom usuel')
    prenomuse = models.CharField(max_length=64, blank=True, null=True, verbose_name='Prenom usuel')
    hom = models.CharField(max_length=1, blank=True, null=True, verbose_name='Indication de senateurs homonymes')
    grpid = models.ForeignKey('GrppolAmeli', models.DO_NOTHING, db_column='grpid', blank=True, null=True, related_name='+')

    class Meta:
        managed = False
        db_table = 'amdsen'
        unique_together = (('amdid', 'senid'),)


class Avicom(models.Model):
    id = models.CharField(primary_key=True, max_length=1, verbose_name='Identifiant')
    lib = models.CharField(max_length=80, verbose_name='Libelle')
    cod = models.CharField(max_length=4, verbose_name='Code')

    class Meta:
        managed = False
        db_table = 'avicom'


class Avigvt(models.Model):
    id = models.CharField(primary_key=True, max_length=1, verbose_name='Identifiant')
    lib = models.CharField(max_length=80, verbose_name='Libelle')
    cod = models.CharField(max_length=4, verbose_name='Code')

    class Meta:
        managed = False
        db_table = 'avigvt'


class Cab(models.Model):
    entid = models.ForeignKey('Ent', models.DO_NOTHING, db_column='entid', primary_key=True, related_name='+', verbose_name='Identifiant')
    codint = models.CharField(max_length=6, verbose_name='Code')
    lil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libelle')

    class Meta:
        managed = False
        db_table = 'cab'


class ComAmeli(models.Model):
    entid = models.ForeignKey('Ent', models.DO_NOTHING, db_column='entid', primary_key=True, related_name='+', verbose_name='Identifiant')
    cod = models.CharField(max_length=12, verbose_name='Code')
    lib = models.CharField(max_length=80, verbose_name='Libelle')
    lil = models.CharField(max_length=255, verbose_name='Libelle long')
    spc = models.CharField(max_length=1, verbose_name='Indication si commission speciale')
    codint = models.CharField(max_length=12, verbose_name='Code interne')
    tri = models.BigIntegerField(blank=True, null=True, verbose_name='Ordre de presentation dans les listes')

    class Meta:
        managed = False
        db_table = 'com_ameli'


class Ent(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Identifiant')
    typ = models.CharField(max_length=1, verbose_name='Type')
    act = models.CharField(max_length=1, blank=True, null=True, verbose_name='Actif ou non')

    class Meta:
        managed = False
        db_table = 'ent'


class Etatxt(models.Model):
    id = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    lic = models.CharField(max_length=255, verbose_name='Libelle court')
    lib = models.CharField(max_length=255, verbose_name='Libelle')
    txttyp = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'etatxt'


class Fbu(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Identifiant')
    lib = models.CharField(max_length=128, verbose_name='Libelle')
    lic = models.CharField(max_length=16, verbose_name='Libelle court')
    sesid = models.ForeignKey('Ses', models.DO_NOTHING, db_column='sesid', related_name='+', verbose_name='Session de depot')

    class Meta:
        managed = False
        db_table = 'fbu'


class GrppolAmeli(models.Model):
    entid = models.ForeignKey(Ent, models.DO_NOTHING, db_column='entid', primary_key=True, related_name='+', verbose_name='Identifiant')
    cod = models.CharField(max_length=12, verbose_name='Code')
    libcou = models.CharField(max_length=80, verbose_name='Libelle courant')
    lilcou = models.CharField(max_length=255, verbose_name='Libelle long courant')
    codint = models.CharField(max_length=60, verbose_name='Code interne')
    tri = models.BigIntegerField(blank=True, null=True, verbose_name='Ordre de presentation dans les listes')

    class Meta:
        managed = False
        db_table = 'grppol_ameli'


class Gvt(models.Model):
    entid = models.ForeignKey(Ent, models.DO_NOTHING, db_column='entid', primary_key=True, related_name='+', verbose_name='Identifiant')
    nom = models.CharField(max_length=64, verbose_name='Nom')
    pre = models.CharField(max_length=64, verbose_name='Prenom')
    qua = models.CharField(max_length=12, verbose_name='Qualite')
    tit = models.CharField(max_length=256, verbose_name='Titre')

    class Meta:
        managed = False
        db_table = 'gvt'


class Intora(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Identifiant')
    subid = models.ForeignKey('Sub', models.DO_NOTHING, db_column='subid', blank=True, null=True, related_name='+', verbose_name='Identifiant de la subdivision sur laquelle porte la prise de parole')
    entid = models.ForeignKey(Ent, models.DO_NOTHING, db_column='entid', related_name='+', verbose_name="Identifiant de l'orateur")
    entid2 = models.ForeignKey(Ent, models.DO_NOTHING, db_column='entid2', blank=True, null=True, related_name='+', verbose_name="Identifiant de l'orateur (au nom de)")
    txtid = models.ForeignKey('TxtAmeli', models.DO_NOTHING, db_column='txtid', related_name='+', verbose_name='Identifiant du texte')
    seaid = models.ForeignKey('Sea', models.DO_NOTHING, db_column='seaid', blank=True, null=True, related_name='+', verbose_name='Identifiant de la seance')
    mom = models.CharField(max_length=1, verbose_name="Moment de l'intervention")
    ord = models.BigIntegerField(verbose_name="Numero d'ordre")
    rolcod = models.ForeignKey('Orarol', models.DO_NOTHING, db_column='rolcod', related_name='+', verbose_name="Code du role de l'orateur")
    temps = models.IntegerField(verbose_name="Duree de l'intevrention")

    class Meta:
        managed = False
        db_table = 'intora'


class Irr(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Identifiant')
    lib = models.CharField(max_length=255, verbose_name='Libelle')
    cod = models.CharField(max_length=4, verbose_name='Code')
    libirr = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libelle')
    art = models.CharField(max_length=32, blank=True, null=True, verbose_name='Article')
    lilmin = models.CharField(max_length=512, blank=True, null=True, verbose_name='Libelle long')
    par = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'irr'


class LecAmeli(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Identifiant')
    lib = models.CharField(max_length=80, verbose_name='Libelle')
    lecpreid = models.ForeignKey('self', models.DO_NOTHING, db_column='lecpreid', blank=True, null=True, related_name='+', verbose_name='Lecture precedente')

    class Meta:
        managed = False
        db_table = 'lec_ameli'


class Mot(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Identifiant')
    lib = models.CharField(max_length=255, verbose_name='Libelle')
    int = models.CharField(max_length=255, blank=True, null=True, verbose_name='Intitule')
    cod = models.CharField(max_length=8, blank=True, null=True, verbose_name='Code')
    ord = models.BigIntegerField(verbose_name='Ordre de presentation')
    libnbe = models.CharField(max_length=512, blank=True, null=True, verbose_name='Libelle pour le nota bene')

    class Meta:
        managed = False
        db_table = 'mot'


class Nat(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Identifiant')
    lib = models.CharField(max_length=80, verbose_name='Libelle')

    class Meta:
        managed = False
        db_table = 'nat'


class Orarol(models.Model):
    cod = models.CharField(primary_key=True, max_length=10, verbose_name='Code')
    lib = models.CharField(max_length=128, blank=True, null=True, verbose_name='Libelle')
    entreq = models.CharField(max_length=1, verbose_name="Indique si le role doit etre complete par le libelle de l'entite d'appartenance de l'orateur")

    class Meta:
        managed = False
        db_table = 'orarol'


class Sai(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Identifiant')
    txtid = models.ForeignKey('TxtAmeli', models.DO_NOTHING, db_column='txtid', related_name='+', verbose_name='Identifiant du texte')
    comid = models.ForeignKey(ComAmeli, models.DO_NOTHING, db_column='comid', related_name='+', verbose_name='Identifiant de la commission')
    sesid = models.ForeignKey('Ses', models.DO_NOTHING, db_column='sesid', related_name='+', verbose_name='Identifiant de la session')
    numrap = models.BigIntegerField(blank=True, null=True, verbose_name="Numero de rapport (ou d'avis)")
    saityp = models.CharField(max_length=1, verbose_name='Type de saisine')
    isdelegfond = models.CharField(max_length=1, verbose_name='Indique si la commission saisie pour avis est déléguée au fond')

    class Meta:
        managed = False
        db_table = 'sai'


class Saisen(models.Model):
    id = models.ForeignKey(Sai, models.DO_NOTHING, db_column='id', primary_key=True, related_name='+', verbose_name='Identifiant')
    senid = models.ForeignKey('SenAmeli', models.DO_NOTHING, db_column='senid', related_name='+', verbose_name='Identifiant du senateur')
    ord = models.BigIntegerField(verbose_name='Ordre')

    class Meta:
        managed = False
        db_table = 'saisen'
        unique_together = (('id', 'senid'),)


class Sea(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Identifiant')
    sesid = models.ForeignKey('Ses', models.DO_NOTHING, db_column='sesid', related_name='+', verbose_name='Identifiant de la session')
    dat = models.DateTimeField(blank=True, null=True, verbose_name='Date de la seance')
    num = models.BigIntegerField(blank=True, null=True, verbose_name='Numero de la seance')

    class Meta:
        managed = False
        db_table = 'sea'


class SenAmeli(models.Model):
    entid = models.ForeignKey(Ent, models.DO_NOTHING, db_column='entid', primary_key=True, related_name='+', verbose_name='Identifiant')
    grpid = models.ForeignKey(GrppolAmeli, models.DO_NOTHING, db_column='grpid', related_name='+', verbose_name='Identifiant du groupe')
    comid = models.ForeignKey(ComAmeli, models.DO_NOTHING, db_column='comid', blank=True, null=True, related_name='+', verbose_name='Identifiant de la commission')
    comspcid = models.ForeignKey(ComAmeli, models.DO_NOTHING, db_column='comspcid', blank=True, null=True, related_name='+', verbose_name='Identifiant de la commission speciale')
    mat = models.CharField(max_length=6, verbose_name='Matricule')
    qua = models.CharField(max_length=12, verbose_name='Qualite')
    nomuse = models.CharField(max_length=64, verbose_name='Nom usuel')
    prenomuse = models.CharField(max_length=64, verbose_name='Prenom usuel')
    nomtec = models.CharField(max_length=64, blank=True, null=True, verbose_name='Nom technique')
    hom = models.CharField(max_length=1, blank=True, null=True, verbose_name='Indication de senateurs homonymes')
    app = models.CharField(max_length=1, blank=True, null=True, verbose_name='Indication de senateurs apparentes')
    ratt = models.CharField(max_length=1, blank=True, null=True, verbose_name='Indication de senateurs rattache a un groupe')
    nomusemin = models.CharField(max_length=64, verbose_name='Nom usuel en minuscule')
    senfem = models.CharField(max_length=1, blank=True, null=True, verbose_name='Indication de feminisation des titres')

    class Meta:
        managed = False
        db_table = 'sen_ameli'


class Ses(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Identifiant')
    typid = models.ForeignKey('Typses', models.DO_NOTHING, db_column='typid', related_name='+', verbose_name='Type de session')
    ann = models.BigIntegerField(verbose_name='Annee de session')
    lil = models.CharField(max_length=255, verbose_name='Libelle long')

    class Meta:
        managed = False
        db_table = 'ses'


class Sor(models.Model):
    id = models.CharField(primary_key=True, max_length=1, verbose_name='Identifiant')
    lib = models.CharField(max_length=80, verbose_name='Libelle')
    cod = models.CharField(max_length=4, verbose_name='Code')
    typ = models.CharField(max_length=1, verbose_name='Type')

    class Meta:
        managed = False
        db_table = 'sor'


class Sub(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Identifiant')
    txtid = models.ForeignKey('TxtAmeli', models.DO_NOTHING, db_column='txtid', related_name='+', verbose_name='Identifiant du texte')
    merid = models.ForeignKey('self', models.DO_NOTHING, db_column='merid', blank=True, null=True, related_name='+', verbose_name='Identifiant de la subdivision mere')
    typid = models.ForeignKey('Typsub', models.DO_NOTHING, db_column='typid', blank=True, null=True, related_name='+', verbose_name='Type')
    lic = models.CharField(max_length=32, blank=True, null=True, verbose_name='Libelle court')
    lib = models.CharField(max_length=512, blank=True, null=True, verbose_name='Libelle long')
    pos = models.BigIntegerField(blank=True, null=True, verbose_name='Position dans le texte')
    sig = models.CharField(max_length=1024, blank=True, null=True, verbose_name='Nom du signet')
    posder = models.BigIntegerField(blank=True, null=True, verbose_name='Position dans la discussion')
    prires = models.BigIntegerField(blank=True, null=True, verbose_name='Indicateur de subdivision mise en reserve ou discutee en priorite')
    dupl = models.CharField(max_length=1, verbose_name='Indicateur de subdivision dupliquee')
    subamd = models.CharField(max_length=1, verbose_name='Indicateur de subdivision amendable')
    sorid = models.CharField(max_length=1, blank=True, null=True)
    txtidder = models.IntegerField(blank=True, null=True, verbose_name='ID du dérouleur texte')
    style = models.CharField(max_length=10, verbose_name='Style daffichage dans le dérouleur')
    islec = models.CharField(max_length=1, verbose_name='Indique si la subdivision est soumise au LEC')
    comdelid = models.ForeignKey(ComAmeli, models.DO_NOTHING, db_column='comdelid', blank=True, null=True, related_name='+', verbose_name='Id de la commission pour avis avec délégation au fond')

    class Meta:
        managed = False
        db_table = 'sub'


class TxtAmeli(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Identifiant')
    natid = models.ForeignKey(Nat, models.DO_NOTHING, db_column='natid', related_name='+', verbose_name='Identifiant de la nature du texte')
    lecid = models.ForeignKey(LecAmeli, models.DO_NOTHING, db_column='lecid', related_name='+', verbose_name='Identifiant de lecture')
    sesinsid = models.ForeignKey(Ses, models.DO_NOTHING, db_column='sesinsid', blank=True, null=True, related_name='+', verbose_name="Identifiant de la session d'inscription")
    sesdepid = models.ForeignKey(Ses, models.DO_NOTHING, db_column='sesdepid', related_name='+', verbose_name='Identifiant de la session de depot')
    fbuid = models.ForeignKey(Fbu, models.DO_NOTHING, db_column='fbuid', blank=True, null=True, related_name='+', verbose_name='Identifiant de la mission (si texte de la loi de finance)')
    num = models.CharField(max_length=32, verbose_name='Numero du texte')
    int = models.CharField(max_length=80, verbose_name='Intitule du texte')
    inl = models.CharField(max_length=720, blank=True, null=True, verbose_name='Intitule long du texte')
    datdep = models.DateTimeField(verbose_name='Date de depot')
    urg = models.CharField(max_length=1, verbose_name='Urgence (avant la revision constitutionnelle de 2008)')
    dis = models.CharField(max_length=1, verbose_name='Indicateur de texte disponible')
    secdel = models.CharField(max_length=1, verbose_name='Indicateur de texte en seconde deliberation')
    loifin = models.CharField(max_length=1, verbose_name='Texte du projet de loi de finance')
    loifinpar = models.BigIntegerField(blank=True, null=True, verbose_name='Indicateur de la partie du projet de loi de finance')
    txtamd = models.CharField(max_length=1, verbose_name='Indicateur de texte amendable')
    datado = models.DateTimeField(blank=True, null=True, verbose_name="Date d'adoption du texte")
    numado = models.BigIntegerField(blank=True, null=True, verbose_name="Numero d'adoption du texte")
    txtexa = models.CharField(max_length=1, blank=True, null=True, verbose_name='Indicateur de texte examine')
    pubdellim = models.DateTimeField(blank=True, null=True, verbose_name='Publication du delai limite')
    numabs = models.IntegerField(blank=True, null=True, verbose_name='Numero du texte (en chiffre)')
    libdelim = models.CharField(max_length=512, blank=True, null=True, verbose_name='Libelle du delai limite')
    libcplnat = models.CharField(max_length=256, blank=True, null=True, verbose_name='Libelle complementaire de la nature du texte')
    doslegsignet = models.CharField(max_length=48, blank=True, null=True, verbose_name='Signet du dossier legislatif')
    proacc = models.CharField(max_length=1, verbose_name='Procedure acceleree (depuis la reforme constitutionnelle de 2008)')
    txttyp = models.CharField(max_length=1, verbose_name='Type du texte')
    ordsnddelib = models.CharField(max_length=5, blank=True, null=True, verbose_name='Ordre de la seconde deliberation')
    txtetaid = models.ForeignKey(Etatxt, models.DO_NOTHING, db_column='txtetaid', related_name='+', verbose_name="Identifiant de l'etat du texte")
    fusderid = models.ForeignKey('self', models.DO_NOTHING, db_column='fusderid', blank=True, null=True, related_name='+', verbose_name='ID du dérouleur fusionné')
    fusder = models.CharField(max_length=1, verbose_name='O sil sagit dun  dérouleur fusionné, N sinon')
    fusderord = models.IntegerField(verbose_name='Ordre de discussion des textes dans un dérouleur fusionné')
    fusdertyp = models.CharField(max_length=2, blank=True, null=True, verbose_name='Type de fusion dérouleur DG ou DA')

    class Meta:
        managed = False
        db_table = 'txt_ameli'


class Typrect(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Identifiant')
    lib = models.CharField(max_length=120, verbose_name='Libelle')
    ord = models.BigIntegerField(verbose_name='Ordre')

    class Meta:
        managed = False
        db_table = 'typrect'


class Typses(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Identifiant')
    lib = models.CharField(max_length=64, blank=True, null=True, verbose_name='Libelle')

    class Meta:
        managed = False
        db_table = 'typses'


class Typsub(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name='Identifiant')
    lib = models.CharField(max_length=32, verbose_name='Libelle')

    class Meta:
        managed = False
        db_table = 'typsub'


class WNivrec(models.Model):
    num = models.BigIntegerField(primary_key=True, verbose_name='Numero')
    lib = models.CharField(max_length=32, blank=True, null=True, verbose_name='Libelle')

    class Meta:
        managed = False
        db_table = 'w_nivrec'

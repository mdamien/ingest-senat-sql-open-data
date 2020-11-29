# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Amescr(models.Model):
    sesann = models.BigIntegerField(verbose_name='Avec scrnum, clé étrangère vers la table scr (scrutin) - élément de la clé de la table')
    scrnum = models.BigIntegerField(verbose_name='Avec sesann, clé étrangère vers la table scr (numéro de scrutin) - élément de la clé de la table')
    amescrnum = models.CharField(max_length=20, verbose_name="Numéro d'amendement")

    class Meta:
        managed = False
        db_table = 'amescr'


class Ass(models.Model):
    codass = models.CharField(primary_key=True, max_length=1, verbose_name='Clé de la table')
    libass = models.CharField(max_length=40, verbose_name='Libellé')

    class Meta:
        managed = False
        db_table = 'ass'


class Aud(models.Model):
    audcle = models.BigIntegerField(primary_key=True, verbose_name='Clé de la table')
    lecassidt = models.CharField(max_length=15, verbose_name='Clé étrangère var lecass (lecture)')
    auddat = models.DateTimeField(verbose_name='Date de la réunion')
    audtit = models.CharField(max_length=1023)
    audurl = models.CharField(max_length=254, verbose_name='URL du compte rendu de commission')
    orgcod = models.CharField(max_length=4, verbose_name='Clé étrangère vers org (commission)')

    class Meta:
        managed = False
        db_table = 'aud'


class Auteur(models.Model):
    autcod = models.CharField(primary_key=True, max_length=6, verbose_name='Clé de la table')
    quacod = models.CharField(max_length=2, verbose_name='Clé étrangère vers qua (civilité)')
    typautcod = models.CharField(max_length=3, verbose_name="Clé étrangère vers typaut (type de l'auteur)")
    nomuse = models.CharField(max_length=254, verbose_name='Nom usuel')
    prenom = models.CharField(max_length=36, blank=True, null=True, verbose_name='Prenoms')
    nomtec = models.CharField(max_length=254, verbose_name='Nom technique utilisé pour les classements par noms')
    autmat = models.CharField(max_length=12, blank=True, null=True, verbose_name='Lien vers la base Sénateurs')
    grpapp = models.CharField(max_length=1, blank=True, null=True, verbose_name='Pour les groupes : contient les apparentés')
    grprat = models.CharField(max_length=1, blank=True, null=True, verbose_name='Pour les groupes : contient les rattachés')
    autfct = models.CharField(max_length=254, blank=True, null=True, verbose_name="Fonction de l'auteur")
    datdeb = models.DateTimeField(blank=True, null=True, verbose_name='Début de validité')
    datfin = models.DateTimeField(blank=True, null=True, verbose_name='Fin de validité')
    senfem = models.CharField(max_length=3, blank=True, null=True, verbose_name='OUI pour les sénatrices ayant demandé la féminisation de leurs fonctions')

    class Meta:
        managed = False
        db_table = 'auteur'


class Ble(models.Model):
    blecod = models.CharField(primary_key=True, max_length=5, verbose_name='Clé de la table')
    blelib = models.CharField(max_length=80, verbose_name='Libellé')

    class Meta:
        managed = False
        db_table = 'ble'


class Bur(models.Model):
    burcod = models.CharField(primary_key=True, max_length=12, verbose_name='Code bureau 4e Rép.')
    burlib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    burlic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    burnumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    burlil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    burlibhon = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé honorariat')
    burlicfem = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court féminin')
    burlibfem = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé féminin')
    burlilfem = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long féminin')
    burlicplu = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court pluriel')
    burlibplu = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé pluriel')
    burlilplu = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long pluriel')
    burlibhonfem = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé honorariat féminin')
    burlibhonplu = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé honorariat pluriel')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')
    burlicfemplu = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court féminin pluriel')
    burlibfemplu = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé féminin pluriel')
    burlilfemplu = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long féminin pluriel')

    class Meta:
        managed = False
        db_table = 'bur'


class Catrap(models.Model):
    catrapcod = models.CharField(primary_key=True, max_length=1, verbose_name='Clé de la table')
    catraplib = models.CharField(max_length=60, verbose_name='Libellé')

    class Meta:
        managed = False
        db_table = 'catrap'


class Com(models.Model):
    typorgcod = models.ForeignKey('TyporgSen', models.DO_NOTHING, db_column='typorgcod', related_name='+', verbose_name='Code type organisme')
    orgcod = models.CharField(primary_key=True, max_length=12, verbose_name='Code organisme')
    orgnumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    orgdatcre = models.DateTimeField(blank=True, null=True, verbose_name='Date création')
    orgdatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    orgnumtie = models.CharField(max_length=12, blank=True, null=True, verbose_name='NuméroTiers')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=500, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=500, blank=True, null=True, verbose_name='Observations')
    orgart = models.CharField(max_length=60, blank=True, null=True, verbose_name='Article')
    comlilmin = models.CharField(max_length=500, blank=True, null=True, verbose_name='Libellé long minuscule')
    orgurlsim = models.CharField(max_length=500, blank=True, null=True, verbose_name='URL simplifié')
    orgurlcmp = models.CharField(max_length=500, blank=True, null=True, verbose_name='URL complet')
    comlibameli = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé AMELI')
    comcodameli = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code transfert AMELI')
    divcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code division')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'com'


class Corscr(models.Model):
    sesann = models.BigIntegerField(verbose_name='Avec scrnum, clé étrangère vers la table scr (scrutin) - élément de la clé de la table')
    scrnum = models.BigIntegerField(verbose_name='Avec sesann, clé étrangère vers la table scr (numéro de scrutin) - élément de la clé de la table')
    corscrord = models.BigIntegerField(blank=True, null=True, verbose_name='Tri des mises au points pour un scrutin donné')
    corscrtxt = models.CharField(max_length=4000, verbose_name='Texte de la mise au point')
    corscrurl = models.CharField(max_length=254, blank=True, null=True, verbose_name='URL du CR de la séance publique correspondante')

    class Meta:
        managed = False
        db_table = 'corscr'


class DateSeance(models.Model):
    lecidt = models.CharField(max_length=15, blank=True, null=True, verbose_name='Devrait etre lecassidt')
    date_s = models.DateTimeField(blank=True, null=True, verbose_name='Date de séance publique')
    code = models.BigIntegerField(primary_key=True, verbose_name='Clé de la table')
    statut = models.CharField(max_length=5, blank=True, null=True, verbose_name='statut spécial : EVENT')

    class Meta:
        managed = False
        db_table = 'date_seance'


class Debats(models.Model):
    datsea = models.DateTimeField(primary_key=True, verbose_name='Date de la séance (clé)')
    debsyn = models.CharField(max_length=1, blank=True, null=True, verbose_name='Clé étrangère vers syndeb (état de synchronisation des données)')
    autinc = models.CharField(max_length=1, blank=True, null=True, verbose_name="à O pour signaler la présence d'intervenants non reconnnus")
    deburl = models.CharField(max_length=80, blank=True, null=True, verbose_name='URL du compte rendu')
    numero = models.BigIntegerField(blank=True, null=True, verbose_name='numéro de la séance')
    estcongres = models.CharField(max_length=1, blank=True, null=True, verbose_name='à oui pour un CR de congrès')
    libspec = models.CharField(max_length=256, blank=True, null=True, verbose_name='Libellé pour un débat spécial')
    etavidcod = models.CharField(max_length=1, blank=True, null=True, verbose_name="Code de l'état d'envoi à la vidéo C=CRI, A=Archive")

    class Meta:
        managed = False
        db_table = 'debats'


class Deccoc(models.Model):
    deccoccod = models.CharField(primary_key=True, max_length=3, verbose_name='Clé de la table')
    deccoclib = models.CharField(max_length=40, verbose_name='Libellé')

    class Meta:
        managed = False
        db_table = 'deccoc'


class Delega(models.Model):
    typorgcod = models.ForeignKey('TyporgSen', models.DO_NOTHING, db_column='typorgcod', related_name='+', verbose_name='Code type organisme')
    orgcod = models.CharField(primary_key=True, max_length=12, verbose_name='Code organisme')
    orgnumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    orgdatcre = models.DateTimeField(blank=True, null=True, verbose_name='Date création')
    orgdatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    orgnumtie = models.CharField(max_length=12, blank=True, null=True, verbose_name='NuméroTiers')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    orgart = models.CharField(max_length=60, blank=True, null=True, verbose_name='Article')
    orgurlsim = models.CharField(max_length=255, blank=True, null=True, verbose_name='URL simplifié')
    orgurlcmp = models.CharField(max_length=255, blank=True, null=True, verbose_name='URL complet')
    orgregjur = models.CharField(max_length=255, blank=True, null=True, verbose_name='Régime juridique')
    orgmoddes = models.CharField(max_length=255, blank=True, null=True, verbose_name='Mode désignation')
    orgmemdep = models.CharField(max_length=12, blank=True, null=True, verbose_name='Membres Députés')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'delega'


class Denrap(models.Model):
    coddenrap = models.CharField(primary_key=True, max_length=5, verbose_name='Clef')
    typraprap = models.CharField(max_length=5, verbose_name='Type de rapport')
    libdenrap = models.CharField(max_length=128, verbose_name='Libellé')
    ordre = models.BigIntegerField(blank=True, null=True, verbose_name='Ordre dans une liste de type')
    denrapmin = models.CharField(max_length=80, blank=True, null=True, verbose_name='Miniature')
    denraptit = models.CharField(max_length=128, blank=True, null=True, verbose_name='Titre de rubrique pour ce type de rapport')
    denrapstymin = models.CharField(max_length=40, blank=True, null=True, verbose_name='Style de miniature')
    gencod = models.CharField(max_length=1, verbose_name='clé étrangère vers gen (genre)')
    solnatrapcod = models.CharField(max_length=2, blank=True, null=True, verbose_name='Cle de SOLNATRAP')

    class Meta:
        managed = False
        db_table = 'denrap'


class Designorg(models.Model):
    designcod = models.CharField(primary_key=True, max_length=12, verbose_name='Code désignataire')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    designnumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    designlib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    designlic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    designlil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    designlibfem = models.CharField(max_length=120, blank=True, null=True, verbose_name='Lbellé féminin')
    designlicfem = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé féminin court')
    designlilfem = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé féminin long')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'designorg'


class Doc(models.Model):
    docidt = models.BigIntegerField(primary_key=True, verbose_name='Clé de la table')
    typdoccod = models.ForeignKey('Typdoc', models.DO_NOTHING, db_column='typdoccod', blank=True, null=True, related_name='+', verbose_name='Type du document')
    docint = models.CharField(max_length=255, blank=True, null=True, verbose_name='Titre long du document')
    docurl = models.CharField(max_length=255, blank=True, null=True, verbose_name='URL du document')
    lecidt = models.ForeignKey('Lecture', models.DO_NOTHING, db_column='lecidt', blank=True, null=True, related_name='+', verbose_name='Numéro de lecture (décrets...)')
    docdat = models.DateTimeField(blank=True, null=True, verbose_name='date du document')
    docnum = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de dépôt (documents déposés)')
    sesann = models.ForeignKey('Ses', models.DO_NOTHING, db_column='sesann', blank=True, null=True, related_name='+', verbose_name='Session de dépôt  (documents déposés)')
    date_depot = models.DateTimeField(blank=True, null=True, verbose_name='Date de dépôt (documents déposés)')
    doctitcou = models.CharField(max_length=254, blank=True, null=True, verbose_name='Titre court du document')
    docdatsea = models.DateTimeField(blank=True, null=True, verbose_name='Date de séance de rattachement')

    class Meta:
        managed = False
        db_table = 'doc'


class Docatt(models.Model):
    docattcle = models.BigIntegerField(primary_key=True, verbose_name='Clé de la table')
    rapcod = models.BigIntegerField(verbose_name='Clé étrangère vers rap (rapport)')
    typattcod = models.CharField(max_length=1, verbose_name='Clé étrangère vers typattcod (type du document attaché)')
    docatturl = models.CharField(max_length=120, blank=True, null=True, verbose_name='URL du document attaché')

    class Meta:
        managed = False
        db_table = 'docatt'


class Docsea(models.Model):
    evtseacle = models.BigIntegerField(verbose_name='Clé étrangère vers evtsea (événement de séance)')
    docseaurl = models.CharField(max_length=160, blank=True, null=True, verbose_name='URL du document')
    docseaurltxt = models.CharField(max_length=80, blank=True, null=True, verbose_name="Texte associé à l'URL")
    docseaurlava = models.CharField(max_length=80, blank=True, null=True, verbose_name='Texte apparaissant avant URL')
    docseaurlapr = models.CharField(max_length=80, blank=True, null=True, verbose_name='Texte apparaissant après URL')
    docseaord = models.BigIntegerField(blank=True, null=True, verbose_name="Ordre du document pour l'événement de séance")

    class Meta:
        managed = False
        db_table = 'docsea'


class Dpt(models.Model):
    dptnum = models.BigIntegerField(primary_key=True, verbose_name='Identifiant circonscription')
    dptcod = models.CharField(max_length=12, verbose_name='Code INSEE')
    dptlib = models.CharField(max_length=120, verbose_name='Libellé')
    dptnbrsen = models.BigIntegerField(blank=True, null=True, verbose_name='Nombre sénateurs')
    dptmodscrsen = models.CharField(max_length=12, blank=True, null=True, verbose_name='Mode scrutin sénatorial')
    dptser = models.CharField(max_length=1, verbose_name='Série (A,B,C)')
    regcod = models.CharField(max_length=12, verbose_name='Code région')
    dptnumtri = models.BigIntegerField(verbose_name='Numéro de tri')
    dptlic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    dptart = models.CharField(max_length=60, blank=True, null=True, verbose_name='Article')
    dptlibtri = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé Moyen')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    dptser2004 = models.CharField(max_length=1, blank=True, null=True, verbose_name='Série (1,2)')
    dptcmt = models.CharField(max_length=255, blank=True, null=True, verbose_name='Commentaire listes')
    dptdatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date de début')
    dptdatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    evetempub = models.CharField(max_length=12, blank=True, null=True, verbose_name='Témoin publication')
    dpturlcmp = models.CharField(max_length=255, blank=True, null=True, verbose_name='URL')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'dpt'


class Dptele(models.Model):
    dptnum = models.ForeignKey(Dpt, models.DO_NOTHING, db_column='dptnum', related_name='+', verbose_name='Identifiant circonscription')
    dptelenbrsie = models.BigIntegerField(blank=True, null=True, verbose_name='Nombre de sièges')
    dpteleid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    typelecod = models.CharField(max_length=12, verbose_name='Code type élection')
    validcod = models.CharField(max_length=32, verbose_name='Code validation')
    valid2cod = models.CharField(max_length=32, verbose_name='Code validation')
    participaidt1 = models.BigIntegerField(blank=True, null=True, verbose_name='Identifiant participation')
    participaidt2 = models.BigIntegerField(blank=True, null=True, verbose_name='Identifiant participation')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')
    eleid = models.BigIntegerField(verbose_name='Identifiant')
    dptelenbrsiepvr = models.BigIntegerField(blank=True, null=True)
    dptelecmt = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dptele'


class Ecr(models.Model):
    rapcod = models.BigIntegerField(blank=True, null=True, verbose_name='Clé étrangère vers rap (rapport)')
    ecrnumtri = models.BigIntegerField(verbose_name="Position de l'auteur dans la liste des auteurs du document")
    autcod = models.CharField(max_length=6, blank=True, null=True, verbose_name='Clé étrangère vers auteur')
    texcod = models.BigIntegerField(blank=True, null=True, verbose_name='Clé étrangère vers le texte')
    ecrnum = models.BigIntegerField(primary_key=True, verbose_name='Clé de la table')
    typedoc = models.CharField(max_length=1, blank=True, null=True, verbose_name='T=texte; R=rapport, D=document')
    signataire = models.CharField(max_length=1, blank=True, null=True, verbose_name='Clé étrangère vers rolsig (rôle du signataire)')
    docidt = models.BigIntegerField(blank=True, null=True, verbose_name='Clé étrangère vers doc (document)')
    ecrqua = models.CharField(max_length=255, blank=True, null=True, verbose_name="Qualité de l'auteur pour un document donné")

    class Meta:
        managed = False
        db_table = 'ecr'


class Elusen(models.Model):
    eluid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    dptnum = models.ForeignKey(Dpt, models.DO_NOTHING, db_column='dptnum', related_name='+', verbose_name='Identifiant circonscription')
    eludatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date début mandat')
    eludatelu = models.DateTimeField(blank=True, null=True, verbose_name="Date d'élection")
    eludatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date fin mandat')
    etadebmancod = models.ForeignKey('Etadebman', models.DO_NOTHING, db_column='etadebmancod', related_name='+', verbose_name='Code début de mandat')
    etafinmancod = models.ForeignKey('Etafinman', models.DO_NOTHING, db_column='etafinmancod', blank=True, null=True, related_name='+', verbose_name='Code état fin de mandat')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eluanndeb = models.BigIntegerField(blank=True, null=True, verbose_name='Année début mandat')
    eluannfin = models.BigIntegerField(blank=True, null=True, verbose_name='Année fin mandat')
    typmancod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code type mandat')
    senmat = models.ForeignKey('Sen', models.DO_NOTHING, db_column='senmat', related_name='+', verbose_name='Matricule')
    eludatcum = models.DateTimeField(blank=True, null=True, verbose_name='Date cumul')
    turelucod = models.CharField(max_length=12, verbose_name='Code tour élection')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'elusen'


class Etadebman(models.Model):
    etadebmancod = models.CharField(primary_key=True, max_length=12, verbose_name='Code début de mandat')
    etadebmanlic = models.CharField(max_length=60, verbose_name='Libellé court')
    etadebmanlib = models.CharField(max_length=120, verbose_name='Libellé')
    etadebmannumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    etadebmanlil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    etadebmanlicfem = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé court féminin')
    etadebmanlibfem = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé féminin')
    etadebmanlilfem = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long féminin')
    etadebmanlicplu = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court pluriel')
    etadebmanlibplu = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé pluriel')
    etadebmanlilplu = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long pluriel')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'etadebman'


class Etafinman(models.Model):
    etafinmancod = models.CharField(primary_key=True, max_length=12, verbose_name='Code état fin de mandat')
    etafinmanlic = models.CharField(max_length=60, verbose_name='Libellé court')
    etafinman = models.CharField(max_length=120, verbose_name='Libellé')
    etafinmannumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    etafinmantemsirpas = models.CharField(max_length=12, blank=True, null=True)
    etafinmancodsirpas = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code transfert GESTION')
    etafinmanlil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    etafinmanlicfem = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court féminin')
    etafinmanlibfem = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé féminin')
    etafinmanlilfem = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long féminin')
    etafinmanlicplu = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libelle court pluriel')
    etafinmanlibplu = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé pluriel')
    etafinmanlilplu = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long pluriel')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'etafinman'


class Etaloi(models.Model):
    etaloicod = models.CharField(primary_key=True, max_length=2, verbose_name='Clé de la table')
    etaloilib = models.CharField(max_length=36, verbose_name='Libellé')

    class Meta:
        managed = False
        db_table = 'etaloi'


class Etasen(models.Model):
    etasencod = models.CharField(primary_key=True, max_length=12, verbose_name='Code état sénateur')
    etasenlic = models.CharField(max_length=60, verbose_name='Libellé court')
    etasenlib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    etasennumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    etasenlil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    etasenlicfem = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court féminin')
    etasenlibfem = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé féminin')
    etasenlilfem = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long féminin')
    etasenlicplu = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libelle court pluriel')
    etasenlibplu = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé pluriel')
    etasenlilplu = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long pluriel')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'etasen'


class Evtsea(models.Model):
    evtseacle = models.BigIntegerField(primary_key=True, verbose_name='Clé de la table')
    loicod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Clé étrangère vers loi (dossier de la motion)')
    typevtcod = models.CharField(max_length=3, verbose_name="Clé étrangère vers typevtsea (type d'événements)")
    lecassidt = models.CharField(max_length=15, verbose_name='Clé étrangère vers lecass (lecture)')
    evtseadat = models.DateTimeField(blank=True, null=True, verbose_name="Date de l'événement")

    class Meta:
        managed = False
        db_table = 'evtsea'


class Foncom(models.Model):
    foncomcod = models.CharField(primary_key=True, max_length=12, verbose_name='Code fonction commission')
    foncomlib = models.CharField(max_length=120, verbose_name='Libellé')
    foncomlic = models.CharField(max_length=60, verbose_name='Libellé court')
    foncomnumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    foncomlil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    foncomlicfem = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court féminin')
    foncomlibfem = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé féminin')
    foncomlilfem = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long féminin')
    foncomlicplu = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court pluriel')
    foncomlibplu = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé pluriel')
    foncomlilplu = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long pluriel')
    foncomlicfemplu = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court féminin pluriel')
    foncomlibfemplu = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé féminin pluriel')
    foncomlilfemplu = models.CharField(max_length=500, blank=True, null=True, verbose_name='Libellé long féminin pluriel')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'foncom'


class Fondelega(models.Model):
    fondelcod = models.CharField(primary_key=True, max_length=12, verbose_name='Code fonction délégation')
    fondellib = models.CharField(max_length=120, verbose_name='Libellé')
    fondellic = models.CharField(max_length=60, verbose_name='Libellé court')
    fondelnumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    fondellil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    fondellicfem = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court féminin')
    fondellibfem = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé  féminin')
    fondellilfem = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long féminin')
    fondellicplu = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libelle court pluriel')
    fondellibplu = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé pluriel')
    fondellilplu = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long pluriel')
    fondellicfemplu = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court féminin pluriel')
    fondellibfemplu = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé féminin pluriel')
    fondellilfemplu = models.CharField(max_length=500, blank=True, null=True, verbose_name='Libellé long féminin pluriel')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'fondelega'


class Fongrppol(models.Model):
    fongrppolcod = models.CharField(primary_key=True, max_length=12, verbose_name='Code fonction groupe politique')
    fongrppollib = models.CharField(max_length=120, verbose_name='Libellé')
    fongrppollic = models.CharField(max_length=60, verbose_name='Libellé court')
    fongrppolnumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    fongrppollil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    fongrppollibfem = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé féminin')
    fongrppollicfem = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court féminin')
    fongrppollilfem = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long féminin')
    fongrppollibplu = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé pluriel')
    fongrppollicplu = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court pluriel')
    fongrppollilplu = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long pluriel')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')
    fongrppollicfemplu = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court féminin pluriel')
    fongrppollibfemplu = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé féminin pluriel')
    fongrppollilfemplu = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long féminin pluriel')

    class Meta:
        managed = False
        db_table = 'fongrppol'


class Fonmemcom(models.Model):
    fonmemcomid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    foncomcod = models.ForeignKey(Foncom, models.DO_NOTHING, db_column='foncomcod', related_name='+', verbose_name='Code fonction commission')
    fonmemcomdatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date de début')
    fonmemcomdatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    fonmemcomrngprt = models.BigIntegerField(blank=True, null=True, verbose_name='Rang protocolaire')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    memcomid = models.ForeignKey('Memcom', models.DO_NOTHING, db_column='memcomid', related_name='+', verbose_name='Identifiant')
    evetempub = models.CharField(max_length=12, blank=True, null=True, verbose_name='Témoin publication')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'fonmemcom'


class Fonmemdelega(models.Model):
    fonmemdelid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    fondelcod = models.ForeignKey(Fondelega, models.DO_NOTHING, db_column='fondelcod', related_name='+', verbose_name='Code fonction délégation')
    fonmemdeldatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date de début')
    fonmemdeldatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    memdelegaid = models.ForeignKey('Memdelega', models.DO_NOTHING, db_column='memdelegaid', related_name='+', verbose_name='Identifiant')
    fonmemdelrngele = models.BigIntegerField(blank=True, null=True, verbose_name='Rang élection')
    evetempub = models.CharField(max_length=12, blank=True, null=True, verbose_name='Témoin publication')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'fonmemdelega'


class Fonmemgrppol(models.Model):
    fonmemgrppolid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    fongrppolcod = models.ForeignKey(Fongrppol, models.DO_NOTHING, db_column='fongrppolcod', related_name='+', verbose_name='Code fonction groupe politique')
    fonmemgrppoldatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date de début')
    fonmemgrppoldatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=30, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    memgrppolid = models.ForeignKey('Memgrppol', models.DO_NOTHING, db_column='memgrppolid', related_name='+', verbose_name='Identifiant')
    evetempub = models.CharField(max_length=12, blank=True, null=True, verbose_name='Témoin publication')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'fonmemgrppol'


class Forpub(models.Model):
    forpubcod = models.CharField(primary_key=True, max_length=3, verbose_name='Clé de la table')
    forpublib = models.CharField(max_length=60, verbose_name='Libellé')

    class Meta:
        managed = False
        db_table = 'forpub'


class Gen(models.Model):
    gencod = models.CharField(max_length=1, verbose_name='Clé de la table')
    genlib = models.CharField(max_length=60, verbose_name='Libellé')

    class Meta:
        managed = False
        db_table = 'gen'


class Grppol(models.Model):
    grppolcod = models.CharField(primary_key=True, max_length=12, verbose_name='Code groupe politique 4e Rép.')
    grppolnumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    grppolpre = models.CharField(max_length=12, blank=True, null=True, verbose_name='A un président (ou un délégué)')
    grppoldatcre = models.DateTimeField(blank=True, null=True, verbose_name='Date création')
    grppoldatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    grppolliccou = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court courant')
    grppollibcou = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé courant')
    grppollilcou = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long courant')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    typorgcod = models.ForeignKey('TyporgSen', models.DO_NOTHING, db_column='typorgcod', related_name='+', verbose_name='Code type organisme')
    grppolart = models.CharField(max_length=60, blank=True, null=True, verbose_name='Article')
    grppolurlsim = models.CharField(max_length=255, blank=True, null=True, verbose_name='URL simplifiée (relative)')
    grppolurlcmp = models.CharField(max_length=255, blank=True, null=True, verbose_name='URL complète')
    grppolcodamelicou = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code transfert AMELI')
    evetempub = models.CharField(max_length=12, blank=True, null=True, verbose_name='Témoin publication')
    grppolcodscr = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code transfert SCRUTINS')
    grppolcodrepro = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code transfert REPROGRAPHIE')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'grppol'


class Intdivers(models.Model):
    intdiverscle = models.BigIntegerField(primary_key=True, verbose_name='Clé')
    autcod = models.CharField(max_length=6, verbose_name='Clé étrangère vers dosleg.auteur (intervenant)')
    secdiverscle = models.BigIntegerField(verbose_name='Clé étrangère vers secdivers (section de discussion)')
    intana = models.CharField(max_length=2048, blank=True, null=True, verbose_name='Analyse')
    intfon = models.CharField(max_length=254, blank=True, null=True, verbose_name="Fonction de l'intervenant")
    intdiversordid = models.BigIntegerField(blank=True, null=True, verbose_name="Identifiant de l'intervention (chronologiquement ordonné)")
    inturl = models.CharField(max_length=80, blank=True, null=True, verbose_name="URL de l'intervention")

    class Meta:
        managed = False
        db_table = 'intdivers'


class Intpjl(models.Model):
    intpjlcle = models.BigIntegerField(primary_key=True, verbose_name='Clé')
    autcod = models.CharField(max_length=6, verbose_name='Clé étrangère vers dosleg.auteur (intervenant)')
    secdiscle = models.BigIntegerField(verbose_name='Clé éntrangère vers secdis (section de discussion)')
    intana = models.CharField(max_length=2048, blank=True, null=True, verbose_name='Analyse')
    intfon = models.CharField(max_length=254, blank=True, null=True, verbose_name="Fonction de l'intervenant")
    inturl = models.CharField(max_length=80, blank=True, null=True, verbose_name="URL de l'intervention")
    intordid = models.BigIntegerField(blank=True, null=True, verbose_name="Identifiant de l'intervention (chronologiquement ordonné)")

    class Meta:
        managed = False
        db_table = 'intpjl'


class Lecass(models.Model):
    lecassidt = models.CharField(primary_key=True, max_length=15, verbose_name='Clé de la table')
    lecidt = models.CharField(max_length=15, verbose_name='Clé étrangère vers lecture')
    codass = models.CharField(max_length=1, verbose_name='Clé étrangère vers ass (assemblée parlementaire)')
    ordreass = models.BigIntegerField(verbose_name='Ordre dans la lecture')
    sesann = models.BigIntegerField(blank=True, null=True, verbose_name='Clé étrangère vers ses (session parlementaire de la petite loi)')
    ptlnum = models.SmallIntegerField(blank=True, null=True, verbose_name='Numéro de la petite loi')
    ptlurl = models.CharField(max_length=254, blank=True, null=True, verbose_name='URL de la petite loi')
    ptlnumcpl = models.CharField(max_length=40, blank=True, null=True, verbose_name='Complément au numéro de la petite loi')
    ptlnot = models.CharField(max_length=254, blank=True, null=True, verbose_name='Note concernant la petite loi')
    ptlurl2 = models.CharField(max_length=254, blank=True, null=True, verbose_name='URL de la 2ème partie de la petite loi')
    ptlnot2 = models.CharField(max_length=254, blank=True, null=True, verbose_name='Note concernant la 2ème partie de la petite loi')
    ptlurl3 = models.CharField(max_length=254, blank=True, null=True, verbose_name='URL de la 3ème partie de la petite loi')
    ptlnot3 = models.CharField(max_length=254, blank=True, null=True, verbose_name='Note concernant la 3ème partie de la petite loi')
    ptlnumcpl2 = models.CharField(max_length=40, blank=True, null=True, verbose_name='Complément au numéro de la 2ème partie de la petite loi')
    ptlnumcpl3 = models.CharField(max_length=40, blank=True, null=True, verbose_name='Complément au numéro de la 3ème partie de la petite loi')
    lecassame = models.CharField(max_length=60, blank=True, null=True, verbose_name='Nr de texte amendé pour la séance publique')
    lecassameses = models.SmallIntegerField(blank=True, null=True, verbose_name='Session de texte amendé pour la séance publique')
    orgcod = models.CharField(max_length=4, blank=True, null=True, verbose_name='Clé étrangère vers ORG (commission saisie au fond)')
    loiintmod = models.CharField(max_length=720, blank=True, null=True, verbose_name='Nouvel intitulé du texte')
    reucom = models.CharField(max_length=254, blank=True, null=True, verbose_name='Réunion de commission pour les PPRE')
    debatsurl = models.CharField(max_length=254, blank=True, null=True, verbose_name='URL si CR des débats manuel')
    depot_only = models.CharField(max_length=3, verbose_name='Si "oui", un texte est déposé mais le statut exact de la lecture (2e, CMP...) n\'est pas encore déterminé')
    lecassamedat = models.DateTimeField(blank=True, null=True, verbose_name='Date de publication des amendements pour la séance publique')
    lecassamecomdat = models.DateTimeField(blank=True, null=True, verbose_name='Date de publication des amendements pour le texte de commission')
    orippr = models.CharField(max_length=1, blank=True, null=True, verbose_name='Clé étrangère vers orippr.oripprcod (Origine de la PPRE)')
    libppr = models.CharField(max_length=254, blank=True, null=True, verbose_name='Libellé de la PPRE')
    sesppr = models.BigIntegerField(blank=True, null=True, verbose_name='Session parlementaire pour PPRE')
    ptlurlcom = models.CharField(max_length=254, blank=True, null=True, verbose_name='URL de la petite loi de commission')
    aliasppr = models.CharField(max_length=254, blank=True, null=True, verbose_name='Alias pour PPRE')
    lecassamecom = models.CharField(max_length=60, blank=True, null=True, verbose_name="Nr de texte amendé pour l'élaboration du texte de commission")
    lecassamesescom = models.SmallIntegerField(blank=True, null=True, verbose_name="Session de texte amendé pour l'élaboration du texte de commission")
    ptlnumcom = models.SmallIntegerField(blank=True, null=True, verbose_name='Numéro de la petite loi de commission')

    class Meta:
        managed = False
        db_table = 'lecass'


class Lecassdeb(models.Model):
    lecassidt = models.CharField(primary_key=True, max_length=15, verbose_name='Clé étrangère vers dosleg.lecass (lecture)')
    datsea = models.DateTimeField(verbose_name='Clé étrangère vers débats')

    class Meta:
        managed = False
        db_table = 'lecassdeb'
        unique_together = (('lecassidt', 'datsea'),)


class Lecassrap(models.Model):
    lecassidt = models.CharField(primary_key=True, max_length=15, verbose_name='Clé étrangère vers lecass (lecture dans une assemblée parlementaire)')
    rapcod = models.BigIntegerField(verbose_name='Clé étrangère vers rap (rapport)')
    lecassrapord = models.BigIntegerField(blank=True, null=True, verbose_name='hiérarchisation des dossiers attachés')

    class Meta:
        managed = False
        db_table = 'lecassrap'
        unique_together = (('lecassidt', 'rapcod'),)


class Lecture(models.Model):
    lecidt = models.CharField(primary_key=True, max_length=15, verbose_name='Clé de la table')
    loicod = models.CharField(max_length=12, verbose_name='Clé étrangère vers loi (dossier législatif)')
    typleccod = models.CharField(max_length=3, verbose_name='Clé étrangère vers typlec (type de lecture)')
    leccom = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé de la lecture')

    class Meta:
        managed = False
        db_table = 'lecture'


class Libcom(models.Model):
    orgcod = models.ForeignKey(Com, models.DO_NOTHING, db_column='orgcod', related_name='+', verbose_name='Code organisme')
    libcomdatdeb = models.DateTimeField(verbose_name='Date début')
    libcomdatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date fin')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=500, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=500, blank=True, null=True, verbose_name='Observations')
    libcomart = models.CharField(max_length=12, blank=True, null=True, verbose_name='Article')
    libcomlilmin = models.CharField(max_length=500, blank=True, null=True, verbose_name='Libellé Minuscule')
    libcomlibameli = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé transfert AMELI')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')
    libcomid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')

    class Meta:
        managed = False
        db_table = 'libcom'
        unique_together = (('orgcod', 'libcomdatdeb'),)


class Libdelega(models.Model):
    orgcod = models.ForeignKey(Delega, models.DO_NOTHING, db_column='orgcod', related_name='+', verbose_name='Code organisme')
    libdelegadatdeb = models.DateTimeField(verbose_name='Date de début')
    libdelegadatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date fin')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    libdelegaart = models.CharField(max_length=12, blank=True, null=True, verbose_name='Article')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')
    libdelegaid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')

    class Meta:
        managed = False
        db_table = 'libdelega'
        unique_together = (('orgcod', 'libdelegadatdeb'),)


class Libgrppol(models.Model):
    grppolcod = models.ForeignKey(Grppol, models.DO_NOTHING, db_column='grppolcod', related_name='+', verbose_name='Code groupe politique 4e Rép.')
    libgrppoldatdeb = models.DateTimeField(verbose_name='Date début')
    libgrppoldatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    libgrppolart = models.CharField(max_length=60, blank=True, null=True, verbose_name='Article')
    libgrppolcodameli = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code transfert AMELI')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')
    libgrppolid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')

    class Meta:
        managed = False
        db_table = 'libgrppol'
        unique_together = (('grppolcod', 'libgrppoldatdeb'),)


class Lnkrap(models.Model):
    rapcodper = models.ForeignKey('Rap', models.DO_NOTHING, db_column='rapcodper', primary_key=True, related_name='+', verbose_name='Clé étrangère vers rap (rapport père)')
    rapcodenf = models.ForeignKey('Rap', models.DO_NOTHING, db_column='rapcodenf', related_name='+', verbose_name='Clé étrangère vers rap (rapport enfant)')
    rapperdsc = models.CharField(max_length=255, blank=True, null=True, verbose_name='Mention apparaissant dans le père')
    rapenfdsc = models.CharField(max_length=255, blank=True, null=True, verbose_name="Mention apparaissant dans l'enfant")

    class Meta:
        managed = False
        db_table = 'lnkrap'
        unique_together = (('rapcodper', 'rapcodenf'),)


class Loi(models.Model):
    loicod = models.CharField(primary_key=True, max_length=12, verbose_name='Clé')
    typloicod = models.CharField(max_length=4, verbose_name='Clé étrangère vers typloi (type de loi)')
    etaloicod = models.CharField(max_length=2, blank=True, null=True, verbose_name='Clé étrangère vers etaloi (état du dossier)')
    deccoccod = models.CharField(max_length=3, blank=True, null=True, verbose_name='Clé étrangère vers deccod (décision du Conseil constitutionnel)')
    numero = models.CharField(max_length=10, blank=True, null=True, verbose_name='Numéro de la loi')
    signet = models.CharField(max_length=36, blank=True, null=True, verbose_name="Racine de l'URL du dossier")
    loient = models.CharField(max_length=80, blank=True, null=True, verbose_name="Entree dans l'index")
    motclef = models.CharField(max_length=255, blank=True, null=True, verbose_name="Complement de l'index")
    loitit = models.CharField(max_length=255, blank=True, null=True, verbose_name='Titre usuel court')
    loiint = models.CharField(max_length=1024, blank=True, null=True, verbose_name='Titre long exhaustif de la loi')
    urgence = models.CharField(max_length=3, blank=True, null=True, verbose_name='oui,non ou dro')
    url_jo = models.CharField(max_length=512, blank=True, null=True, verbose_name='URL de la promulgation JO')
    loinumjo = models.CharField(max_length=36, blank=True, null=True, verbose_name='Numéro du JO')
    loidatjo = models.DateTimeField(blank=True, null=True, verbose_name='Date de publication au JO')
    date_loi = models.DateTimeField(blank=True, null=True, verbose_name='Date de promulgation')
    loititjo = models.CharField(max_length=720, blank=True, null=True, verbose_name='Titre de la loi promulguée')
    url_jo2 = models.CharField(max_length=512, blank=True, null=True, verbose_name='URL du 1er correctif JO')
    loinumjo2 = models.CharField(max_length=36, blank=True, null=True, verbose_name='Numéro du JO (1er correctif)')
    loidatjo2 = models.DateTimeField(blank=True, null=True, verbose_name='Date de publication du 1er correctif au JO')
    deccocurl = models.CharField(max_length=512, blank=True, null=True, verbose_name='URL vers la décision du Conseil constitutionnel')
    num_decision = models.CharField(max_length=15, blank=True, null=True, verbose_name='Numéro de la décision du Conseil constitutionnel')
    date_decision = models.DateTimeField(blank=True, null=True, verbose_name='Date de la décision du Conseil constitutionnel')
    loicodmai = models.CharField(max_length=12, blank=True, null=True, verbose_name='Clé étrangère vers le dossier législatif maître')
    loinoudelibcod = models.CharField(max_length=12, blank=True, null=True, verbose_name="Clé étrangère vers le dossier législatif d'une nouvelle délibération")
    motionloiorigcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Clé étrangère vers le dossier législatif sur lequel porte la motion')
    objet = models.TextField(blank=True, null=True, verbose_name='Objet du texte')
    url_ordonnance = models.CharField(max_length=100, blank=True, null=True, verbose_name="Url de l'ordonance")
    saisine_date = models.DateTimeField(blank=True, null=True, verbose_name='Date de saisine du Conseil constitutionnel')
    saisine_par = models.CharField(max_length=128, blank=True, null=True, verbose_name='Conditions de saisine du Conseil constitutionnel')
    loidatjo3 = models.DateTimeField(blank=True, null=True, verbose_name='Date de publication du 2ème correctif au JO')
    loinumjo3 = models.CharField(max_length=36, blank=True, null=True, verbose_name='Numéro du JO (2ème correctif)')
    url_jo3 = models.CharField(max_length=512, blank=True, null=True, verbose_name='URL du 2ème correctif JO')
    url_an = models.CharField(max_length=128, blank=True, null=True, verbose_name="URL du dossier législatif sur le site de l'Assemblée Nationale")
    url_presart = models.CharField(max_length=100, blank=True, null=True, verbose_name='URL de la page qui contient la présentation article par article des travaux parlementaires sur ce texte')
    signetalt = models.CharField(max_length=36, blank=True, null=True, verbose_name='Signet alternatif, à utiliser pour un renommage de signet')
    orgcod = models.CharField(max_length=4, blank=True, null=True, verbose_name='Organisme créé par la résolution')
    doscocurl = models.CharField(max_length=80, blank=True, null=True, verbose_name='URL du dossier du Conseil constitutionnel')
    loiintori = models.CharField(max_length=1024, blank=True, null=True, verbose_name="Intitulé d'origine")
    proaccdat = models.DateTimeField(blank=True, null=True, verbose_name="Date d'engagement de la procédure accélérée")
    proaccoppdat = models.DateTimeField(blank=True, null=True, verbose_name="Date d'oposition à la procédure accélérée")
    retproaccdat = models.DateTimeField(blank=True, null=True, verbose_name='Date de retrait de la procédure accélérée')

    class Meta:
        managed = False
        db_table = 'loi'


class Loithe(models.Model):
    loicod = models.ForeignKey(Loi, models.DO_NOTHING, db_column='loicod', primary_key=True, related_name='+', verbose_name='Clé étrangère vers loi (dossier législatif)')
    thecle = models.ForeignKey('The', models.DO_NOTHING, db_column='thecle', related_name='+', verbose_name='Clé étrangère vers the (thème)')

    class Meta:
        managed = False
        db_table = 'loithe'
        unique_together = (('loicod', 'thecle'),)


class Memcom(models.Model):
    memcomid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    orgcod = models.ForeignKey(Com, models.DO_NOTHING, db_column='orgcod', related_name='+', verbose_name='Code organisme')
    memcomdatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date de début')
    memcomdatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    senmat = models.ForeignKey('Sen', models.DO_NOTHING, db_column='senmat', related_name='+', verbose_name='Matricule')
    memcomtitsup = models.CharField(max_length=12, blank=True, null=True, verbose_name='Titulaire/Suppléant')
    evetempub = models.CharField(max_length=12, blank=True, null=True, verbose_name='Témoin publication')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'memcom'


class Memdelega(models.Model):
    memdelegaid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    orgcod = models.ForeignKey(Delega, models.DO_NOTHING, db_column='orgcod', related_name='+', verbose_name='Code organisme')
    memdelegadatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date de début')
    memdelegadatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    senmat = models.ForeignKey('Sen', models.DO_NOTHING, db_column='senmat', related_name='+', verbose_name='Matricule')
    designcod = models.ForeignKey(Designorg, models.DO_NOTHING, db_column='designcod', related_name='+', verbose_name='Code désignataire')
    evetempub = models.CharField(max_length=12, blank=True, null=True, verbose_name='Témoin publication')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'memdelega'


class Memgrppol(models.Model):
    memgrppolid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    grppolcod = models.ForeignKey(Grppol, models.DO_NOTHING, db_column='grppolcod', related_name='+', verbose_name='Code groupe politique 4e Rép.')
    typapppolcod = models.ForeignKey('Typapppol', models.DO_NOTHING, db_column='typapppolcod', related_name='+', verbose_name='Code type appartenance')
    memgrppoldatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date de début')
    memgrppoldatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    senmat = models.ForeignKey('Sen', models.DO_NOTHING, db_column='senmat', related_name='+', verbose_name='Matricule')
    evetempub = models.CharField(max_length=12, blank=True, null=True, verbose_name='Témoin publication')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'memgrppol'


class Natloi(models.Model):
    groupe = models.CharField(primary_key=True, max_length=36, verbose_name='Clé de la table')
    natloilib = models.CharField(max_length=40, verbose_name='Libellé')

    class Meta:
        managed = False
        db_table = 'natloi'


class Org(models.Model):
    orgcod = models.CharField(primary_key=True, max_length=4, verbose_name='Clé de la table')
    typorgcod = models.CharField(max_length=5, verbose_name="Clé étrangère vers typorg (type de l'organisme)")
    orgnom = models.CharField(max_length=128, verbose_name="Nom usuel de l'organisme")
    orgliblon = models.CharField(max_length=255, blank=True, null=True, verbose_name="Nom officiel de l'oganisme")
    codass = models.CharField(max_length=1, blank=True, null=True, verbose_name='Clé étrangère vers ass (assemblée parlementaire)')
    orglibaff = models.CharField(max_length=60, blank=True, null=True, verbose_name="Identification de l'organisme pour les applications")
    orgord = models.SmallIntegerField(blank=True, null=True, verbose_name="Ordre protocolaire de l'organisme")
    orgurl = models.CharField(max_length=124, blank=True, null=True, verbose_name="URL de la page de présentation de l'organisme")
    orglibcou = models.CharField(max_length=60, blank=True, null=True, verbose_name="Nom court de l'organisme (pour les listes)")
    org_de = models.CharField(max_length=6, blank=True, null=True, verbose_name='du, de la')
    urltra = models.CharField(max_length=124, blank=True, null=True, verbose_name="URL des travaux de l'organisme")
    inttra = models.CharField(max_length=254, blank=True, null=True, verbose_name="Intitulé associé des travaux de l'organisme")
    orgdatdebcop = models.DateTimeField(blank=True, null=True, verbose_name='Début de validité pour les communiqués de presse')
    orgdatfincop = models.DateTimeField(blank=True, null=True, verbose_name='Fin de validité pour les communiqués de presse')
    orgnomcouv = models.CharField(max_length=128, blank=True, null=True, verbose_name="Nom apparaîssant sur les couvertures des documents de l'organisme")
    senorgcod = models.CharField(max_length=12, blank=True, null=True, verbose_name="Clé de l'organisme correspondant dans la base Sénateurs")
    html_color = models.CharField(max_length=6, blank=True, null=True, verbose_name="Code couleur pour les travaux de contrôle de l'organisme")
    orgdatdeb = models.DateTimeField(blank=True, null=True, verbose_name="Date de création (premier jour d'activité)")
    orgdatfin = models.DateTimeField(blank=True, null=True, verbose_name="Date de clôture (dernier jour d'activité)")
    orggen = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'org'


class Orgnomhis(models.Model):
    onhnum = models.BigIntegerField(primary_key=True, verbose_name='Clé de la table')
    orgcod = models.ForeignKey(Org, models.DO_NOTHING, db_column='orgcod', related_name='+', verbose_name='Clé étrangère vers org')
    orgnom = models.CharField(max_length=128, verbose_name="Nom usuel de l'organisme")
    orglibcou = models.CharField(max_length=60, verbose_name="Nom court de l'organisme (pour les listes)")
    orgliblon = models.CharField(max_length=255, verbose_name="Nom officiel de l'oganisme")
    org_de = models.CharField(max_length=6, verbose_name='du, de la')
    intra = models.CharField(max_length=254, blank=True, null=True, verbose_name="Intitulé associé des travaux de l'organisme")
    orgnomcouv = models.CharField(max_length=128, blank=True, null=True, verbose_name="Nom apparaîssant sur les couvertures des documents de l'organisme")
    onhfin = models.DateTimeField(verbose_name='Date de fin de validité de cete enregistrement')

    class Meta:
        managed = False
        db_table = 'orgnomhis'


class Orippr(models.Model):
    oripprcod = models.CharField(primary_key=True, max_length=1, verbose_name='Clé de la table')
    oripprlib = models.CharField(max_length=255, verbose_name='Libellé')

    class Meta:
        managed = False
        db_table = 'orippr'


class Oritxt(models.Model):
    oritxtcod = models.CharField(primary_key=True, max_length=6, verbose_name='Clé de la table')
    oritxtlib = models.CharField(max_length=255, verbose_name='Libellé')
    oriordre = models.CharField(max_length=1, blank=True, null=True, verbose_name='0=initial (déposé), 1=final, 2=intermédiaire (commission)')
    codass = models.CharField(max_length=1, blank=True, null=True, verbose_name='Clé étrangère vers ass (assemblée parlementaire)')
    oritxtlibfem = models.CharField(max_length=255, verbose_name='Libellé féminisé')
    oritxtado = models.CharField(max_length=1, blank=True, null=True, verbose_name='Adoption : O=adopté, N=rejeté, I=indéterminé')
    oritxtorg = models.CharField(max_length=1, blank=True, null=True, verbose_name='Nécessite un organisme : O=oui, N=no')
    oritxtmod = models.CharField(max_length=1, blank=True, null=True, verbose_name='Texte modifié : O=oui, N=no')

    class Meta:
        managed = False
        db_table = 'oritxt'


class Posvot(models.Model):
    posvotcod = models.CharField(primary_key=True, max_length=1, verbose_name='Clé de la table')
    posvotlib = models.CharField(max_length=60, verbose_name='Libellé')

    class Meta:
        managed = False
        db_table = 'posvot'


class Qua(models.Model):
    quacod = models.CharField(primary_key=True, max_length=2, verbose_name='Clé de la table')
    qualic = models.CharField(max_length=12, verbose_name='Libellé')
    quaabr = models.CharField(max_length=12, verbose_name='Abrévation')
    quaabrplu = models.CharField(max_length=12, verbose_name='Abrévation au pluriel')

    class Meta:
        managed = False
        db_table = 'qua'


class QuaSen(models.Model):
    quacod = models.CharField(primary_key=True, max_length=12, verbose_name='Code qualité')
    qualic = models.CharField(max_length=60, verbose_name='Libellé court')
    quanumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    quacodsirpas = models.CharField(max_length=1, blank=True, null=True, verbose_name='Code transfert GESTION')
    quacodsex = models.CharField(max_length=1, blank=True, null=True, verbose_name='Code sexe')
    qualib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    qualil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    qualicplu = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court pluriel')
    qualibplu = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé pluriel')
    qualilplu = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long pluriel')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'qua_sen'


class Rap(models.Model):
    rapcod = models.BigIntegerField(primary_key=True, verbose_name='Code du rapport - clé interne')
    sesann = models.BigIntegerField(verbose_name='Clé étrangère vers ses (session parlementaire)')
    coddenrap = models.CharField(max_length=5, verbose_name='Clé étrangère vers denrap (dénomination du rapport)')
    typurl = models.CharField(max_length=1, verbose_name="Clé étrangère vers typurl (type de l'URL)")
    blecod = models.CharField(max_length=5, blank=True, null=True, verbose_name='Clé étrangère vers ble (Bleu budgétaire)')
    rapnum = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro')
    raptom = models.SmallIntegerField(blank=True, null=True, verbose_name='Tome')
    rapfac = models.SmallIntegerField(blank=True, null=True, verbose_name='Fascicule')
    rapann = models.SmallIntegerField(blank=True, null=True, verbose_name='Annexe')
    rapvol = models.SmallIntegerField(blank=True, null=True, verbose_name='Volume')
    raptitcou = models.CharField(max_length=254, blank=True, null=True, verbose_name="Titre court tel qu'il appara¿t dans des listes")
    raptil = models.CharField(max_length=600, blank=True, null=True, verbose_name='Titre court = titre complet du rapport')
    rapurl = models.CharField(max_length=255, blank=True, null=True, verbose_name='URL du rapport - pour les doc interne URL partiel')
    url2 = models.CharField(max_length=80, blank=True, null=True, verbose_name='URL de la deuxième partie')
    url3 = models.CharField(max_length=80, blank=True, null=True, verbose_name='URL de la troisième partie')
    url4 = models.CharField(max_length=80, blank=True, null=True, verbose_name='URL de la quatrième partie')
    url2txt = models.CharField(max_length=40, blank=True, null=True, verbose_name='Libellé associé à URL2')
    url3txt = models.CharField(max_length=40, blank=True, null=True, verbose_name='Libellé associé à URL3')
    url4txt = models.CharField(max_length=40, blank=True, null=True, verbose_name='Libellé associé à URL4')
    date_depot = models.DateTimeField(verbose_name='Date de dépôt')
    prix = models.CharField(max_length=18, blank=True, null=True, verbose_name='Prix de vente')
    rapnuman = models.BigIntegerField(blank=True, null=True, verbose_name="Numéro à l'Assemblée Nationale")
    numerobis = models.CharField(max_length=32, blank=True, null=True, verbose_name='numéro complémentaire (rectifié bis...)')
    rapsoustit = models.CharField(max_length=1024, blank=True, null=True, verbose_name='Sous-titre ¿ventuel')
    rapdatsea = models.DateTimeField(blank=True, null=True, verbose_name='Date de s¿ance ¿ laquelle le rapport est attach¿')
    depot_only = models.CharField(max_length=3, blank=True, null=True, verbose_name="Si oui, le document n'est pas disponible et n'est mentionné que dans la feuille de dépôt")
    rapres = models.CharField(max_length=4000, blank=True, null=True, verbose_name='Résumé')
    forpubcod = models.CharField(max_length=3, blank=True, null=True, verbose_name='Clé étrangère vers forpub (format de publication)')

    class Meta:
        managed = False
        db_table = 'rap'


class Raporg(models.Model):
    rapcod = models.ForeignKey(Rap, models.DO_NOTHING, db_column='rapcod', primary_key=True, related_name='+', verbose_name='Clé étrangère vers rap (rapport)')
    orgcod = models.ForeignKey(Org, models.DO_NOTHING, db_column='orgcod', related_name='+', verbose_name='Clé étrangère vers org (organisme)')

    class Meta:
        managed = False
        db_table = 'raporg'
        unique_together = (('rapcod', 'orgcod'),)


class Rapthe(models.Model):
    rapcod = models.ForeignKey(Rap, models.DO_NOTHING, db_column='rapcod', primary_key=True, related_name='+', verbose_name='Clé étrangère vers rap (rapport)')
    thecle = models.ForeignKey('The', models.DO_NOTHING, db_column='thecle', related_name='+', verbose_name='Clé étrangère vers the (thème)')

    class Meta:
        managed = False
        db_table = 'rapthe'
        unique_together = (('rapcod', 'thecle'),)


class Rolsig(models.Model):
    signataire = models.CharField(primary_key=True, max_length=1, verbose_name='Clé de la table')
    rolsiglib = models.CharField(max_length=60, verbose_name='Libellé')

    class Meta:
        managed = False
        db_table = 'rolsig'


class Scr(models.Model):
    sesann = models.BigIntegerField(primary_key=True, verbose_name='Clé étrangère vers la table sesann (session) - élément de la clé de la table')
    scrnum = models.BigIntegerField(verbose_name='Numéro de scrutin - élément de la clé de la table')
    code = models.BigIntegerField(blank=True, null=True, verbose_name='Clé étrangère vers date_seance (séance du scrutin)')
    scrint = models.CharField(max_length=4000, blank=True, null=True, verbose_name='Intitulé du scrutin')
    scrdat = models.DateTimeField(blank=True, null=True, verbose_name='date du scrutin')
    scrpou = models.BigIntegerField(blank=True, null=True, verbose_name='Nombre de pour')
    scrcon = models.BigIntegerField(blank=True, null=True, verbose_name='Nombre de contre')
    scrvot = models.BigIntegerField(blank=True, null=True, verbose_name='Nombre de votants')
    scrsuf = models.BigIntegerField(blank=True, null=True, verbose_name='Nombre de suffrages exprimés')
    scrvotsea = models.BigIntegerField(blank=True, null=True, verbose_name='Nombre de votants annoncé en séance')
    scrsufsea = models.BigIntegerField(blank=True, null=True, verbose_name='Nombre de suffrages exprimés annoncé en séance')
    scrpousea = models.BigIntegerField(blank=True, null=True, verbose_name='Nombre de pour annoncé en séance')
    scrconsea = models.BigIntegerField(blank=True, null=True, verbose_name='Nombre de contre annoncé en séance')
    scrmaj = models.BigIntegerField(blank=True, null=True, verbose_name='majorité des suffrages exprimés')
    scrmajsea = models.BigIntegerField(blank=True, null=True, verbose_name='majorité des suffrages exprimés annoncée en séance')
    soslib = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scr'
        unique_together = (('sesann', 'scrnum'),)


class Secdis(models.Model):
    secdiscle = models.BigIntegerField(primary_key=True, verbose_name='Clé')
    lecassidt = models.CharField(max_length=255, verbose_name='Clé étrangère vers dosleg.lecass (lecture)')
    typseccod = models.ForeignKey('Typsec', models.DO_NOTHING, db_column='typseccod', related_name='+', verbose_name='Clé étrangère vers typsec (type de section)')
    datsea = models.DateTimeField(verbose_name='Clé étrangère vers débats')
    secdisnum = models.CharField(max_length=512, blank=True, null=True, verbose_name='Numérotation de la section')
    secdisobj = models.CharField(max_length=2048, blank=True, null=True, verbose_name='Objet de la section')
    secdisurl = models.CharField(max_length=80, blank=True, null=True, verbose_name='URL de la section')
    secdisordid = models.BigIntegerField(blank=True, null=True, verbose_name='Ordre dans la fratrie')
    secdispere = models.BigIntegerField(blank=True, null=True, verbose_name='Section mère')

    class Meta:
        managed = False
        db_table = 'secdis'


class Secdivers(models.Model):
    secdiverscle = models.BigIntegerField(primary_key=True, verbose_name='Clé')
    typseccod = models.ForeignKey('Typsec', models.DO_NOTHING, db_column='typseccod', related_name='+', verbose_name='Clé étrangère vers typsec (type de section)')
    datsea = models.DateTimeField(verbose_name='Clé étrangère vers débats')
    secdiverslibelle = models.CharField(max_length=254, blank=True, null=True, verbose_name='Libellé associé à la section')
    secdiversobj = models.CharField(max_length=2048, blank=True, null=True, verbose_name='Objet de la section')

    class Meta:
        managed = False
        db_table = 'secdivers'


class Sen(models.Model):
    senmat = models.CharField(primary_key=True, max_length=6, verbose_name='Matricule')
    quacod = models.ForeignKey(QuaSen, models.DO_NOTHING, db_column='quacod', related_name='+', verbose_name='Code qualité')
    sennomuse = models.CharField(max_length=40, verbose_name='Nom usuel')
    senprenomuse = models.CharField(max_length=60, verbose_name='Prénom usuel')
    etasencod = models.ForeignKey(Etasen, models.DO_NOTHING, db_column='etasencod', related_name='+', verbose_name='Code état sénateur')
    sengrppolcodcou = models.ForeignKey(Grppol, models.DO_NOTHING, db_column='sengrppolcodcou', blank=True, null=True, related_name='+', verbose_name='Code groupe politique courant')
    sengrppolliccou = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé groupe politique courant')
    sentypappcou = models.CharField(max_length=60, blank=True, null=True, verbose_name='Appartenance politique courante')
    sencomcodcou = models.ForeignKey(Com, models.DO_NOTHING, db_column='sencomcodcou', blank=True, null=True, related_name='+', verbose_name='Code commission courante')
    sencomliccou = models.CharField(max_length=60, blank=True, null=True, verbose_name='Commission courante')
    sencirnumcou = models.ForeignKey(Dpt, models.DO_NOTHING, db_column='sencirnumcou', blank=True, null=True, related_name='+', verbose_name='Identifiant circonscription')
    sencircou = models.CharField(max_length=120, blank=True, null=True, verbose_name='Circonscription courante')
    senburliccou = models.CharField(max_length=60, blank=True, null=True, verbose_name='Fonction bureau courante')
    sendatpreele = models.DateTimeField(blank=True, null=True, verbose_name='Premier jour de mandat')
    sennomusecap = models.CharField(max_length=40, verbose_name='Nom usuel Capitales')
    sencrinom = models.CharField(max_length=40, blank=True, null=True, verbose_name='Nom CRI')
    senfem = models.CharField(max_length=12, blank=True, null=True, verbose_name='Féminisation fonctions')
    sennomdis = models.CharField(max_length=40, blank=True, null=True, verbose_name='Nom distinctif')
    sennomdit = models.CharField(max_length=40, blank=True, null=True, verbose_name='Nom dit')
    titnobcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code titre noblesse')
    senobs4r1 = models.CharField(max_length=500, blank=True, null=True, verbose_name='Observation 4e Rép. 1')
    senobs4r2 = models.CharField(max_length=500, blank=True, null=True, verbose_name='Observation 4e Rép. 2')
    senobs3r1 = models.CharField(max_length=500, blank=True, null=True, verbose_name='Observation 3e Rép. 1')
    senobs3r2 = models.CharField(max_length=500, blank=True, null=True, verbose_name='Observation 3e Rép. 2')
    sendatderele = models.DateTimeField(blank=True, null=True, verbose_name='Dernier jour de mandat')
    sencirnumcou4r = models.BigIntegerField(blank=True, null=True, verbose_name='Num Circonscription courante 4 Rép.')
    sencircou4r = models.CharField(max_length=120, blank=True, null=True, verbose_name='Circonscription courante 4 Rép.')
    sencirnumcou3r = models.BigIntegerField(blank=True, null=True, verbose_name='Num Circonscription courante 3 Rép.')
    sencircou3r = models.CharField(max_length=120, blank=True, null=True, verbose_name='Circonscription courante 3 Rép.')
    sengrppolcodcou4r = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code groupe politique courant 4e Rép.')
    sentypappcou4r = models.CharField(max_length=60, blank=True, null=True, verbose_name='Appartenance politique courante 4 Rép.')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')
    catprocod2e = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code catégorie professionnelle 2nd Emp.')
    sendespro2e = models.CharField(max_length=255, blank=True, null=True, verbose_name='Description profession 2nd Emp.')
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
    senburid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    burcod = models.ForeignKey(Bur, models.DO_NOTHING, db_column='burcod', related_name='+', verbose_name='Code bureau 4e Rép.')
    senburdatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date de début')
    senburdatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    senburrelint = models.CharField(max_length=12, blank=True, null=True, verbose_name='Chargé Relations Internationales')
    senburrngele = models.BigIntegerField(blank=True, null=True, verbose_name="Rang d'élection")
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    senmat = models.ForeignKey(Sen, models.DO_NOTHING, db_column='senmat', related_name='+', verbose_name='Matricule')
    senburhon = models.CharField(max_length=12, blank=True, null=True, verbose_name='Honorariat')
    evetempub = models.CharField(max_length=12, blank=True, null=True, verbose_name='Témoin publication')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'senbur'


class Sennom(models.Model):
    senmat = models.ForeignKey(Sen, models.DO_NOTHING, db_column='senmat', related_name='+', verbose_name='Matricule')
    sennomdatdeb = models.DateTimeField(verbose_name='Date de début')
    sennomdatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    quacod = models.ForeignKey(QuaSen, models.DO_NOTHING, db_column='quacod', related_name='+', verbose_name='Code qualité')
    sennomuse = models.CharField(max_length=40, verbose_name='Nom usuel')
    sennomusecap = models.CharField(max_length=40, verbose_name='Nom usuel Capitales')
    sennomtec = models.CharField(max_length=60, verbose_name='Nom technique')
    senprenomuse = models.CharField(max_length=60, verbose_name='Prénom usuel')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')
    sennomid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')

    class Meta:
        managed = False
        db_table = 'sennom'
        unique_together = (('senmat', 'sennomdatdeb'),)


class Ses(models.Model):
    sesann = models.BigIntegerField(primary_key=True, verbose_name="Clé de la table (année de l'ouverture de la session)")
    seslib = models.CharField(max_length=36, verbose_name='Libellé')

    class Meta:
        managed = False
        db_table = 'ses'


class Stavot(models.Model):
    stavotidt = models.CharField(primary_key=True, max_length=2, verbose_name='Clé de la table')
    stavotlib = models.CharField(max_length=60, verbose_name='Libellé')

    class Meta:
        managed = False
        db_table = 'stavot'


class Syndeb(models.Model):
    debsyn = models.CharField(primary_key=True, max_length=1, verbose_name='Clé')
    syndeblib = models.CharField(max_length=60, verbose_name='Libellé')

    class Meta:
        managed = False
        db_table = 'syndeb'


class Texte(models.Model):
    texcod = models.BigIntegerField(primary_key=True, verbose_name='Clé de la table')
    oritxtcod = models.CharField(max_length=6, blank=True, null=True, verbose_name='origine du texte - clé externe')
    typtxtcod = models.CharField(max_length=3, verbose_name='type du texte - clé externe')
    typurl = models.CharField(max_length=1, verbose_name="type d'URL")
    lecassidt = models.CharField(max_length=15, verbose_name='lecture par assemblée - clé externe')
    sesann = models.BigIntegerField(blank=True, null=True, verbose_name='Session de numérotation - clé externe')
    orgcod = models.CharField(max_length=4, blank=True, null=True, verbose_name='Organisme associé - clé externe')
    texnum = models.BigIntegerField(blank=True, null=True, verbose_name='numéro du texte')
    texurl = models.CharField(max_length=255, blank=True, null=True, verbose_name='URL principal')
    url2 = models.CharField(max_length=36, blank=True, null=True, verbose_name='URL complémentaire 2')
    url3 = models.CharField(max_length=80, blank=True, null=True, verbose_name='URL complémentaire 3')
    url4 = models.CharField(max_length=256, blank=True, null=True, verbose_name='URL complémentaire 4')
    url2txt = models.CharField(max_length=256, blank=True, null=True, verbose_name="Libellé pour l'URL 2")
    url3txt = models.CharField(max_length=256, blank=True, null=True, verbose_name="libellé pour l'URL 3")
    url4txt = models.CharField(max_length=256, blank=True, null=True, verbose_name="Libellé pour l'URL 4")
    txtoritxtdat = models.DateTimeField(verbose_name='Date associée au texte (dépôt ou adoption)')
    prix = models.CharField(max_length=18, blank=True, null=True, verbose_name='Prix de vente')
    numerobis = models.CharField(max_length=32, blank=True, null=True, verbose_name='numéro complémentaire (rectifié bis...)')
    texdatsea = models.DateTimeField(blank=True, null=True, verbose_name='Date de séance à laquelle est rattaché le dépôt du texte')
    reserve_comspe = models.CharField(max_length=3, blank=True, null=True, verbose_name='Sous réserve decom. spéciale (oui/non)')
    datrejet_disc_immediate = models.DateTimeField(blank=True, null=True, verbose_name='Date (éventuelle) de rejet de la demande de discussion immédiate')
    texace = models.CharField(max_length=1, blank=True, null=True, verbose_name="O si associé à un avis du Conseil d'état")

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
    thecle = models.SmallIntegerField(primary_key=True, verbose_name='Clé de la table')
    thelib = models.CharField(max_length=80, verbose_name='Libellé')
    theali = models.CharField(max_length=80, blank=True, null=True, verbose_name='relatif [à/au/à la,...]')

    class Meta:
        managed = False
        db_table = 'the'


class Titsen(models.Model):
    titsencod = models.CharField(primary_key=True, max_length=1, verbose_name='Clé de la table')
    titsenlib = models.CharField(max_length=69, blank=True, null=True, verbose_name='Libellé')

    class Meta:
        managed = False
        db_table = 'titsen'


class Typapppol(models.Model):
    typapppolcod = models.CharField(primary_key=True, max_length=1, verbose_name='Code type appartenance')
    typapppollib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    typapppollic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    typapppolnumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    typapppollil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    typapppollicfem = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court féminin')
    typapppollibfem = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé féminin')
    typapppollilfem = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long féminin')
    typapppollicplu = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court pluriel')
    typapppollibplu = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé pluriel')
    typapppollilplu = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long pluriel')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'typapppol'


class Typatt(models.Model):
    typattcod = models.CharField(primary_key=True, max_length=1, verbose_name='Clé de la table')
    typattlib = models.CharField(max_length=40, verbose_name='Libellé')

    class Meta:
        managed = False
        db_table = 'typatt'


class Typaut(models.Model):
    typautcod = models.CharField(primary_key=True, max_length=3, verbose_name='Clé de la table')
    typautlib = models.CharField(max_length=36, verbose_name='Libellé')

    class Meta:
        managed = False
        db_table = 'typaut'


class Typdoc(models.Model):
    typdoccod = models.CharField(primary_key=True, max_length=3, verbose_name='Clé de la table')
    typdoclib = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé')

    class Meta:
        managed = False
        db_table = 'typdoc'


class Typevtsea(models.Model):
    typevtcod = models.CharField(primary_key=True, max_length=3, verbose_name='Clé de la table')
    typevtlib = models.CharField(max_length=61, verbose_name='Libellé')

    class Meta:
        managed = False
        db_table = 'typevtsea'


class Typlec(models.Model):
    typleccod = models.CharField(primary_key=True, max_length=3, verbose_name='Clé de la table')
    typleclib = models.CharField(max_length=60, verbose_name='Libellé')
    typlecord = models.BigIntegerField(blank=True, null=True, verbose_name='classement de la lecture')

    class Meta:
        managed = False
        db_table = 'typlec'


class Typloi(models.Model):
    typloicod = models.CharField(primary_key=True, max_length=4, verbose_name='Clé de la table')
    typloilib = models.CharField(max_length=80, verbose_name='Libellé')
    groupe = models.CharField(max_length=36, blank=True, null=True, verbose_name='Clé étrangère vers natloi (regroupement de dossiers par nature)')
    typloiden = models.CharField(max_length=80, blank=True, null=True, verbose_name='Dénomination officielle du type de dossier')
    typloigen = models.CharField(max_length=1, blank=True, null=True, verbose_name='Genre : F=féminin, M=masculin')
    typloitit = models.CharField(max_length=80, blank=True, null=True, verbose_name='Titre utilisé pour les regroupements par types')
    typloidenplu = models.CharField(max_length=80, blank=True, null=True, verbose_name='Dénomination au pluriel')
    typloide = models.CharField(max_length=10, blank=True, null=True, verbose_name='de, de la...')
    typloiabr = models.CharField(max_length=20, blank=True, null=True, verbose_name='Abréviation, utilisée notamment dans le TAP')

    class Meta:
        managed = False
        db_table = 'typloi'


class Typorg(models.Model):
    typorgcod = models.CharField(primary_key=True, max_length=5, verbose_name='Clé de la table')
    typorglib = models.CharField(max_length=60, verbose_name='Libellé')
    typorgurl = models.CharField(max_length=254, blank=True, null=True, verbose_name='URL de la page associée')
    typorgtitens = models.CharField(max_length=60, blank=True, null=True, verbose_name='Titre associé à la listes des organismes du type considéré')
    typorgvid = models.CharField(max_length=60, blank=True, null=True, verbose_name='Code pour la vidéothèque')
    typorgord = models.BigIntegerField(blank=True, null=True, verbose_name='Classement')

    class Meta:
        managed = False
        db_table = 'typorg'


class TyporgSen(models.Model):
    typorgcod = models.CharField(primary_key=True, max_length=12, verbose_name='Code type organisme')
    typorglib = models.CharField(max_length=120, verbose_name='Libellé')
    typorglic = models.CharField(max_length=60, verbose_name='Libellé court')
    typorgnumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    evetempub = models.CharField(max_length=12, blank=True, null=True)
    typorgurlsim = models.CharField(max_length=500, blank=True, null=True, verbose_name='URL simplifiée')
    typorgurlcmp = models.CharField(max_length=500, blank=True, null=True, verbose_name='URL complète')
    typorglibplu = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé pluriel')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'typorg_sen'


class Typrap(models.Model):
    typraprap = models.CharField(primary_key=True, max_length=5, verbose_name='Clé de la table')
    typraplib = models.CharField(max_length=60, verbose_name='Libellé')
    typrapind = models.CharField(max_length=1, verbose_name='O = indépendent dess dossiers législatifs')
    typraplibplu = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé pluriel')
    typrapurl = models.CharField(max_length=255, blank=True, null=True, verbose_name='URL de la page présentants les rapports de ce type')
    catrapcod = models.CharField(max_length=1, blank=True, null=True, verbose_name='Clé étrangère vers catrap (catégorie du rapport)')
    typraprep = models.CharField(max_length=254, blank=True, null=True, verbose_name='Répertoire par défaut pour ce type de rapports')
    typrapnot = models.CharField(max_length=1, blank=True, null=True, verbose_name='O=une notice est générée pour ce type de rapports')
    typrapses = models.CharField(max_length=1, blank=True, null=True, verbose_name='O=la numérotation est remise à zéro à chaque session')

    class Meta:
        managed = False
        db_table = 'typrap'


class Typsec(models.Model):
    typseccod = models.CharField(primary_key=True, max_length=32, verbose_name='Clé')
    typseclib = models.CharField(max_length=64, verbose_name='Libellé')
    typseccat = models.CharField(max_length=15, blank=True, null=True, verbose_name='Catégorie liée au type')

    class Meta:
        managed = False
        db_table = 'typsec'


class Typtxt(models.Model):
    typtxtcod = models.CharField(primary_key=True, max_length=3, verbose_name='Clé de la table')
    typtxtlib = models.CharField(max_length=36, verbose_name='Libellé')

    class Meta:
        managed = False
        db_table = 'typtxt'


class Typurl(models.Model):
    typurl = models.CharField(primary_key=True, max_length=1, verbose_name='Clé de la table')
    libtypurl = models.CharField(max_length=40, verbose_name='Libellé')

    class Meta:
        managed = False
        db_table = 'typurl'


class Votsen(models.Model):
    sesann = models.BigIntegerField(primary_key=True, verbose_name='Avec scrnum, clé étrangère vers la table scr (scrutin) - élément de la clé de la table')
    scrnum = models.BigIntegerField(verbose_name='Avec sesann, clé étrangère vers la table scr (numéro de scrutin) - élément de la clé de la table')
    senmat = models.CharField(max_length=6, verbose_name='Matricule du sénateur (table SEN de la base senateurs) - élément de la clé de la table')
    posvotcod = models.CharField(max_length=1, blank=True, null=True, verbose_name='Clé étrangère vers posvot (position de vote)')
    titsencod = models.CharField(max_length=1, verbose_name='Clé étrangère vers titsen (titre du sénateur)')
    stavotidt = models.CharField(max_length=2, verbose_name='Clé étrangère vers statvot (statut spécial du votant)')
    senmatdel = models.CharField(max_length=6, blank=True, null=True, verbose_name='Matricule du délégant (clé étrangère vers SEN)')

    class Meta:
        managed = False
        db_table = 'votsen'
        unique_together = (('sesann', 'scrnum', 'senmat'),)

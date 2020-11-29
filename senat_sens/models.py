# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Activite(models.Model):
    actid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    typactcod = models.CharField(max_length=30, verbose_name='Type')
    catactcod = models.CharField(max_length=20, verbose_name='Catégorie')
    scrid = models.BigIntegerField(blank=True, null=True)
    comcod = models.CharField(max_length=12, blank=True, null=True)
    delegacod = models.CharField(max_length=12, blank=True, null=True)
    actlic = models.CharField(max_length=90, blank=True, null=True, verbose_name='Libellé court')
    actlib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
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
    actid = models.BigIntegerField(primary_key=True, verbose_name="Identifiant de l'activité")
    loicod = models.CharField(max_length=12, verbose_name="Identifiant d'un texte dans la table loi de la base DOSLEG")

    class Meta:
        managed = False
        db_table = 'activite_loi'
        unique_together = (('actid', 'loicod'),)


class ActiviteParticipant(models.Model):
    actparid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    actid = models.BigIntegerField(verbose_name='Activité à laquelle le Sénateur participe')
    senmat = models.CharField(max_length=6, verbose_name='Sénateur')
    fapcod = models.CharField(max_length=30, verbose_name='Fonction particulière')
    fapidx = models.BigIntegerField(blank=True, null=True, verbose_name="Ordonnancement dans la fonction. Permet notamment d'ordonner les présidents de réunion.")
    typactparcod = models.CharField(max_length=20, verbose_name="Sénateur présent ou excusé (au sens de la commission, pas de l'article 23bis).")

    class Meta:
        managed = False
        db_table = 'activite_participant'
        unique_together = (('actid', 'senmat'), ('actid', 'senmat'), ('actid', 'senmat'),)


class ActiviteSenateur(models.Model):
    actsenid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    senmat = models.CharField(max_length=6, verbose_name='Sénateur')
    typactsencod = models.CharField(max_length=20, verbose_name="Type d'activité")
    datdeb = models.DateTimeField(verbose_name='Début')
    datfin = models.DateTimeField(verbose_name='Fin')
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
    actprocod = models.CharField(primary_key=True, max_length=12, verbose_name='Code activité professionnelle')
    actprolib = models.CharField(max_length=60)
    actpronumtri = models.BigIntegerField(blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'actpro'


class Adresse(models.Model):
    adrid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    poiconid = models.BigIntegerField(verbose_name='Identifiant point de contact')
    typbistercod = models.CharField(max_length=12)
    typvoicod = models.CharField(max_length=12)
    adrcmp = models.CharField(max_length=38, blank=True, null=True, verbose_name='Complément adresse')
    adrcmp2 = models.CharField(max_length=38, blank=True, null=True, verbose_name='Complément adresse 2')
    adrnumvoi = models.CharField(max_length=38, blank=True, null=True, verbose_name='Numéro dans la voie')
    adrnomvoi = models.CharField(max_length=38, blank=True, null=True, verbose_name='nom de la voie')
    adrcom = models.CharField(max_length=38, blank=True, null=True, verbose_name='Commune')
    adrcodpos = models.CharField(max_length=5, blank=True, null=True, verbose_name='Code postal')
    adrburdis = models.CharField(max_length=38, blank=True, null=True, verbose_name='Bureau distributeur')
    adrcdxcod = models.CharField(max_length=5, blank=True, null=True, verbose_name='Code Cedex')
    adrcdxlib = models.CharField(max_length=38, blank=True, null=True, verbose_name='Libellé Cedex')
    adrnumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
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
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')
    assterart = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asster'


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
    typorgcod = models.CharField(max_length=12, verbose_name='Code type organisme')
    orgcod = models.CharField(primary_key=True, max_length=12, verbose_name='Code organisme')
    orgnumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    orgdatcre = models.DateTimeField(blank=True, null=True, verbose_name='Date création')
    orgdatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    orgnumtie = models.CharField(max_length=12, blank=True, null=True, verbose_name='NuméroTiers')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=500, blank=True, null=True, verbose_name='Libellé long')
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


class Csp(models.Model):
    cspcod = models.CharField(primary_key=True, max_length=12, verbose_name='Code CSP')
    catprocod = models.CharField(max_length=12, verbose_name='Code catégorie professionnelle')
    cspfamcod = models.CharField(max_length=12, verbose_name='Code famille CSP')
    csplib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Rubrique CSP')
    cspnumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri CSP')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'csp'


class Delega(models.Model):
    typorgcod = models.CharField(max_length=12, verbose_name='Code type organisme')
    orgcod = models.CharField(primary_key=True, max_length=12, verbose_name='Code organisme')
    orgnumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    orgdatcre = models.DateTimeField(blank=True, null=True, verbose_name='Date création')
    orgdatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    orgnumtie = models.CharField(max_length=12, blank=True, null=True, verbose_name='NuméroTiers')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
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


class Design(models.Model):
    designcod = models.CharField(primary_key=True, max_length=12, verbose_name='Code désignataire')
    moddescod = models.CharField(max_length=12, verbose_name='Code')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    orgcod = models.CharField(max_length=12, verbose_name='Code organisme')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    designnumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'design'


class Designoep(models.Model):
    designcod = models.CharField(max_length=12, verbose_name='Code désignataire')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    orgcod = models.CharField(max_length=12, verbose_name='Code organisme')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    designoepnumtri = models.BigIntegerField(blank=True, null=True)
    designoepnbrtit = models.BigIntegerField(blank=True, null=True)
    designoepnbrsup = models.BigIntegerField(blank=True, null=True)
    designoepdatdeb = models.DateTimeField(blank=True, null=True)
    designoepdatfin = models.DateTimeField(blank=True, null=True)
    designoepid = models.BigIntegerField(primary_key=True)
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')
    fonmemextparcod = models.CharField(max_length=20)
    fontemrem = models.CharField(max_length=12, blank=True, null=True)
    fonremlil = models.CharField(max_length=512, blank=True, null=True)
    incompat = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'designoep'


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
    dpturlcmp = models.CharField(max_length=255, blank=True, null=True, verbose_name='URL')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'dpt'


class Dptele(models.Model):
    dptnum = models.BigIntegerField(verbose_name='Identifiant circonscription')
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


class Dpttypman(models.Model):
    dptnum = models.BigIntegerField(verbose_name='Identifiant circonscription')
    typmancod = models.CharField(max_length=12, verbose_name='Code type mandat')
    dpttypmanid = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'dpttypman'


class Ele(models.Model):
    typmancod = models.CharField(max_length=12, verbose_name='Code type mandat')
    eleann = models.CharField(max_length=12, verbose_name='Année')
    eledat = models.DateTimeField(blank=True, null=True, verbose_name="Date de l'élection")
    eledatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date début mandat')
    eledatfinpre = models.DateTimeField(blank=True, null=True, verbose_name='Date fin mandat précédent')
    eleser = models.CharField(max_length=1, blank=True, null=True, verbose_name='Série')
    elelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    elelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    elelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')
    eleid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    elepar = models.CharField(max_length=12, blank=True, null=True, verbose_name='Élection partielle')

    class Meta:
        managed = False
        db_table = 'ele'


class Elucan(models.Model):
    eluid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    eludatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date début mandat')
    eludatelu = models.DateTimeField(blank=True, null=True, verbose_name="Date d'élection")
    eludatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date fin mandat')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    eluanndeb = models.BigIntegerField(blank=True, null=True, verbose_name='Année début mandat')
    eluannfin = models.BigIntegerField(blank=True, null=True, verbose_name='Année fin mandat')
    elunbrhab = models.BigIntegerField(blank=True, null=True, verbose_name="Nombre d'habitants")
    typmancod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code type mandat')
    dptnum = models.BigIntegerField(blank=True, null=True, verbose_name='Identifiant du département')
    senmat = models.CharField(max_length=6, verbose_name='Matricule')
    canart = models.CharField(max_length=60, blank=True, null=True, verbose_name='Aaticle de la circonscription')
    eludatcum = models.DateTimeField(blank=True, null=True, verbose_name='Date cumul')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'elucan'


class Eludep(models.Model):
    eluid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    eludatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date début mandat')
    depcod = models.CharField(max_length=12, blank=True, null=True)
    eludatelu = models.DateTimeField(blank=True, null=True, verbose_name="Date d'élection")
    eludatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date fin mandat')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    eluanndeb = models.BigIntegerField(blank=True, null=True, verbose_name='Année début mandat')
    eluannfin = models.BigIntegerField(blank=True, null=True, verbose_name='Année fin mandat')
    elunbrhab = models.BigIntegerField(blank=True, null=True, verbose_name="Nombre d'habitants")
    typmancod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code type mandat')
    senmat = models.CharField(max_length=6, verbose_name='Matricule')
    eludatcum = models.DateTimeField(blank=True, null=True, verbose_name='Date cumul')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')
    id_organe_assnat = models.CharField(max_length=50, blank=True, null=True)
    circo = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eludep'


class Eludiv(models.Model):
    eluid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    eludatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date début mandat')
    eludatelu = models.DateTimeField(blank=True, null=True, verbose_name="Date d'élection")
    eludatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date fin mandat')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    eluanndeb = models.BigIntegerField(blank=True, null=True, verbose_name='Année début mandat')
    eluannfin = models.BigIntegerField(blank=True, null=True, verbose_name='Année fin mandat')
    elunbrhab = models.BigIntegerField(blank=True, null=True, verbose_name="Nombre d'habitants")
    typmancod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code type mandat')
    senmat = models.CharField(max_length=6, verbose_name='Matricule')
    eludatcum = models.DateTimeField(blank=True, null=True, verbose_name='Date cumul')
    eludivurlcmp = models.CharField(max_length=255, blank=True, null=True)
    eludivart = models.CharField(max_length=60, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'eludiv'


class Elueur(models.Model):
    eluid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    eludatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date début mandat')
    eludatelu = models.DateTimeField(blank=True, null=True, verbose_name="Date d'élection")
    eludatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date fin mandat')
    nationcod = models.CharField(max_length=12, blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    eluanndeb = models.BigIntegerField(blank=True, null=True, verbose_name='Année début mandat')
    eluannfin = models.BigIntegerField(blank=True, null=True, verbose_name='Année fin mandat')
    elunbrhab = models.BigIntegerField(blank=True, null=True, verbose_name="Nombre d'habitants")
    typmancod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code type mandat')
    senmat = models.CharField(max_length=6, verbose_name='Matricule')
    eludatcum = models.DateTimeField(blank=True, null=True, verbose_name='Date cumul')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'elueur'


class Elureg(models.Model):
    eluid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    eludatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date début mandat')
    regcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code région')
    eludatelu = models.DateTimeField(blank=True, null=True, verbose_name="Date d'élection")
    eludatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date fin mandat')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    eluanndeb = models.BigIntegerField(blank=True, null=True, verbose_name='Année début mandat')
    eluannfin = models.BigIntegerField(blank=True, null=True, verbose_name='Année fin mandat')
    elunbrhab = models.BigIntegerField(blank=True, null=True, verbose_name="Nombre d'habitants")
    typmancod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code type mandat')
    senmat = models.CharField(max_length=6, verbose_name='Matricule')
    eludatcum = models.DateTimeField(blank=True, null=True, verbose_name='Date cumul')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'elureg'


class Elusen(models.Model):
    eluid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    dptnum = models.BigIntegerField(verbose_name='Identifiant circonscription')
    eludatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date début mandat')
    eludatelu = models.DateTimeField(blank=True, null=True, verbose_name="Date d'élection")
    eludatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date fin mandat')
    etadebmancod = models.CharField(max_length=12, verbose_name='Code début de mandat')
    etafinmancod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code état fin de mandat')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eluanndeb = models.BigIntegerField(blank=True, null=True, verbose_name='Année début mandat')
    eluannfin = models.BigIntegerField(blank=True, null=True, verbose_name='Année fin mandat')
    typmancod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code type mandat')
    senmat = models.CharField(max_length=6, verbose_name='Matricule')
    eludatcum = models.DateTimeField(blank=True, null=True, verbose_name='Date cumul')
    turelucod = models.CharField(max_length=12, verbose_name='Code tour élection')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'elusen'


class Eluter(models.Model):
    eluid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    asstercod = models.CharField(max_length=12, blank=True, null=True)
    typmancod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code type mandat')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    eludatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date début mandat')
    eluanndeb = models.BigIntegerField(blank=True, null=True, verbose_name='Année début mandat')
    eludatelu = models.DateTimeField(blank=True, null=True, verbose_name="Date d'élection")
    eludatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date fin mandat')
    eluannfin = models.BigIntegerField(blank=True, null=True, verbose_name='Année fin mandat')
    elunbrhab = models.BigIntegerField(blank=True, null=True, verbose_name="Nombre d'habitants")
    senmat = models.CharField(max_length=6, verbose_name='Matricule')
    eludatcum = models.DateTimeField(blank=True, null=True, verbose_name='Date cumul')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'eluter'


class Elutit(models.Model):
    eluid = models.BigIntegerField(verbose_name='Identifiant')
    titeluid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    titelecod = models.CharField(max_length=12, verbose_name='Code titre élu')
    titeludatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date de début')
    titeluanndeb = models.BigIntegerField(blank=True, null=True, verbose_name='Année de début')
    titeludatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    titeluannfin = models.BigIntegerField(blank=True, null=True, verbose_name='Année de fin')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    titeluhon = models.CharField(max_length=12, blank=True, null=True, verbose_name='Honorariat')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'elutit'


class Eluvil(models.Model):
    eluid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    eludatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date début mandat')
    eludatelu = models.DateTimeField(blank=True, null=True, verbose_name="Date d'élection")
    eludatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date fin mandat')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    eluanndeb = models.BigIntegerField(blank=True, null=True, verbose_name='Année début mandat')
    eluannfin = models.BigIntegerField(blank=True, null=True, verbose_name='Année fin mandat')
    elunbrhab = models.BigIntegerField(blank=True, null=True, verbose_name="Nombre d'habitants")
    typmancod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code type mandat')
    senmat = models.CharField(max_length=6, verbose_name='Matricule')
    vilart = models.CharField(max_length=60, blank=True, null=True)
    eludatcum = models.DateTimeField(blank=True, null=True, verbose_name='Date cumul')
    vilurlcmp = models.CharField(max_length=255, blank=True, null=True)
    url = models.CharField(max_length=120, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'eluvil'


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


class Fongrpsen(models.Model):
    fongrpsencod = models.CharField(primary_key=True, max_length=12, verbose_name='Code fonction groupe sénatorial')
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
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')
    fongrpsenlicfemplu = models.CharField(max_length=60, blank=True, null=True)
    fongrpsenlibfemplu = models.CharField(max_length=120, blank=True, null=True)
    fongrpsenlilfemplu = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fongrpsen'


class Fonmemcom(models.Model):
    fonmemcomid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    foncomcod = models.CharField(max_length=12, verbose_name='Code fonction commission')
    fonmemcomdatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date de début')
    fonmemcomdatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    fonmemcomrngprt = models.BigIntegerField(blank=True, null=True, verbose_name='Rang protocolaire')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    memcomid = models.BigIntegerField(verbose_name='Identifiant')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'fonmemcom'


class Fonmemdelega(models.Model):
    fonmemdelid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    fondelcod = models.CharField(max_length=12, verbose_name='Code fonction délégation')
    fonmemdeldatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date de début')
    fonmemdeldatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    memdelegaid = models.BigIntegerField(verbose_name='Identifiant')
    fonmemdelrngele = models.BigIntegerField(blank=True, null=True, verbose_name='Rang élection')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'fonmemdelega'


class Fonmemgrppol(models.Model):
    fonmemgrppolid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    fongrppolcod = models.CharField(max_length=12, verbose_name='Code fonction groupe politique')
    fonmemgrppoldatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date de début')
    fonmemgrppoldatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=30, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    memgrppolid = models.BigIntegerField(verbose_name='Identifiant')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'fonmemgrppol'


class Fonmemgrpsen(models.Model):
    fonmemgrpsenid = models.BigIntegerField(primary_key=True)
    fongrpsencod = models.CharField(max_length=12, verbose_name='Code fonction groupe sénatorial')
    fonmemgrpsendatdeb = models.DateTimeField()
    fonmemgrpsendatfin = models.DateTimeField(blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    memgrpsenid = models.BigIntegerField()
    fonmemgrpsenrngele = models.BigIntegerField(blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'fonmemgrpsen'


class Fonmemorg(models.Model):
    fonmemorgid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    memorgid = models.BigIntegerField(verbose_name='Identifiant')
    fonorgcod = models.CharField(max_length=12, verbose_name='Code fonction organisme')
    fonmemorgdatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date de début')
    fonmemorganndeb = models.BigIntegerField(blank=True, null=True, verbose_name='Année de début')
    fonmemorgdatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    fonmemorgannfin = models.BigIntegerField(blank=True, null=True, verbose_name='Année de fin')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    fonmemorgrngele = models.BigIntegerField(blank=True, null=True, verbose_name='Rang élection')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'fonmemorg'


class Fonorg(models.Model):
    fonorgcod = models.CharField(primary_key=True, max_length=12, verbose_name='Code fonction organisme')
    fonorglib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    fonorglic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    fonorgnumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    fonorglil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    fonorglibfem = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé féminin')
    fonorglicfem = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court féminin')
    fonorglilfem = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long féminin')
    fonorglibplu = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé pluriel')
    fonorglicplu = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court pluriel')
    fonorglilplu = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long pluriel')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')
    fonorglicfemplu = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court féminin pluriel')
    fonorglibfemplu = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé féminin pluriel')
    fonorglilfemplu = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long féminin pluriel')

    class Meta:
        managed = False
        db_table = 'fonorg'


class Grppol(models.Model):
    grppolcod = models.CharField(primary_key=True, max_length=12, verbose_name='Code groupe politique 4e Rép.')
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
    typorgcod = models.CharField(max_length=12, verbose_name='Code type organisme')
    grppolart = models.CharField(max_length=60, blank=True, null=True, verbose_name='Article')
    grppolurlsim = models.CharField(max_length=255, blank=True, null=True, verbose_name='URL simplifiée (relative)')
    grppolurlcmp = models.CharField(max_length=255, blank=True, null=True, verbose_name='URL complète')
    grppolcodamelicou = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code transfert AMELI')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'grppol'


class Grpsenami(models.Model):
    typorgcod = models.CharField(max_length=12, verbose_name='Code type organisme')
    orgcod = models.CharField(primary_key=True, max_length=12, verbose_name='Code organisme')
    orgnumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    orgdatcre = models.DateTimeField(verbose_name='Date création')
    orgdatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    grpsenalf = models.CharField(max_length=5, blank=True, null=True, verbose_name='Membre APF')
    scnorgcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code organisme')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    orgart = models.CharField(max_length=60, blank=True, null=True, verbose_name='Article')
    grpsenweb = models.CharField(max_length=12, blank=True, null=True, verbose_name='Edition WEB')
    typgrpsencod = models.CharField(max_length=12, verbose_name='Code type groupe')
    orgurlsim = models.CharField(max_length=255, blank=True, null=True, verbose_name='URL simplifié')
    orgurlcmp = models.CharField(max_length=255, blank=True, null=True, verbose_name='URL complet')
    comorgcod = models.CharField(max_length=12, verbose_name='Code organisme')
    orgtemannu = models.CharField(max_length=12, blank=True, null=True, verbose_name='Témoin transfert ANNUAIRE')
    plaindcod = models.CharField(max_length=12)
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')
    type_com_neant = models.CharField(max_length=12, blank=True, null=True, verbose_name="Pour les groupes non rattachés à une commission (COMORGCOD='NEANT') précise le type spécial de groupe : - HORSCOM : groupe hors commission (intergroupe par exemple) - TOUTCOM : groupe rattaché à plusieurs commissions (nouveau besoin 01/2018)")

    class Meta:
        managed = False
        db_table = 'grpsenami'


class Libcom(models.Model):
    orgcod = models.CharField(max_length=12, verbose_name='Code organisme')
    libcomdatdeb = models.DateTimeField(verbose_name='Date début')
    libcomdatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date fin')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=500, blank=True, null=True, verbose_name='Libellé long')
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
    orgcod = models.CharField(max_length=12, verbose_name='Code organisme')
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
    grppolcod = models.CharField(max_length=12, verbose_name='Code groupe politique 4e Rép.')
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


class Libgrpsen(models.Model):
    orgcod = models.CharField(max_length=12, verbose_name='Code organisme')
    libgrpsendatautbur = models.DateTimeField(verbose_name="Date d'autorisation bureau")
    libgrpsendatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    libgrpsenlib = models.CharField(max_length=120, verbose_name='Libellé groupe sénatorial')
    libgrpsenlic = models.CharField(max_length=60, verbose_name='Libellé court')
    libgrpsenlil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')
    libgrpsenid = models.BigIntegerField(primary_key=True)
    libgrpsenart = models.CharField(max_length=60, blank=True, null=True, verbose_name='Article')

    class Meta:
        managed = False
        db_table = 'libgrpsen'
        unique_together = (('orgcod', 'libgrpsendatautbur'),)


class Liborg(models.Model):
    orgcod = models.CharField(max_length=12, verbose_name='Code organisme')
    liborgdatdeb = models.DateTimeField(verbose_name='Date de début')
    liborgdatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    liborgart = models.CharField(max_length=60, blank=True, null=True, verbose_name='Article')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')
    liborgid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')

    class Meta:
        managed = False
        db_table = 'liborg'
        unique_together = (('orgcod', 'liborgdatdeb'),)


class Mel(models.Model):
    melid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant Mel')
    poiconid = models.BigIntegerField(verbose_name='Identifiant point de contact')
    melema = models.CharField(max_length=255, blank=True, null=True, verbose_name='Adresse Mel')
    melnumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mel'


class Memcom(models.Model):
    memcomid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    orgcod = models.CharField(max_length=12, verbose_name='Code organisme')
    memcomdatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date de début')
    memcomdatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    senmat = models.CharField(max_length=6, verbose_name='Matricule')
    memcomtitsup = models.CharField(max_length=12, blank=True, null=True, verbose_name='Titulaire/Suppléant')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'memcom'


class Memdelega(models.Model):
    memdelegaid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    orgcod = models.CharField(max_length=12, verbose_name='Code organisme')
    memdelegadatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date de début')
    memdelegadatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    senmat = models.CharField(max_length=6, verbose_name='Matricule')
    designcod = models.CharField(max_length=12, verbose_name='Code désignataire')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'memdelega'


class Memextpar(models.Model):
    memextparid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    orgcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code organisme')
    memextpardatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date de Debut')
    memextpardatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    memextpartitsup = models.CharField(max_length=12, blank=True, null=True, verbose_name='Titulaire Suppleant')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    senmat = models.CharField(max_length=6, verbose_name='Matricule')
    memextparrngele = models.BigIntegerField(blank=True, null=True)
    designcod = models.CharField(max_length=12, verbose_name='Code désignataire')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')
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
    memgrppolid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    grppolcod = models.CharField(max_length=12, verbose_name='Code groupe politique 4e Rép.')
    typapppolcod = models.CharField(max_length=1, verbose_name='Code type appartenance')
    memgrppoldatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date de début')
    memgrppoldatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    senmat = models.CharField(max_length=6, verbose_name='Matricule')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'memgrppol'


class Memgrpsen(models.Model):
    memgrpsenid = models.BigIntegerField(primary_key=True)
    orgcod = models.CharField(max_length=12, verbose_name='Code organisme')
    memgrpsendatent = models.DateTimeField()
    memgrpsendatsor = models.DateTimeField()
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    senmat = models.CharField(max_length=6, verbose_name='Matricule')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'memgrpsen'


class Memorg(models.Model):
    memorgid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    senmat = models.CharField(max_length=6, verbose_name='Matricule')
    orgcod = models.CharField(max_length=12, verbose_name='Code organisme')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    memorgdatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date de début')
    memorganndeb = models.BigIntegerField(blank=True, null=True, verbose_name='Année de début')
    memorgdatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    memorgannfin = models.BigIntegerField(blank=True, null=True, verbose_name='Année de fin')
    designcod = models.CharField(max_length=12, verbose_name='Code désignataire')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'memorg'


class Minind(models.Model):
    minid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    senmat = models.CharField(max_length=6, blank=True, null=True, verbose_name='Matricule')
    typmincod = models.CharField(max_length=12)
    gvtid = models.BigIntegerField()
    memgvtrngprt = models.BigIntegerField(blank=True, null=True)
    mindatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date Nomination')
    minanndeb = models.BigIntegerField(blank=True, null=True, verbose_name='Année début')
    mindatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date fin fonctions')
    minannfin = models.BigIntegerField(blank=True, null=True, verbose_name='Année fin')
    mincirfin = models.CharField(max_length=120, blank=True, null=True, verbose_name='Circ fin fon')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    titmincod = models.CharField(max_length=12)
    mindel = models.CharField(max_length=12, blank=True, null=True, verbose_name='Ministre délégué')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')
    poicon = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'minind'


class Mismin(models.Model):
    misid = models.BigIntegerField(verbose_name='Identifiant Mission')
    minid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant Ministre')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'mismin'
        unique_together = (('minid', 'misid'),)


class Missen(models.Model):
    misid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    senmat = models.CharField(max_length=6, verbose_name='Matricule')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'missen'
        unique_together = (('misid', 'senmat'),)


class Moddes(models.Model):
    moddescod = models.CharField(primary_key=True, max_length=12, verbose_name='Code')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    moddesnumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')
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
    zongeocod = models.CharField(max_length=12, verbose_name='Code zone géographique')
    nationliccap = models.CharField(max_length=60, blank=True, null=True)
    nationlictri = models.CharField(max_length=60, blank=True, null=True)
    nationurlcmp = models.CharField(max_length=255, blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'nation'


class Nationgrpsen(models.Model):
    nationgrpsenid = models.BigIntegerField(primary_key=True)
    orgcod = models.CharField(max_length=12, verbose_name='Code organisme')
    nationcod = models.CharField(max_length=12)
    nationgpsendatdeb = models.DateTimeField(blank=True, null=True)
    nationgrpsendatfin = models.DateTimeField(blank=True, null=True)
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'nationgrpsen'


class Org(models.Model):
    typorgcod = models.CharField(max_length=12, verbose_name='Code type organisme')
    orgcod = models.CharField(primary_key=True, max_length=12, verbose_name='Code organisme')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    orgart = models.CharField(max_length=60, blank=True, null=True, verbose_name='Article')
    orgnumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    orgdatcre = models.DateTimeField(blank=True, null=True, verbose_name='Date création')
    orgdatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    orgurlsim = models.CharField(max_length=255, blank=True, null=True, verbose_name='URL simplifié')
    orgurlcmp = models.CharField(max_length=255, blank=True, null=True, verbose_name='URL complet')
    orgregjur = models.CharField(max_length=255, blank=True, null=True, verbose_name='Régime juridique')
    orgmoddes = models.CharField(max_length=255, blank=True, null=True, verbose_name='Mode désignation')
    orgmemdep = models.CharField(max_length=12, blank=True, null=True, verbose_name='Membres Députés')
    orgtemannu = models.CharField(max_length=12, blank=True, null=True, verbose_name='Témoin transfert ANNUAIRE')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'org'


class Orgext(models.Model):
    typorgcod = models.CharField(max_length=12, verbose_name='Code type organisme')
    orgcod = models.CharField(primary_key=True, max_length=12, verbose_name='Code organisme')
    orgnumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    orgdatcre = models.DateTimeField(blank=True, null=True, verbose_name='Date création')
    orgdatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    orgnumtie = models.CharField(max_length=12, blank=True, null=True, verbose_name='NuméroTiers')
    orgextregjur = models.CharField(max_length=500, blank=True, null=True, verbose_name='Régime juridique')
    orgextrubclas = models.CharField(max_length=255, blank=True, null=True, verbose_name='Rubrique de classement (obsolète)')
    orgextnbrsen = models.BigIntegerField(blank=True, null=True, verbose_name='Nombre de représentants')
    orgextdurman = models.CharField(max_length=120, blank=True, null=True, verbose_name='Durée du mandat')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    orgart = models.CharField(max_length=60, blank=True, null=True, verbose_name='Article')
    orgextmoddes = models.CharField(max_length=500, blank=True, null=True, verbose_name='Mode de désignation')
    orgextminrat = models.CharField(max_length=120, blank=True, null=True, verbose_name='Ministère de rattachement')
    orgextrep = models.CharField(max_length=255, blank=True, null=True, verbose_name='Représentants')
    orgurlsim = models.CharField(max_length=255, blank=True, null=True, verbose_name='URL simplifié')
    orgurlcmp = models.CharField(max_length=255, blank=True, null=True, verbose_name='URL complet')
    orgtemannu = models.CharField(max_length=12, blank=True, null=True, verbose_name='Témoin transfert ANNUAIRE')
    stajurcod = models.CharField(max_length=12, verbose_name='Code')
    etaprrcod = models.CharField(max_length=12, verbose_name='Code')
    orgextdatprr = models.DateTimeField(blank=True, null=True, verbose_name='Date de décrêt de prorogation')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')
    basdescod = models.CharField(max_length=12, verbose_name='Code')
    orgparite = models.CharField(max_length=12, blank=True, null=True, verbose_name='Parité')
    typorgextcod = models.CharField(max_length=64)
    orgextprescod = models.CharField(max_length=20)
    codesgg = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgext'


class Orgthe(models.Model):
    orgcod = models.CharField(max_length=12, verbose_name='Code organisme')
    thecle = models.SmallIntegerField(verbose_name='Clé')

    class Meta:
        managed = False
        db_table = 'orgthe'
        unique_together = (('thecle', 'orgcod'),)


class Pcs(models.Model):
    pcscod = models.CharField(primary_key=True, max_length=4, verbose_name='Code PCS')
    pcslil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé')
    pcs42cod = models.CharField(max_length=2, verbose_name='Code PCS42')

    class Meta:
        managed = False
        db_table = 'pcs'


class Pcs24(models.Model):
    pcs24cod = models.CharField(primary_key=True, max_length=2, verbose_name='Code PCS24')
    pcs24lib = models.CharField(max_length=95, blank=True, null=True, verbose_name='Libellé')
    pcs8cod = models.CharField(max_length=1, verbose_name='Code PCS8')

    class Meta:
        managed = False
        db_table = 'pcs24'


class Pcs42(models.Model):
    pcs42cod = models.CharField(primary_key=True, max_length=2, verbose_name='Code PCS42')
    pcs42lib = models.CharField(max_length=84, blank=True, null=True, verbose_name='Libellé')
    pcs24cod = models.CharField(max_length=2, verbose_name='Code PCS24')

    class Meta:
        managed = False
        db_table = 'pcs42'


class Pcs8(models.Model):
    pcs8cod = models.CharField(primary_key=True, max_length=1, verbose_name='Code PCS8')
    pcs8lil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé')

    class Meta:
        managed = False
        db_table = 'pcs8'


class Pcscatpro(models.Model):
    catprocod = models.CharField(max_length=12, verbose_name='Code catégorie professionnelle')
    pcscod = models.CharField(max_length=4, verbose_name='Code PCS')
    procatprodef = models.CharField(max_length=12, blank=True, null=True)
    pcscatproid = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'pcscatpro'


class Poicon(models.Model):
    poiconid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant point de contact')
    senmat = models.CharField(max_length=6, verbose_name='Matricule')
    typpoiconcod = models.CharField(max_length=12, verbose_name='Code type Point de contact')
    poiconlib = models.CharField(max_length=120, blank=True, null=True)
    poiconnumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poicon'


class Qua(models.Model):
    quacod = models.CharField(primary_key=True, max_length=12, verbose_name='Code qualité')
    qualic = models.CharField(max_length=60, verbose_name='Libellé court')
    quanumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
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
        db_table = 'qua'


class Reg(models.Model):
    regcod = models.CharField(primary_key=True, max_length=12, verbose_name='Code région')
    territcod = models.CharField(max_length=12, verbose_name='Code')
    reglib = models.CharField(max_length=120, verbose_name='Libellé région')
    regnumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    regcodparlis = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code transfert Parlis')
    artreg = models.CharField(max_length=60, blank=True, null=True, verbose_name='Article')
    regurlcmp = models.CharField(max_length=255, blank=True, null=True, verbose_name='URL')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')
    regcodrpl = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code région remplaçante')
    reglic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court région')
    reglil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long région')
    regdatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date début région')
    regdatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date fin région')
    regcodint = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reg'


class Sen(models.Model):
    senmat = models.CharField(primary_key=True, max_length=6, verbose_name='Matricule')
    quacod = models.CharField(max_length=12, verbose_name='Code qualité')
    sennomuse = models.CharField(max_length=40, verbose_name='Nom usuel')
    sennomtec = models.CharField(unique=True, max_length=60, verbose_name='Nom technique (tris)')
    senprenomuse = models.CharField(max_length=60, verbose_name='Prénom usuel')
    sendatnai = models.DateTimeField(blank=True, null=True, verbose_name='Date de naissance')
    sendatdec = models.DateTimeField(blank=True, null=True, verbose_name='Date du décés')
    etasencod = models.CharField(max_length=12, verbose_name='Code état sénateur')
    sendespro = models.CharField(max_length=255, blank=True, null=True, verbose_name='Description Profession')
    pcscod = models.CharField(max_length=4, verbose_name='Code PCS')
    catprocod = models.CharField(max_length=12, verbose_name='Code catégorie professionnelle')
    sengrppolcodcou = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code groupe politique courant')
    sengrppolliccou = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé groupe politique courant')
    sentypappcou = models.CharField(max_length=60, blank=True, null=True, verbose_name='Appartenance politique courante')
    sencomcodcou = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code commission courante')
    sencomliccou = models.CharField(max_length=60, blank=True, null=True, verbose_name='Commission courante')
    sencirnumcou = models.BigIntegerField(blank=True, null=True, verbose_name='Identifiant circonscription')
    sencircou = models.CharField(max_length=120, blank=True, null=True, verbose_name='Circonscription courante')
    senburliccou = models.CharField(max_length=60, blank=True, null=True, verbose_name='Fonction bureau courante')
    senema = models.CharField(max_length=255, blank=True, null=True, verbose_name='Adresse électronique')
    sennomusecap = models.CharField(max_length=40, verbose_name='Nom usuel Capitales')
    senfem = models.CharField(max_length=12, blank=True, null=True, verbose_name='Féminisation fonctions')
    sennumsie = models.BigIntegerField(blank=True, null=True, verbose_name='N° de siège Hémicycle')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')
    sendaiurl = models.CharField(max_length=255, blank=True, null=True, verbose_name="URL des déclarations d'intérêts")

    class Meta:
        managed = False
        db_table = 'sen'
        unique_together = (('sennomuse', 'senprenomuse', 'sendatnai'),)


class Senbur(models.Model):
    senburid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    burcod = models.CharField(max_length=12, verbose_name='Code bureau 4e Rép.')
    senburdatdeb = models.DateTimeField(blank=True, null=True, verbose_name='Date de début')
    senburdatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    senburrelint = models.CharField(max_length=12, blank=True, null=True, verbose_name='Chargé Relations Internationales')
    senburrngele = models.BigIntegerField(blank=True, null=True, verbose_name="Rang d'élection")
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    senmat = models.CharField(max_length=6, verbose_name='Matricule')
    senburhon = models.CharField(max_length=12, blank=True, null=True, verbose_name='Honorariat')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'senbur'


class Sennom(models.Model):
    senmat = models.CharField(max_length=6, verbose_name='Matricule')
    sennomdatdeb = models.DateTimeField(verbose_name='Date de début')
    sennomdatfin = models.DateTimeField(blank=True, null=True, verbose_name='Date de fin')
    quacod = models.CharField(max_length=12, verbose_name='Code qualité')
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


class Senurl(models.Model):
    senurlid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant')
    senmat = models.CharField(max_length=6, verbose_name='Matricule')
    typurlcod = models.CharField(max_length=12, verbose_name='Code type URL')
    senurlurl = models.CharField(max_length=255, verbose_name='URL')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    senurlnumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'senurl'


class Stajur(models.Model):
    stajurcod = models.CharField(primary_key=True, max_length=12, verbose_name='Code')
    stajurlic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    stajurlib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    stajurnumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'stajur'


class Telephone(models.Model):
    telid = models.BigIntegerField(primary_key=True, verbose_name='Identifiant téléphone')
    typtelcod = models.CharField(max_length=12, verbose_name='Code type numéro de téléphone')
    poiconid = models.BigIntegerField(verbose_name='Identifiant point de contact')
    telnum = models.CharField(max_length=15, blank=True, null=True, verbose_name='Numéro de tel')
    telnumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    syscredat = models.DateTimeField(blank=True, null=True)
    sysmajdat = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'telephone'


class Temval(models.Model):
    temvalcod = models.CharField(primary_key=True, max_length=12, verbose_name='Code validité')
    temvallic = models.CharField(max_length=60, verbose_name='Libellé court')
    temvallib = models.CharField(max_length=120, verbose_name='Libellé')

    class Meta:
        managed = False
        db_table = 'temval'


class Territ(models.Model):
    territcod = models.CharField(primary_key=True, max_length=12, verbose_name='Code')
    territlib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé territoire')
    territnumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Ordre de tri')
    territart = models.CharField(max_length=60, blank=True, null=True, verbose_name='Article')
    territurlcmp = models.CharField(max_length=255, blank=True, null=True, verbose_name='URL')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')
    catterritcod = models.CharField(max_length=12)
    territlic = models.CharField(max_length=60, blank=True, null=True)
    territlil = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'territ'


class Titele(models.Model):
    titelecod = models.CharField(primary_key=True, max_length=12, verbose_name='Code titre élu')
    titelelic = models.CharField(max_length=60)
    typmancod = models.CharField(max_length=12, verbose_name='Code type mandat')
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
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'titele'


class Typadr(models.Model):
    typadrcod = models.CharField(primary_key=True, max_length=12, verbose_name='Code type adresse')
    typadrlic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    typadrlib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    typadrnumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'typadr'


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


class Typbister(models.Model):
    typbistercod = models.CharField(primary_key=True, max_length=12, verbose_name='Code Type bis ter')
    typbisterlic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    typbisterlib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    typbisternumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')

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
    typelecod = models.CharField(primary_key=True, max_length=12, verbose_name='Code type élection')
    typelelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    typelelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    typelelil = models.CharField(max_length=500, blank=True, null=True, verbose_name='Libellé long')
    typelenumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'typele'


class Typgrpsen(models.Model):
    typgrpsencod = models.CharField(primary_key=True, max_length=12, verbose_name='Code type groupe')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    typgrpsennumtri = models.BigIntegerField(blank=True, null=True)
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'typgrpsen'


class Typman(models.Model):
    typmancod = models.CharField(primary_key=True, max_length=12, verbose_name='Code type mandat')
    typmanlib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé type mandat')
    typmantypele = models.CharField(max_length=12, blank=True, null=True, verbose_name="Type d'élection")
    typmannumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'typman'


class Typorg(models.Model):
    typorgcod = models.CharField(primary_key=True, max_length=12, verbose_name='Code type organisme')
    typorglib = models.CharField(max_length=120, verbose_name='Libellé')
    typorglic = models.CharField(max_length=60, verbose_name='Libellé court')
    typorgnumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    typorgurlsim = models.CharField(max_length=500, blank=True, null=True, verbose_name='URL simplifiée')
    typorgurlcmp = models.CharField(max_length=500, blank=True, null=True, verbose_name='URL complète')
    typorglibplu = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé pluriel')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'typorg'


class Typurl(models.Model):
    typurlcod = models.CharField(primary_key=True, max_length=12, verbose_name='Code type URL')
    temvalcod = models.CharField(max_length=12, blank=True, null=True, verbose_name='Code validité')
    evelic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    evelib = models.CharField(max_length=120, blank=True, null=True, verbose_name='Libellé')
    evelil = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé long')
    eveobs = models.CharField(max_length=255, blank=True, null=True, verbose_name='Observations')
    typurllogo = models.CharField(max_length=255, blank=True, null=True, verbose_name='Logo')
    typurlnumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    typurllogoref = models.CharField(max_length=255, blank=True, null=True, verbose_name='Logo refonte')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'typurl'


class Typvoi(models.Model):
    typvoicod = models.CharField(primary_key=True, max_length=12, verbose_name='Code type de voie')
    typvoilic = models.CharField(max_length=60, blank=True, null=True, verbose_name='Libellé court')
    typvoilib = models.CharField(max_length=255, blank=True, null=True, verbose_name='Libellé')
    typvoinumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')

    class Meta:
        managed = False
        db_table = 'typvoi'


class Zongeo(models.Model):
    zongeocod = models.CharField(primary_key=True, max_length=12, verbose_name='Code zone géographique')
    concod = models.CharField(max_length=12, verbose_name='Code continent')
    zongeolib = models.CharField(max_length=120, verbose_name='Libellé')
    zongeolic = models.CharField(max_length=60, verbose_name='Libellé court')
    zongeonumtri = models.BigIntegerField(blank=True, null=True, verbose_name='Numéro de tri')
    syscredat = models.DateTimeField(blank=True, null=True, verbose_name='Date système création')
    sysmajdat = models.DateTimeField(blank=True, null=True, verbose_name='Date système modification')

    class Meta:
        managed = False
        db_table = 'zongeo'

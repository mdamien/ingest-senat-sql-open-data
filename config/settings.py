from .base_settings import *

INSTALLED_APPS += [
	'senat_dosleg',
	'senat_debats',
	'senat_ameli',
	'django_extensions'
]

DATABASE_ROUTERS = [
	'senat_dosleg.dbrouter.SenatDoslegDBRouter'
	'senat_debat.dbrouter.SenatDebatsDBRouter'
	'senat_debat.dbrouter.SenatAmeliDBRouter'
]

DATABASES['db_senat_dosleg'] ={
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'senat_opendata_dosleg',
    'USER': 'postgres',
    'PASSWORD': 'password',
}

DATABASES['db_senat_debats'] ={
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'senat_opendata_debats',
    'USER': 'postgres',
    'PASSWORD': 'password',
}

DATABASES['db_senat_ameli'] ={
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'senat_opendata_ameli',
    'USER': 'postgres',
    'PASSWORD': 'password',
}
from .base_settings import *

INSTALLED_APPS += [
	'senat_dosleg',
	'senat_debats',
    'senat_ameli',
    'senat_sens',
    'senat_questions',
	'django_extensions'
]

DATABASE_ROUTERS = [
	'senat_dosleg.dbrouter.SenatDoslegDBRouter',
	'senat_debats.dbrouter.SenatDebatsDBRouter',
    'senat_ameli.dbrouter.SenatAmeliDBRouter',
    'senat_sens.dbrouter.SenatSensDBRouter',
    'senat_questions.dbrouter.SenatQuestionsDBRouter',
]

DATABASES['db_senat_dosleg'] = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'senat_opendata_dosleg',
    'USER': 'postgres',
    'PASSWORD': 'password',
}

DATABASES['db_senat_debats'] = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'senat_opendata_debats',
    'USER': 'postgres',
    'PASSWORD': 'password',
}

DATABASES['db_senat_ameli'] = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'senat_opendata_ameli',
    'USER': 'postgres',
    'PASSWORD': 'password',
}

DATABASES['db_senat_sens'] = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'senat_opendata_sens',
    'USER': 'postgres',
    'PASSWORD': 'password',
}

DATABASES['db_senat_questions'] = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'senat_opendata_questions',
    'USER': 'postgres',
    'PASSWORD': 'password',
}
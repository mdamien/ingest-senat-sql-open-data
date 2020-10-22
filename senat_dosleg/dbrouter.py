class SenatDoslegDBRouter(object):
    """
    A router to control senat_dosleg db operations
    """
    def db_for_read(self, model, **hints):
        "Point all operations on senat_dosleg models to 'db_senat_dosleg'"
        from django.conf import settings
        if not 'db_senat_dosleg' in settings.DATABASES:
            return None
        if model._meta.app_label == 'senat_dosleg':
            return 'db_senat_dosleg'
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on senat_dosleg models to 'db_senat_dosleg'"
        from django.conf import settings
        if not 'db_senat_dosleg' in settings.DATABASES:
            return None
        if model._meta.app_label == 'senat_dosleg':
            return 'db_senat_dosleg'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in senat_dosleg is involved"
        from django.conf import settings
        if not 'db_senat_dosleg' in settings.DATABASES:
            return None
        if obj1._meta.app_label == 'senat_dosleg' or obj2._meta.app_label == 'senat_dosleg':
            return True
        return None

    def allow_syncdb(self, db, model):
        "Make sure the senat_dosleg app only appears on the 'senat_dosleg' db"
        from django.conf import settings
        if not 'db_senat_dosleg' in settings.DATABASES:
            return None
        if db == 'db_senat_dosleg':
            return model._meta.app_label == 'senat_dosleg'
        elif model._meta.app_label == 'senat_dosleg':
            return False
        return None
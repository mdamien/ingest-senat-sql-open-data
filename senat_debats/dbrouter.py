class SenatDebatsDBRouter(object):
    """
    A router to control senat_debats db operations
    """
    def db_for_read(self, model, **hints):
        "Point all operations on senat_debats models to 'db_senat_debats'"
        from django.conf import settings
        if not 'db_senat_debats' in settings.DATABASES:
            return None
        if model._meta.app_label == 'senat_debats':
            return 'db_senat_debats'
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on senat_debats models to 'db_senat_debats'"
        from django.conf import settings
        if not 'db_senat_debats' in settings.DATABASES:
            return None
        if model._meta.app_label == 'senat_debats':
            return 'db_senat_debats'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in senat_debats is involved"
        from django.conf import settings
        if not 'db_senat_debats' in settings.DATABASES:
            return None
        if obj1._meta.app_label == 'senat_debats' or obj2._meta.app_label == 'senat_debats':
            return True
        return None

    def allow_syncdb(self, db, model):
        "Make sure the senat_debats app only appears on the 'senat_debats' db"
        from django.conf import settings
        if not 'db_senat_debats' in settings.DATABASES:
            return None
        if db == 'db_senat_debats':
            return model._meta.app_label == 'senat_debats'
        elif model._meta.app_label == 'senat_debats':
            return False
        return None
class SenatAmeliDBRouter(object):
    """
    A router to control senat_ameli db operations
    """
    def db_for_read(self, model, **hints):
        "Point all operations on senat_ameli models to 'db_senat_ameli'"
        from django.conf import settings
        if not 'db_senat_ameli' in settings.DATABASES:
            return None
        if model._meta.app_label == 'senat_ameli':
            return 'db_senat_ameli'
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on senat_ameli models to 'db_senat_ameli'"
        from django.conf import settings
        if not 'db_senat_ameli' in settings.DATABASES:
            return None
        if model._meta.app_label == 'senat_ameli':
            return 'db_senat_ameli'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in senat_ameli is involved"
        from django.conf import settings
        if not 'db_senat_ameli' in settings.DATABASES:
            return None
        if obj1._meta.app_label == 'senat_ameli' or obj2._meta.app_label == 'senat_ameli':
            return True
        return None

    def allow_syncdb(self, db, model):
        "Make sure the senat_ameli app only appears on the 'senat_ameli' db"
        from django.conf import settings
        if not 'db_senat_ameli' in settings.DATABASES:
            return None
        if db == 'db_senat_ameli':
            return model._meta.app_label == 'senat_ameli'
        elif model._meta.app_label == 'senat_ameli':
            return False
        return None
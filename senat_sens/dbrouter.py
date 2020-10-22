class SenatSensDBRouter(object):
    """
    A router to control senat_sens db operations
    """
    def db_for_read(self, model, **hints):
        "Point all operations on senat_sens models to 'db_senat_sens'"
        from django.conf import settings
        if not 'db_senat_sens' in settings.DATABASES:
            return None
        if model._meta.app_label == 'senat_sens':
            return 'db_senat_sens'
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on senat_sens models to 'db_senat_sens'"
        from django.conf import settings
        if not 'db_senat_sens' in settings.DATABASES:
            return None
        if model._meta.app_label == 'senat_sens':
            return 'db_senat_sens'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in senat_sens is involved"
        from django.conf import settings
        if not 'db_senat_sens' in settings.DATABASES:
            return None
        if obj1._meta.app_label == 'senat_sens' or obj2._meta.app_label == 'senat_sens':
            return True
        return None

    def allow_syncdb(self, db, model):
        "Make sure the senat_sens app only appears on the 'senat_sens' db"
        from django.conf import settings
        if not 'db_senat_sens' in settings.DATABASES:
            return None
        if db == 'db_senat_sens':
            return model._meta.app_label == 'senat_sens'
        elif model._meta.app_label == 'senat_sens':
            return False
        return None
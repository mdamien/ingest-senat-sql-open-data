class SenatQuestionsDBRouter(object):
    """
    A router to control senat_questions db operations
    """
    def db_for_read(self, model, **hints):
        "Point all operations on senat_questions models to 'db_senat_questions'"
        from django.conf import settings
        if not 'db_senat_questions' in settings.DATABASES:
            return None
        if model._meta.app_label == 'senat_questions':
            return 'db_senat_questions'
        return None

    def db_for_write(self, model, **hints):
        "Point all operations on senat_questions models to 'db_senat_questions'"
        from django.conf import settings
        if not 'db_senat_questions' in settings.DATABASES:
            return None
        if model._meta.app_label == 'senat_questions':
            return 'db_senat_questions'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in senat_questions is involved"
        from django.conf import settings
        if not 'db_senat_questions' in settings.DATABASES:
            return None
        if obj1._meta.app_label == 'senat_questions' or obj2._meta.app_label == 'senat_questions':
            return True
        return None

    def allow_syncdb(self, db, model):
        "Make sure the senat_questions app only appears on the 'senat_questions' db"
        from django.conf import settings
        if not 'db_senat_questions' in settings.DATABASES:
            return None
        if db == 'db_senat_questions':
            return model._meta.app_label == 'senat_questions'
        elif model._meta.app_label == 'senat_questions':
            return False
        return None
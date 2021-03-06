SECRET_KEY = 'secret_key'
SOUTH_TESTS_MIGRATE = True

TESTING = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
   }
}


MIDDLEWARE_CLASSES = ()

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'notifications',
)

ROOT_URLCONF = 'notifications.urls'


# Need to skip migrations for now as migrations created with python2 break with python3
# See https://code.djangoproject.com/ticket/23455
class DisableMigrations(object):
    def __contains__(self, item):
        return True
    def __getitem__(self, item):
        return "notmigrations"

MIGRATION_MODULES = DisableMigrations()


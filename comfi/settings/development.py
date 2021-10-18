from .base import *
import dj_database_url
import django_heroku

DEBUG = True
ALLOWED_HOSTS = ['*']




AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

# DATABASES = {
#     'default': dj_database_url.config()
        
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'floyddipela',
        'USER': 'floyddipela',
        'PASSWORD': '',
        'HOST': '',
        'POST': '5432',
    },
        'postgresql': dj_database_url.config()
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'heroku_9c9d4095a655b98',
#         'USER': 'b93b0ad0a2825c',
#         'PASSWORD': '98a7f30e',
#         'HOST': 'us-cdbr-east-04.cleardb.com',
#         'POST': '3306',
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
# db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
# DATABASES['default'].update(db_from_env)

STRIPE_PUBLIC_KEY = config('STRIPE_TEST_PUBLIC_KEY')
STRIPE_SECRET_KEY = config('STRIPE_TEST_SECRET_KEY')
django_heroku.settings(locals())
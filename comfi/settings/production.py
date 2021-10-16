from .base import *
from decouple import config
import django_heroku
import dj_database_url
DEBUG = True



# ALLOWED_HOSTS = ['ip-address','0.0.0.0', 'hevitall.herokuapp.com']
ALLOWED_HOSTS = ['*']

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]
DATABASES = {
    'default': dj_database_url.config()
        
    }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'heroku_c629df9e9cbd489',
#         'USER': 'b39cb79fa33c24',
#         'PASSWORD': 'fcbdfe31',
#         'HOST': 'us-cdbr-east-04.cleardb.com',
#         'POST': '3367',
#     }
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'dbtn7m6jn38nqt',
#         'USER': 'qndbsixuflnbup',
#         'PASSWORD': 'cf485536387b0ec4a458405ab8bf88ba0a201e26c6b299641e8f29dc4194447e',
#         'HOST': 'ec2-52-87-123-108.compute-1.amazonaws.com',
#         'PORT': '5432',
#     }
# }
# # import dj_database_url
# # db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
# # DATABASES['default'].update(db_from_env)


# STRIPE_PUBLIC_KEY = config('STRIPE_LIVE_PUBLIC_KEY')
# STRIPE_SECRET_KEY = config('STRIPE_LIVE_SECRET_KEY')
django_heroku.settings(locals())
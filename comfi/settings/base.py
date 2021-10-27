import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))


SECRET_KEY=config("SECRET_KEY")


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'django_countries',
    'rope',

    'cloudinary_storage',
    'cloudinary',
    # 'allauth.socialaccount.providers.vk',  # if you need VK api
    'allauth.socialaccount.providers.facebook', # if you need FB api
    # 'allauth.socialaccount.providers.google',
    

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'comfi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
            ],
        },
    },
]


WSGI_APPLICATION = 'comfi.wsgi.application'



LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'facebook':
     
        {
         'METHOD': 'oauth2',
         'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
         'SCOPE': ['email', 'public_profile'],
         'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
         'INIT_PARAMS': {'cookie': True},
         'FIELDS': [
             'id',
             'first_name',
             'last_name',
             'name',
             'name_format',
             'picture',
             'short_name'
         ],
         'EXCHANGE_TOKEN': True,
         'LOCALE_FUNC': lambda request: 'ru_RU',
         'VERIFIED_EMAIL': False,
         'VERSION': 'v7.0',
         # you should fill in 'APP' only if you don't create a Facebook instance at /admin/socialaccount/socialapp/
         'APP': {
             'client_id': '834810577213058',  # !!! THIS App ID
             'secret': '8499919a6c473d1192c50603203af535',  # !!! THIS App Secret
             'key': ''
                }
         }
}


# SOCIALACCOUNT_PROVIDERS = {
#     'google':
     
#         {
         
#          'SCOPE': ['email', 'profile'],
#          'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
#          'INIT_PARAMS': {'cookie': True},
#          'FIELDS': [
#              'id',
#              'first_name',
#              'last_name',
#              'name',
#              'name_format',
#              'picture',
#              'short_name'
#          ],
#          'EXCHANGE_TOKEN': True,
#          'LOCALE_FUNC': lambda request: 'ru_RU',
#          'VERIFIED_EMAIL': False,
#          'VERSION': 'v7.0',
#          # you should fill in 'APP' only if you don't create a Facebook instance at /admin/socialaccount/socialapp/
#          'APP': {
#              'client_id': '320992521656-3okhuvq2id6unqeecal0m422pq3uq037.apps.googleusercontent.com',  # !!! THIS App ID
#              'secret': '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',  # !!! THIS App Secret
#              'key': ''
#                 }
#          }
# }
# SITE_ID = 2
# LOGIN_REDIRECT_URL = '/'

# # Additional configuration settings
# SOCIALACCOUNT_QUERY_EMAIL = True
# ACCOUNT_LOGOUT_ON_GET= True
# ACCOUNT_UNIQUE_EMAIL = True
# ACCOUNT_EMAIL_REQUIRED = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUD_NAME'),
    'CLOUD_API_KEY': config('CLOUD_API_KEY'),
    'API_SECRET': config('API_SECRET'),
}

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')

# Auth

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)
SITE_ID = 1
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = False # a personal preference. True by default. I don't want users to be interrupted by logging in
# ACCOUNT_AUTHENTICATION_METHOD = 'email'  # a personal preference. I don't want to add 'i don't remember my username' like they did at Nintendo, it's stupid

ACCOUNT_LOGIN_ON_PASSWORD_RESET = True  # False by default
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True  # True by default
# ACCOUNT_LOGOUT_REDIRECT_URL = '/login'
ACCOUNT_USERNAME_BLACKLIST = ['suka', 'blyat',]  # :D
ACCOUNT_USERNAME_MIN_LENGTH = 4  # a personal preference
ACCOUNT_SESSION_REMEMBER = True  # None by default (to ask 'Remember me?'). I want the user to be always logged in



ACCOUNT_EMAIL_VERIFICATION = "none"
LOGIN_REDIRECT_URL = '/'

# CRISPY FORMS

CRISPY_TEMPLATE_PACK = 'bootstrap4'


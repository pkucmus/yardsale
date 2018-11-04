import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'vp)gy*xy*ezf*9efo#1t3zao%ecyp4jz94sk)gb_g@hk%!r^y2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS'].split(',')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'bootstrapform',
    'sorl.thumbnail',
    'django_classified',
    'snipeit',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'service.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_classified.context_processors.common_values',
            ],
        },
    },
]

WSGI_APPLICATION = 'service.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['YARDSALE_DATABASE_NAME'],
        'USER': os.environ['YARDSALE_DATABASE_USER'],
        'PASSWORD': os.environ['YARDSALE_DATABASE_PASSWORD'],
        'HOST': os.environ['YARDSALE_DATABASE_HOST'],
        'PORT': os.environ['YARDSALE_DATABASE_PORT'],
        'CONN_MAX_AGE': int(
            os.environ.get('YARDSALE_DATABASE_CONN_MAX_AGE', 20000)
        ),
    }
}


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join('/', 'shared', 'static')
MEDIA_ROOT = os.path.join('/', 'shared', 'media')

THUMBNAIL_CACHE_TIMEOUT = 3600 * 24 * 365
THUMBNAIL_DEBUG = True
THUMBNAIL_PREFIX = 'cache/'

# Email backend setup
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_PORT = int(os.environ['EMAIL_PORT'])
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_FROM = os.environ['EMAIL_FROM']

SNIPEIT_URL = os.environ['SNIPEIT_URL']
SNIPEIT_API_JWT = os.environ['SNIPEIT_API_JWT']

snipeit_verify = os.environ['SNIPEIT_HTTPS_VERIFY']

SNIPEIT_HTTPS_VERIFY = (
    False if snipeit_verify.lower() == 'false' else snipeit_verify
)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': (
                '%(levelname)s '
                '%(asctime)s '
                '%(module)s '
                '%(process)d '
                '%(thread)d '
                '%(message)s'
                '%(pathname)s:%(lineno)d'
            )
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': False
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG'
    }
}

SITE_ID = 1

DCF_CURRENCY = 'PLN'

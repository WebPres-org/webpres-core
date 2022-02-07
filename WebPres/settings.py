"""
WebPres project v1.
Generated by 'django-admin startproject' using Django 3.2.9.
By ronyman.com
"""
import os
import django_heroku
import sys
sys.modules['fontawesome_free'] = __import__('fontawesome-free')
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.core.files.storage import DefaultStorage
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Include BOOTSTRAP5_FOLDER in path
BOOTSTRAP5_FOLDER = os.path.abspath(os.path.join(BASE_DIR, "..", "bootstrap5"))
if BOOTSTRAP5_FOLDER not in sys.path:
    sys.path.insert(0, BOOTSTRAP5_FOLDER)



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = config("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ADMINS = ()
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'graphene_django',
    'bootstrap5',
    'core',
    'apps.hello_world',
    'apps.user',
    'crispy_forms',
    'fontawesome_free',
     'decouple',
    'blog',
    'storages',
     'grappelli',
    'filebrowser',

]

###Setting for Blog Pos
GRAPHENE = {
    'SCHEMA': 'blog.schema.schema'
}
###End Setting for Blog Pos

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'WebPres.urls'

###Add New
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "login"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'WebPres.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {'django.request': {'handlers': ['mail_admins'], 'level': 'ERROR', 'propagate': True}},
}

# Settings for django-bootstrap-v5
BOOTSTRAP5 = {
    'error_css_class': 'bootstrap5-error',
    'required_css_class': 'bootstrap5-required',
    'javascript_in_head': True,
}





STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
# Activate Django-Heroku.
django_heroku.settings(locals())

######
AWS_ACCESS_KEY_ID = os.environ.get('AKIAXBABVM7AK5AY24HW')
AWS_SECRET_ACCESS_KEY = os.environ.get('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')
AWS_STORAGE_BUCKET_NAME = 'ronyman'

AWS_DEFAULT_ACL = 'public-read'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None

STATICFILES_STORAGE = 'apps.user.storage.MediaStorage'
DEFAULT_FILE_STORAGE = 'apps.user.storage.MediaStorage'

STATIC_URL = 'http://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
######

# To set static for admin
#ADMIN_MEDIA_PREFIX = '/static/admin/'
#To allow django-admin collectstatic to automatically bellow:
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'



######
TINYMCE_JS_URL = os.path.join(STATIC_URL, "path/to/tiny_mce/tiny_mce.js")
TINYMCE_JS_ROOT = os.path.join(STATIC_ROOT, "path/to/tiny_mce")
TINYMCE_DEFAULT_CONFIG = {
    'height': 360,
    'width': 1120,
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
    }
#####
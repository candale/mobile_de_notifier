import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6rw)cbi=_1s)!dp6i3q^q&)e$80g2m9ng%+973zm152h&8-4a^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

APPLICATIONS_MODULE = 'apps'

# Make APPLICATIONS_MODULE folder available in the sys.path
sys.path.insert(0, os.path.join(BASE_DIR, APPLICATIONS_MODULE))


# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

OTHER_APPS = [
    'twitter_bootstrap',
]

MY_APPS = [
    'cars'
]

INSTALLED_APPS = DJANGO_APPS + OTHER_APPS + MY_APPS

# Project structure
APPS_DIR = os.path.join(BASE_DIR, "apps")
DATABASE_PATH = os.path.join(BASE_DIR, "db")
DATABASE_NAME = "cars.sqlite3"
DATABSE_ABS_PATH = os.path.join(DATABASE_PATH, DATABASE_NAME)

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SESION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
# Set one week cookie age
SESSION_COOKIE_AGE = 604800

ROOT_URLCONF = 'mobile_de_notifier.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "cars/templates"),
        ],
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

WSGI_APPLICATION = 'mobile_de_notifier.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABSE_ABS_PATH,
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

# Scheduler settings

# Frequency of scheduler polling in minutes
SCHEDULER_BEAT_INTERVAL = 5

# Used for resolving the path to python executable
RUNNING_IN_VIRTUALENV = True

SHEDUELR_SCRIPTS_DIRECTORY = os.path.join(BASE_DIR, 'scripts')

# The script that triggers the crawler and mail sending
SCHDEULER_SCRIPT_NAME = 'scheduler.py'

# The user whose crontab file will be used
CRONTAB_USER = 'root'

CRONTAB_ENTRY_COMMENT = "python_mobile_de_notifier_scheduler"

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

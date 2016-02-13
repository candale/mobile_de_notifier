import os
import pwd
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6rw)cbi=_1s)!dp6i3q^q&)e$80g2m9ng%+973zm152h&8-4a^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['212.47.248.43']

APPLICATIONS_MODULE = 'apps'

# Make APPLICATIONS_MODULE folder available in the sys.path
sys.path.insert(0, os.path.join(BASE_DIR, APPLICATIONS_MODULE))

# Make the scrapy project available for management commands
os.environ['SCRAPY_SETTINGS_MODULE'] = (
    'scrapers.cars_scraper.cars_scraper.settings'
)


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

]

MY_APPS = [
    'cars',
    'notifications'
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

LOGIN_REDIRECT_URL = '/searches'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
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
# Used for resolving the path to python executable
RUNNING_IN_VIRTUALENV = True

SHEDUELR_SCRIPTS_DIRECTORY = os.path.join(BASE_DIR, 'scripts')

# The script that triggers the crawler and mail sending
SCHDEULER_SCRIPT_NAME = 'scheduler.py'

# The user whose crontab file will be used
CRONTAB_USER = pwd.getpwuid(os.getuid())[0]

# Interval (in minutes) at which the crawler should run
CRAWLER_SCHEDULER_BEAT_INTERVAL = 10

# Interval (in minutes) at which the mailing should be run
MAILING_SCHEDULER_BEAT_INTERVAL = 20

# Comment by which the crawler cron job is recognized
CRONTAB_CRAWLER_ENTRY_COMMENT = 'python_mobile_de_notifier_scheduler_crawler'

# Comment by which the mailing cron job is recognized
CRONTAB_MAILING_ENTRY_COMMENT = 'python_mobile_de_notifier_scheduler_mailing'

# Scrapy
SCRAPERS_DIR = os.path.join(BASE_DIR, 'scrapers')
SCRAPY_PROJECT_ROOT = os.path.join(SCRAPERS_DIR, 'cars_scraper')
SPIDER_NAME = 'mobile_de'

# The address and password from which the mails will be sent
PROJECT_MAIL_ADDRESS = 'mobilede.noreply@gmail.com'
PROJECT_MAIL_PASS = 'scraperMobileDE'

# Mail settings
MAIL_ADDRESS = 'mobilede.noreply@gmail.com'
MAIL_PASSWORD = 'scraperMobileDE'

# Static files (CSS, JavaScript, Images)

STATIC_ROOT = 'static'
STATIC_URL = '/static/'

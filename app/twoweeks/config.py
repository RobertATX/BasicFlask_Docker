__author__ = 'davidlarrimore'
import os


######################
# ENVIRONMENT CONFIG #
######################
TRAP_BAD_REQUEST_ERRORS = True
CSRF_ENABLED = True
DEBUG = True
DEVELOPMENT = True
HOST = os.environ['HOST']
#NEW_RELIC_CONFIG_FILE = os.environ['NEW_RELIC_CONFIG_FILE']

SECRET_KEY = os.environ['FLASK_AUTH_SECRET_KEY']

###################
# DATABASE CONFIG #
###################
DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']
DATABASE_USERNAME = os.environ['DATABASE_USERNAME']
DATABASE_DATABASE = os.environ['DATABASE_DATABASE']
DATABASE_PORT = '3306'

ADMIN_USERNAME = os.environ['ADMIN_USERNAME']
ADMIN_PASSWORD = os.environ['ADMIN_PASSWORD']
ADMIN_EMAIL = os.environ['ADMIN_EMAIL']


TEST_DATABASE_HOSTNAME = 'dev.c6uo5ewdeq5k.us-east-1.rds.amazonaws.com'
DEV_DATABASE_HOSTNAME = 'mixfindb.c6uo5ewdeq5k.us-east-1.rds.amazonaws.com'
LOCAL_DATABASE_HOSTNAME = 'localhost'


if os.environ['APP_SETTINGS'] == 'TEST':
    DATABASE_HOSTNAME = TEST_DATABASE_HOSTNAME
elif os.environ['APP_SETTINGS'] == 'DEV':
    DATABASE_HOSTNAME = DEV_DATABASE_HOSTNAME
elif os.environ['APP_SETTINGS'] == 'DEVELOPMENT':
     DATABASE_HOSTNAME = DEV_DATABASE_HOSTNAME
elif os.environ['APP_SETTINGS'] == 'LOCAL':
     DATABASE_HOSTNAME = LOCAL_DATABASE_HOSTNAME
else:
    DATABASE_HOSTNAME = DEV_DATABASE_HOSTNAME

SQLALCHEMY_DATABASE_URI = 'mysql://'+DATABASE_USERNAME+':'+DATABASE_PASSWORD+'@'+DATABASE_HOSTNAME+':'+DATABASE_PORT+'/'+DATABASE_DATABASE





################
# EMAIL CONFIG #
################
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MAIL_DEFAULT_SENDER = 'admin@mixfin.com'



##################
# SESSION CONFIG #
##################
#Session Timeout in Minutes
PERMANENT_SESSION_LIFETIME = 200
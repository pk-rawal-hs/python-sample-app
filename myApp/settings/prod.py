from myApp.settings.base import *

DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')

#use postgres for production
'''
	To use postgres:
		If you are using Heroku -
			heroku pg:credentials:url
			and add fill the fields with appropiate values.

'''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}


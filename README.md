# Django-models
in this repository, we will try together to invade Django models and their integration with PostgreSQL 
-------------------------------------------------------------------------------------------------------
to integrate with postgresql you will have to do some steps ;
--------------------------------------------------------------
-first of all you have to install Postgresql engine with the command:
    pip install psycopg2 
this command will install Postgresql engine that will help you with Postgresql connection and data manipulation (ORM)
-second, we have to adjust the setting.py in our Project so go to setting.py and in the database list configuration you will put the information bellow :
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'test', #database name 
        'USER' : 'postgres', #database username
        'PASSWORD' : '' #PASTE YOUR PASSWORD HERE (Note* if you deactivate your password authentication you can remove password field)
        'HOST' : 'localhost', #host (if you are working with a local development server just type 'localhost' and if you are working with remote instanceyou will paste the instance ip here )
        'PORT' : '' #by default PostgreSQL is runnable on our machine on port 5432 if you left it blank it will work on the default port 
    }
}

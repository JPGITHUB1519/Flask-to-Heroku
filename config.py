import os


DEBUG = False
# shortened for readability
SECRET_KEY = '\xbf\xb0\x11\xb1\xcd\xf9\xba\x8bp\x0c...'
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
print SQLALCHEMY_DATABASE_URI

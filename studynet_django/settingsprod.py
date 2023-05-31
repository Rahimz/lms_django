from .settings import *


DEBUG = False
ALLOWED_HOSTS = ['api.aghareb.ir']
# settings to show images of course thumbnail
WEBSITE_URL = 'http://api.aghareb.ir'

CORS_ALLOWED_ORIGINS = [
    "http://aghareb.ir",
]

CSRF_TRUSTED_ORIGINS = [
    "http://aghareb.ir",
]
from .common import *
import os
import dj_database_url

DEBUG = False

SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = ["market-place-8hq1.onrender.com"]

DATABASES = {"default": dj_database_url.config()}

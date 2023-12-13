from .common import *
import os
import dj_database_url

DEBUG = False

DATABASE_URL = os.environ.get("DATABASE_URL")

SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = ["market-place-8hq1.onrender.com"]

RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

DATABASES = {
    "default": dj_database_url.config(
        # Feel free to alter this value to suit your needs.
        default=DATABASE_URL,
        conn_max_age=600,
    )
}

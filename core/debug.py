import os
from . import environ


# If .env file exist then it's development Environment
DEBUG = True
if environ.ENV.exist("DEBUG"):
  if str(environ.ENV.get("DEBUG")).lower() in ("0", "false", "no"):
    DEBUG = False
if environ.ENV.exist("PRODUCTION"):
  DEBUG = False

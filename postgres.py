import os
import logging
import psycopg2
import sqlalchemy
import subprocess
import sys


database_url = subprocess.run(["heroku config:get DATABASE_URL -a dfy-budget"], shell=True, capture_output=True, text=True)
os.environ["DATABASE_URL"] = str(database_url.stdout)



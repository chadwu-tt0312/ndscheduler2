"""Default settings."""

import logging
import os


#
# Development mode or production mode
# If DEBUG is True, then auto-reload is enabled, i.e., when code is modified, server will be
# reloaded immediately
#
DEBUG = True

#
# Static Assets
#
# The web UI is a single page app. All javascripts/css files should be in STATIC_DIR_PATH
#
STATIC_DIR_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)), "static")
TEMPLATE_DIR_PATH = STATIC_DIR_PATH
APP_INDEX_PAGE = "index.html"
WEBSITE_TITLE = "Scheduler"

#
# Server setup
#
HTTP_PORT = 7777
HTTP_ADDRESS = "127.0.0.1"

SSL_CERT = None
SSL_KEY = None

TORNADO_MAX_WORKERS = 8

#
# ApScheduler settings
#
THREAD_POOL_SIZE = 4
JOB_MAX_INSTANCES = 3
JOB_COALESCE = True
TIMEZONE = "UTC"

# When a job is misfired -- A job were to run at a specific time, but due to some
# reason (e.g., scheduler restart), we miss that run.
#
# By default, if a job is misfired within 1 hour, the scheduler will rerun it.
# Otherwise, if it's misfired over 1 hour, the scheduler will not rerun it.
JOB_MISFIRE_GRACE_SEC = 3600

#
# Database settings
#
JOBS_TABLENAME = "scheduler_jobs"
EXECUTIONS_TABLENAME = "scheduler_execution"
AUDIT_LOGS_TABLENAME = "scheduler_jobauditlog"

DATABASE_TABLENAMES = {
    "jobs_tablename": JOBS_TABLENAME,
    "executions_tablename": EXECUTIONS_TABLENAME,
    "auditlogs_tablename": AUDIT_LOGS_TABLENAME,
}

# See different database providers in ndscheduler/core/datastore/providers/

# SQLite
#
DATABASE_CLASS = "ndscheduler.corescheduler.datastore.providers.sqlite.DatastoreSqlite"
DATABASE_CONFIG_DICT = {"file_path": "datastore.db"}

# Postgres
#
# DATABASE_CLASS = 'ndscheduler.corescheduler.datastore.providers.postgres.DatastorePostgres'
# DATABASE_CONFIG_DICT = {
#     'user': 'username',
#     'password': '',
#     'hostname': 'localhost',
#     'port': 5432,
#     'database': 'scheduler',
#     'sslmode': 'disable'
# }

# MySQL
#
# DATABASE_CLASS = 'ndscheduler.corescheduler.datastore.providers.mysql.DatastoreMySQL'
# DATABASE_CONFIG_DICT = {
#     'user': 'username',
#     'password': '',
#     'hostname': 'localhost',
#     'port': 3306,
#     'database': 'scheduler'
# }

# ndscheduler is based on apscheduler. Here we can customize the apscheduler's main scheduler class
# Please see ndscheduler/core/scheduler/base.py
SCHEDULER_CLASS = "ndscheduler.corescheduler.core.base.BaseScheduler"

#
# Set logging level
#
logging.getLogger().setLevel(logging.INFO)


# Packages that contains job classes, e.g., simple_scheduler.jobs
JOB_CLASS_PACKAGES = []

# Secure Cookie Name
COOKIE_NAME = "user"
# Secure Cookie Hash
SECURE_COOKIE = "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__"
# Secure cookie age in days (decimals are supported)
COOKIE_MAX_AGE = 1

# Authentication
# To enable user authentication, modify the dict below
# e.g. AUTH_CREDENTIALS = {'username': 'password'}
# The pasword must be hashed using bcrypt (e.g. htpasswd -nbB userName userPassword)
AUTH_CREDENTIALS = {"user": "$2b$12$kdS48PJ4lN0AUkAPlKrSsepvmtZLhnAzbJhFTJPBIv71.Q8EvMFpi"}

# List of admin users
ADMIN_USER = ["user"]

HELP_URL = "https://github.com/palto42/ndscheduler/blob/develop/README.md"
ISSUES_URL = "https://github.com/palto42/ndscheduler/issues"

# Mail Server
MAIL_SERVER = []

# Server sender mail address
SERVER_MAIL = ""
ADMIN_MAIL = None

# LDAP server address in the format "ldap://my.ldap.server" "ldaps://my.ldap.server"
# Non-standard ports can be specified like "ldap://my.ldap.server:1234"
LDAP_SERVER = ""
# If "ldaps://" is used, specify of the SSL certificate should be verified
# Possible options are "demand", "allow" or "never"
LDAP_REQUIRE_CERT = "demand"
LDAP_CERT_DIR = None
LDAP_CERT_File = None
# Define LDAP dn format for login, {username} will be replaced with the entered user name
LDAP_LOGIN_DN = "uid={username},ou=users,dc=example,dc=com"
# List of permitted LDAP users. If none are specified, any authenticated used is allowed
LDAP_USERS = []

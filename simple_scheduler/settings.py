"""Settings to override default settings."""

import logging

#
# Override settings
#
DEBUG = True

HTTP_PORT = 8888
HTTP_ADDRESS = "127.0.0.1"

#
# Set logging level
#
logging.getLogger().setLevel(logging.DEBUG)

JOB_CLASS_PACKAGES = ["simple_scheduler.jobs"]

# Exclude specific jobs that require additional dependencies
EXCLUDE_JOB_CLASS_PACKAGES = ["apns_job"]
TIMEZONE = "Asia/Taipei"

# Secure Cookie Hash
# SECURE_COOKIE = "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__"
# Secure cookie age in days (decimals are supported)
# COOKIE_MAX_AGE = 1

# User authentication
#
# To enable user authentication, modify the dict below
# e.g. AUTH_CREDENTIALS = {'username': 'password'}
# The pasword must be hashed using bcrypt (e.g. htpasswd -nbB userName userPassword)
AUTH_CREDENTIALS = {"user": "$2b$12$kdS48PJ4lN0AUkAPlKrSsepvmtZLhnAzbJhFTJPBIv71.Q8EvMFpi"}

ADMIN_USER = "user"

# Email settings
SERVER_MAIL = ""
ADMIN_MAIL = None  # 設定為 None 表示不發送郵件通知

# 如果需要啟用郵件通知，請設定以下值：
# ADMIN_MAIL = "your-email@example.com"  # 管理員郵件地址
# SERVER_MAIL = "scheduler@your-domain.com"  # 發送者郵件地址
# MAIL_SERVER = ["smtp.your-domain.com", 587]  # SMTP 伺服器設定

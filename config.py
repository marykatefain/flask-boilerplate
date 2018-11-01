import os
env = os.environ.copy()

DEBUG = False

if 'SECRET_KEY' in env:
    SECRET_KEY = env['SECRET_KEY']

if 'ALLOWED_HOSTS' in env:
    ALLOWED_HOSTS = env['ALLOWED_HOSTS'].split(',')
else:
    ALLOWED_HOSTS = ['*']

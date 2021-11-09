import os
from pathlib import Path

# from dotenv import load_dotenv
from smart_getenv import getenv
from distutils.util import strtobool


basedir = os.path.abspath(os.path.dirname(__file__))
# load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = getenv('SECRET_KEY') or '004f2af45d3a4e161a7dd2d17fdae47f12s'
    JSON_SORT_KEYS = False
    LOG_TO_STDOUT = getenv('LOG_TO_STDOUT')

    timezone = getenv('TIMEZONE', default='Asia/Chongqing')
    DEBUG = getenv('DEBUG', default=False, type=bool)
    THREAD_NUM = getenv('THREAD_NUM', default=2)
    JSON_AS_ASCII = False
    APP_ROOT = os.getcwd()

    BOOTSTRAP_BTN_STYLE = 'primary'
    BOOTSTRAP_BTN_SIZE = 'sm'
    BOOTSTRAP_TABLE_VIEW_TITLE='Read'
    BOOTSTRAP_TABLE_EDIT_TITLE='Update'
    BOOTSTRAP_TABLE_DELETE_TITLE='Remove'
    BOOTSTRAP_TABLE_NEW_TITLE='Create'
import os

class Config(object):
  SECRET_KEY= os.environ.get('SECRET_KEY') or 'most-trusted-hypershit-110x-hungry-supercharged'

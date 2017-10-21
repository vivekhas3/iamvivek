from setuptools import setup

import os

# Put here required packages
packages = ['Django<=1.6',]

if 'REDISCLOUD_URL' in os.environ and 'REDISCLOUD_PORT' in os.environ and 'REDISCLOUD_PASSWORD' in os.environ:
     packages.append('django-redis-cache')
     packages.append('hiredis')

setup(name='viveks',
      version='1.0',
      description='My resume',
      author='Vivek',
      author_email='vivekhas3@gmail.com',
      url='http://viveks-scalesservice.rhcloud.com/',
      install_requires=packages,
)


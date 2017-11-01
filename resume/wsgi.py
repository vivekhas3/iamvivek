"""
WSGI config for tester project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append("/home/ec2-user/web/iamvivek/")
sys.path.append("/home/ec2-user/web/iamvivek/resume/wsgi/openshift/")
sys.path.append("/home/ec2-user/venv-27/lib/python2.7/site-packages/")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "resume.wsgi.openshift.settings")

from django.core.wsgi import get_wsgi_application
activate_env=os.path.expanduser("/home/ec2-user/venv-27/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

application = get_wsgi_application()






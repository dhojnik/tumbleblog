#!/usr/bin/python
import sys
import logging
activate_this = '/var/www/virtualenv/bin/activate_this.py'
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/webapp/tumbleblog")

from tumbleblog import app as application
application.secret_key = 'amo2joh0eeNi'

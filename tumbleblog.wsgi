import os
import sys
import site
 
# Add virtualenv site packages
site.addsitedir(os.path.join(os.path.dirname(__file__), '/var/www/virtualenv/lib/python3.5/site-packages/'))
 
# Path of execution
sys.path.append('/var/www/webapp')
 
# Fired up virtualenv before include application
activate_env = os.path.expanduser(os.path.join(os.path.dirname(__file__), '/var/www/virtualenv/bin/activate_this.py'))
execfile(activate_env, dict(__file__=activate_env))
 
# import my_flask_app as application
from tumbleblog import app as application

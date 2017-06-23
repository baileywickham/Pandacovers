import sys
sys.path.append('/var/www/html/Pandacovers')
from webtool import app as application
#wsgi script points the server (using mod_wsgi to view and run these scripts) to the actual python file we need to run
#then compiles it thats why there is a webtool.pyc
#from _____ is the name of the python file we want to serve. make sure to change this in /etc/apache2/sites-availble and use a2ensite
#to enable the new site. also add the virtualhost, but I am not sure how to redirect to that virtualhost

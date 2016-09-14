from scaffold.core.data.database import db

app_domain = 'http://localhost:5000'
app_email_template_path = 'templates/email/'

from_email = 'no-reply@maidstone-hackspace.org.uk'

flask_secret_key = '4466ae96-849f-4fbe-a469-3295bf1a13f5'

database = {
    'charset': 'utf8',
    'use_unicode': True,
    'type': 'mysql',
    'host': 'localhost',
    'user': 'root',
    'passwd': "",
    'db': "mydb",
    'port': 3306}


oauth_live = False
oauth_redirect_uri = app_domain + '/oauth'
oauth_conf = {
    'google': {},
    'github': {},
    'twitter': {}
}

import os 
# we can override the defaults by creating these settings files
if os.path.exists('config/settings_dev.py'):
    from settings_dev  import *

if os.path.exists('config/settings_testing.py'):
    from settings_live  import *

if os.path.exists('config/settings_live.py'):
    from settings_live  import *

db.config(database)

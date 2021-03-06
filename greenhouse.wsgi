#!/usr/bin/python
import sys 
import logging 
logging.basicConfig(stream=sys.stderr) 
sys.path.insert(0,"/var/www/Greenhouse-Website/") 
from Greenhouse-Website import app as application
application.secret_key = 'ij38y7gyevhbjf43uhvrgcy'

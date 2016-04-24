import cgi
import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2
import json

# ===================================== Server Classes(Controllers) ==================== #
class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('<html><body>')
        self.response.write('Hello')
        self.response.write('</body></html>')

class FishGear(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'application/json'   
        obj = {
  "fishgears": [
    {
      "id": 1, 
      "image": "SomeImageURL", 
      "lat": 51.5374, 
      "location_name": "Chalkwell Beach", 
      "long": 0.675081, 
      "title": "Fish Net Gear", 
      "warning": None
    }, 
    {
      "id": 2, 
      "image": "SomeImageURL", 
      "lat":  51.5365, 
      "location_name": "Chalkwell Beach", 
      "long": 0.6754, 
      "title": "Fish Net Gear", 
      "warning": None
    }, 
    {
      "id": 3, 
      "image": "SomeImageURL", 
      "lat": 51.54099, 
      "location_name": "Bell Wharf Beach", 
      "long": 0.64580, 
      "title": "Fish Net Gear", 
      "warning": None
    }, 
    {
      "id": 4, 
      "image": "SomeImageURL", 
      "lat": 51.5311, 
      "location_name": "California Beach", 
      "long": 0.64576, 
      "title": "Fish Net Gear", 
      "warning": None
    }
    ]
}
        self.response.out.write(json.dumps(obj))
        
        

app = webapp2.WSGIApplication([
	# Route tuples for application
	('/', MainPage),
    ('/fishgears/json', FishGear)
	], debug=True)
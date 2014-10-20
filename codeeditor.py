import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)

class MainPage(webapp2.RequestHandler):
	def get(self):
		if users.get_current_user():
			url = users.create_logout_url(self.request.uri)
			url_linktext = 'Logout'
		else:
			url = users.create_login_url(self.request.uri)
			url_linktext = 'Login'
		template_values={
			'url' :url,
			'url_linktext': url_linktext,
		}
		template = JINJA_ENVIRONMENT.get_template('index.html')
		self.response.write(template.render(template_values))

class CodeFile(ndb.Model):
	author = ndb.UserProperty()
	content = ndb.TextProperty(indexed=False)
	date = ndb.DateTimeProperty(auto_now_add=True)
	

application = webapp2.WSGIApplication([
	('/', MainPage),
], debug=True)

"""
	Pass JavaScript variable to Python
	Save into the database
	Load the file and display to the mainpage
	Design the interface
"""
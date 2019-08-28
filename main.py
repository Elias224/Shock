from google.appengine.ext import ndb
import jinja2
import os
import webapp2

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class RegisterHandler(webapp2.RequestHandler):
  def get(self):
      donation_template = the_jinja_env.get_template('donation.html')
      self.response.out.write(donation_template.render())
  def post(self):
      template1 = the_jinja_env.get_template('donation.html')
      Name = self.request.get('name')
      Email = self.request.get('email')
      Phone = self.request.get('phone')
      Item_description = self.request.get('item description')
      User = NewUser(Name=Name, Email=Email, Phone=Phone, Item_description=Item_description)
      User.put()
      self.response.out.write(donation_template.render())

class Home(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('index.html')
        self.response.out.write(template.render())

class About(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('info.html')
        self.response.out.write(template.render())

class GetInvolved(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('kyr.html')
        self.response.out.write(template.render())

class Biographies(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('volunteer.html')
        self.response.out.write(template.render())

class Donate(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('htc.html')
        self.response.out.write(template.render())

class Vision(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('vision.html')
        self.response.out.write(template.render())

app = webapp2.WSGIApplication([
  ('/register', RegisterHandler),
  ('/', Home),
  ('/vision', Vision),
  ('/getinvolved', GetInvolved),
  ('/biographies', Biographies),
  ('/donate1', RegisterHandler),
  ('/donate', Donate),
  ('/about', About),
], debug=True)
#info about us
#vision Vision

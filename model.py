from google.appengine.ext import ndb

class NewUser(ndb.Model):
   type = ndb.StringProperty(required=True, default='NewUser')
   Name = ndb.StringProperty(required=True)
   Email = ndb.StringProperty(required=True)
   Phone = ndb.StringProperty(required=True)
   Item_discription = ndb.StringProperty(required=True)

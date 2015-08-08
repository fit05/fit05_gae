from google.appengine.ext import ndb

# Create your models here.
class Facility(db.Model):
	fid = ndb.IntegerProperty()
	name = ndb.StringProperty()
	description=ndb.StringProperty(multiline=True)
	geo=ddb.GeoPtProperty()
	date=ndb.DateTimeProperty(auto_now_add=True)

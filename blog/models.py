from datetime import datetime
from blog import db
from flask_login import UserMixin



class Users(UserMixin,db.Model):
    name = db.Column(db.VARCHAR(60), primary_key=True)
    message = db.Column(db.TEXT)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.name


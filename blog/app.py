from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from blog import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash



#Create flask Instance
app = Flask(__name__)


#Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

#secret key
import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


db = SQLAlchemy(app)



#model
class Users(db.Model):
    name = db.Column(db.VARCHAR(60), primary_key=True)
    message = db.Column(db.TEXT)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.name



#Form class
class UserForm(FlaskForm):
    name = StringField ('Name', validators=[DataRequired()], render_kw={"placeholder":"Your Name...."})
    message = TextAreaField ('Message', render_kw={"rows": 5, "cols": 50, "placeholder":"Your Message...."}, validators=[DataRequired()])
    submit = SubmitField ('Submit')


@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/about')
def abt():
    return render_template('about.html')

@app.route('/edu')
def edu():
    return render_template('edu.html')

@app.route('/exp')
def exp():
    return render_template('exp.html')

@app.route('/wrk')
def wrk():
    return render_template('wrk.html')



@app.route('/contact', methods=['GET', 'POST'])
def cont():
    name = None
    form = UserForm()
    #validating form
    if form.validate_on_submit():
        user=Users(name = form.name.data, message = form.message.data)
        db.session.add(user)
        db.session.commit()
        name= form.name.data
        form.name.data=''
        form.message.data=''
        flash('Message submitted successfully!')
    our_users=Users.query.order_by(Users.date_added)
    return render_template('contact.html', form = form, our_users=our_users, name=name)

@app.route('/dashboard', methods=['GET', 'POST'])
def dash():
    # form = UserForm()
    # name = form.name.data
    # message= form.message.data
    # #validating form
    # if form.validate_on_submit():
    #     user = User.query.filter_by(username=form.username.data).first()
    #     user=Users(name = form.name.data, message = form.message.data)
    #     db.session.add(user)
    #     db.session.commit()
    #     name= form.name.data
    #     form.name.data=''
    #     form.message.data=''
    #     flash('Message submitted successfully!')
    our_users=Users.query.order_by(Users.date_added)
    return render_template('dashboard.html', our_users=our_users)
    

class User(UserMixin,db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(15), unique=True, nullable=False)
  hashed_password=db.Column(db.String(128))
  # post = db.relationship('Post', backref='users', lazy=True)

  def __repr__(self):
    return f"User('{self.username}', '{self.email}')"

#adated from Grinberg(2014, 2018)
  @property
  def password(self):
    raise AttributeError('Password is not readable.')

  @password.setter
  def password(self,password):
    self.hashed_password=generate_password_hash(password)

  def verify_password(self,password):
    return check_password_hash(self.hashed_password,password)


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


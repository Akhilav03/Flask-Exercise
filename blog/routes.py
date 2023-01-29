from flask import render_template, flash
from blog import app, db
from blog.models import Users
from blog.forms import  UserForm




@app.route("/")
def home():
  return render_template('index.html')

@app.route("/about")
def about():
  return render_template('about.html', title='About')


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
    return render_template('dashboard.html', form = form, our_users=our_users, name=name)


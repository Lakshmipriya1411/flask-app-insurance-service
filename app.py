import boto3
from flask import Flask, render_template,request
from flask import url_for
from flask_bootstrap import Bootstrap
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
from aws_xray_sdk.core import xray_recorder, patch_all
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
# from flask_mysqldb import MySQL
# import MySQLdb.cursors
import re
app = Flask(__name__)

xray_recorder.configure(
    sampling=False,
    context_missing='LOG_ERROR',
    plugins=('EC2Plugin'),   
    service='BitCoin Flask Web App'
)
XRayMiddleware(app, xray_recorder)
patch_all()
bootstrap = Bootstrap(app)
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'root'
# app.config['MYSQL_DB'] = 'bitcoin'
  
# mysql = MySQL(app)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/faq')
def faq():
    return render_template('faq.html')
@app.route('/blog')    
def blog():
    return render_template('blog.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/pricing')
def pricing():
    return render_template('pricing.html')
    
@app.route('/login',methods=['GET', 'POST'])
def login():
    # return render_template('login.html')
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # cursor.execute('SELECT * FROM user WHERE username = % s AND password = % s', (username, password, ))
        # account = cursor.fetchone()
        if True:
            # session['loggedin'] = True
            # session['id'] = account['id']
            # session['username'] = account['username']
            msg = 'Logged in successfully !'
            return render_template('index.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)
@app.route('/signup',methods=['GET', 'POST'])

def signup():
    msg = ''
   
    if request.method == 'POST' and 'firstname' in request.form and 'lastname' in request.form and 'username' in request.form and 'password' in request.form and 'email' in request.form :        
        username = request.form['username']
        password = request.form['password']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        # cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        # cursor.execute('SELECT * FROM user WHERE username = % s', (username, ))
        # account = cursor.fetchone()
        # if account:
            # msg = 'Account already exists !'
        # elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            # msg = 'Invalid email address !'
        # elif not re.match(r'[A-Za-z0-9]+', username):
            # msg = 'Username must contain only characters and numbers !'
        # elif not username or not password or not email:
            # msg = 'Please fill out the form !'
        # else:
            # cursor.execute('INSERT INTO user VALUES (NULL,%s,%s, % s, % s, % s)', (firstname,lastname,username, password, email, ))
            # mysql.connection.commit()
        msg = 'You have successfully registered !'
    # elif request.method == 'POST':
        # msg = 'Please fill out the form !'
    return render_template('signup.html', msg = msg)                  
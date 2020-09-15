from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_mail import Mail
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = '0943eb52672340e1162dc8cce842f6'
app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///site.db'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)
login_manager.login_view="login"
login_manager.login_message_category='info'
app.config["MAIL_SERVER"]='smtp.gmail.com'
app.config["MAIL_PORT"]=465
app.config["MAIL_USE_SSL"]=False
app.config["MAIL_USE_TLS "]=False

app.config["MAIL_USERNAME"]=os.environ.get('EMAIL_USER')
app.config["MAIL_PASSWORD"]=os.environ.get('EMAIL_PASS')
mail=Mail(app)



from feedsblog.users.routes import users
from feedsblog.posts.routes import posts
from feedsblog.main.routes import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)




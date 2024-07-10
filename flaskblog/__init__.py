import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config["SECRET_KEY"] = "64af23abdef232726fdbbf2ea2575c88"
# The three bars on the uri signals a relative path, the db must be on the same directory.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# login is the fn name of the fn managing the login on routes.py
login_manager.login_view = "login"
# It uses the info class for bootstrap
login_manager.login_message_category = "info"
app.config["MAIL_SERVER"] = "smtp.googlemail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
# Remember to export this variables
# export EMAIL_USER="your_email@example.com"
# export EMAIL_PASSWORD="your_password"
app.config["MAIL_USERNAME"] = os.environ.get("EMAIL_USER")
app.config["MAIL_PASSWORD"] = os.environ.get("EMAIL_PASSWORD")
mail = Mail(app)

from flaskblog import routes


"""
NOTE:
We must run on the terminal to create the db
from project import app, db
app.app_context().push()
db.create_all()

Then the .db file is created in a folder called "Instance" in your project. 

"""

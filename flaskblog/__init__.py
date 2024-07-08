from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "64af23abdef232726fdbbf2ea2575c88"
# The three bars on the uri signals a relative path, the db must be on the same directory.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)

from flaskblog import routes


"""
NOTE:
We must run on the terminal to create the db
from project import app, db
app.app_context().push()
db.create_all()

Then the .db file is created in a folder called "Instance" in your project. 

"""

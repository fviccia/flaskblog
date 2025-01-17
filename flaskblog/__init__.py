from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
mail = Mail()
# login is the fn name of the fn managing the login on routes.py
# Using blueprints, is the defined fn in the users blueprint
login_manager.login_view = "users.login"
# It uses the info class for bootstrap
login_manager.login_message_category = "info"


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # from flaskblog import routes
    # Must register the blueprint objects instead of the default routes as above
    from flaskblog.users.routes import users

    app.register_blueprint(users)
    from flaskblog.posts.routes import posts

    app.register_blueprint(posts)
    from flaskblog.main.routes import main

    app.register_blueprint(main)

    from flaskblog.errors.handlers import errors

    app.register_blueprint(errors)

    return app


"""
NOTE:
We must run on the terminal to create the db
from project import app, db
app.app_context().push()
db.create_all()

Then the .db file is created in a folder called "Instance" in your project. 

"""

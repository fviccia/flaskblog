from datetime import datetime, timezone
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flaskblog import db, login_manager
from flask_login import UserMixin
from flask import current_app


# Decorated function needed for login_manager to know the current user
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    # Inherit from UserMixin to have avalaible the attributes that login_manager expects
    id = db.Column(db.Integer, primary_key=True)
    # Nullable is in False to enforce the existence of the field.
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    """
    Setting a relationship to the Post class, 
    Backref:
    In the Post model, this creates an attribute named author which refers back to the User instance that authored the post. 
    Essentially, this allows you to access the user who authored a particular post through post.author.
    """
    posts = db.relationship("Post", backref="author", lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config["SECRET_KEY"], expires_sec)
        return s.dumps({"user.id": self.id}).decode("utf-8")

    # Define the method as static to not expect the self param
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            user_id = s.loads(token)["user_id"]
        except:
            return None
        # If its valid, return the user.
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}','{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(
        db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc)
    )
    content = db.Column(db.Text, nullable=False)
    # Links to the User Model, is in lower case because we are referring to the table and field name not the class
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"

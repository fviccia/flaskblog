import os


class Config:

    # Some variables are setted in bashrc
    # export SECRET_KEY=""
    # export SQLALCHEMY_DATABASE_URI=""
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")

    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True

    # Remember to export this variables
    # export EMAIL_USER="your_email@example.com"
    # export EMAIL_PASSWORD="your_password"
    MAIL_USERNAME = os.environ.get("EMAIL_USER")
    MAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

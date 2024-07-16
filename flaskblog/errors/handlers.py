from flask import Blueprint, render_template


errors = Blueprint("errors", __name__)


# There is a method called just errorhandler without the app, must use the app one to make the handlers avalaible for all the application.
@errors.app_errorhandler(404)
def error_404(error):
    # The second value is the status in flask
    return render_template("errors/404.html"), 404


@errors.app_errorhandler(403)
def error_403(error):
    # The second value is the status in flask
    return render_template("errors/403.html"), 403


@errors.app_errorhandler(500)
def error_500(error):
    # The second value is the status in flask
    return render_template("errors/500.html"), 500

from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post


posts = [
    {
        "author": "Franco Viccia",
        "title": "First Post",
        "content": "First Post Content",
        "date_posted": "April 20, 2018",
    },
    {
        "author": "John Doe",
        "title": "Second Post",
        "content": "Second Post Content",
        "date_posted": "April 22, 2018",
    },
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/register", methods=["GET", "POST"])
def register():
    # This is the form object that i created on forms.py
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    # With this i render a template but making those args avalaible inside.
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccesfull! Please check username and password", "danger")
    return render_template("login.html", title="Login", form=form)

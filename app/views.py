from . import app
from .database import test_create, test_select, test_select_all, add_user, username_select, password_select
from flask import render_template, flash, request, url_for, redirect, session
from passlib.hash import sha256_crypt
@app.route('/')
def index():
    #test_create()

    return render_template('login.html')

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == "POST":
        name = request.form.get("username")
        password = request.form.get("password")
        namedata = username_select(name)
        passworddata = password_select(password)
        if namedata is None:
            flash("No name", "danger")
            return render_template("login.html")
            #return "Name is null"
        else:
            if password == passworddata[0]:
                session["log"] = True
                session["username"] = name
                flash("You are now login", "success")
                return redirect(url_for('index'))
                #return "Login is done"
            else:
                flash("incorrect password", "danger")
                return render_template("login.html")
                    #return "Password is wrong"

    return render_template('login.html')

@app.route('/reg', methods = ['POST', 'GET'])
def reg():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirm")

        if password == confirm:
            add_user(username, password)
            return redirect(url_for('login'))
        else:
            flash("password does not match", "danger")
            return render_template('reg.html.')

    return render_template('reg.html')

@app.route("/logout")
def logout():
    session.clear()
    flash("You are logout", "success")
    return redirect(url_for("login"))
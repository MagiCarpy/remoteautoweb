from DCW import app, db, bcrypt
from flask import render_template, url_for, request, redirect, flash
from flask_login import login_user, current_user, logout_user, login_required
from DCW.forms import LoginForm, RegisterForm
from DCW.models import User, Devices

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="home")

@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegisterForm()
    if form.validate_on_submit() and request.method == 'POST':
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Registration Successful', 'success')
        return redirect(url_for('login'))

    return render_template("register.html", title="register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit() and request.method == 'POST':
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            flash('Login Successful', 'success')
            if 'next' in request.args:
                return redirect(request.args.get('next'))
            else:
                return redirect(url_for('home'))
        else:
            flash(f'Invalid Login: check username or password', 'danger')
    return render_template("login.html", title="login", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/devices", methods=['GET', 'POST'])
@login_required
def devices():
    devices = Devices.query.all()
    if request.method == 'POST':
        # make cleaner when more devices
        data = request.form
        if data.get('light'):
            devices[0].status = 1
        else:
            devices[0].status = 0
        db.session.commit()
    print(devices[0].status)
    return render_template("devices.html", title="devices", devices=devices)
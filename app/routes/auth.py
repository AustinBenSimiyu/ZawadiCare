from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user
from app.forms import RegistrationForm, LoginForm
from app.models.user import User
from app import db

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = RegistrationForm()
    login_form = LoginForm() 
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            due_date=form.due_date.data
        )
        user.set_password(form.password.data)
        
        # Make the first user an admin
        if User.query.count() == 0:
            user.is_admin = True
        
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now registered!')
        return redirect(url_for('auth.login'))
    return render_template('base2.html', title='Register', register_form=form, login_form=login_form)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    form = LoginForm()
    register_form = RegistrationForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password')
            return redirect(url_for('auth.login'))
        login_user(user)
        return redirect(url_for('main.dashboard'))
    return render_template('base2.html', title='Sign In', login_form=form, register_form=register_form)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.home'))
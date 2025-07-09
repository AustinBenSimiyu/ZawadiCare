from flask import Blueprint, render_template, flash, redirect, url_for, abort, request
from flask_login import login_required, current_user
from app.models.user import User
from app import db
from werkzeug.security import generate_password_hash
from functools import wraps
from datetime import datetime

bp = Blueprint('admin', __name__, url_prefix='/admin')

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

@bp.route('/')
@login_required
@admin_required
def admin_dashboard():
    users = User.query.all()
    return render_template('admin/dashboard.html', users=users)

@bp.route('/user/<int:id>/reset_password', methods=['GET', 'POST'])
@login_required
@admin_required
def reset_password(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        new_password = request.form.get('new_password')
        if new_password:
            user.password_hash = generate_password_hash(new_password)
            db.session.commit()
            flash(f'Password updated for {user.username}')
        return redirect(url_for('admin.admin_dashboard'))
    return render_template('admin/reset_password.html', user=user)

@bp.route('/user/<int:id>/update_due_date', methods=['GET', 'POST'])
@login_required
@admin_required
def update_due_date(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        new_due_date = request.form.get('due_date')
        try:
            user.due_date = datetime.strptime(new_due_date, '%Y-%m-%d').date()
            db.session.commit()
            flash(f'Due date updated for {user.username}')
        except ValueError:
            flash('Invalid date format. Please use YYYY-MM-DD format.')
        return redirect(url_for('admin.admin_dashboard'))
    return render_template('admin/update_due_date.html', user=user)

@bp.route('/user/<int:id>/delete', methods=['POST'])
@login_required
@admin_required
def delete_user(id):
    user = User.query.get_or_404(id)
    if user == current_user:
        flash('Cannot delete your own account')
        return redirect(url_for('admin.admin_dashboard'))
    db.session.delete(user)
    db.session.commit()
    flash(f'User {user.username} has been deleted')
    return redirect(url_for('admin.admin_dashboard'))

@bp.route('/user/<int:id>/toggle_admin')
@login_required
@admin_required
def toggle_admin(id):
    user = User.query.get_or_404(id)
    if user == current_user:
        flash('Cannot modify your own admin status')
        return redirect(url_for('admin.admin_dashboard'))
    user.is_admin = not user.is_admin
    db.session.commit()
    flash(f'Admin status toggled for {user.username}')
    return redirect(url_for('admin.admin_dashboard')) 
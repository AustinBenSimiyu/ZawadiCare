from flask import Blueprint, render_template
from flask_login import login_required, current_user
from datetime import datetime
from app.models.tracking import Weight, Movement, Appointment, Photo

bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/home')
def home():
    return render_template('index.html')

@bp.route('/base')
def base():
    return render_template('base.html')

@bp.route('/dashboard')
@login_required
def dashboard():
    current_date = datetime.now().date()
    if current_user.due_date:
        weeks = ((current_user.due_date - current_date).days // 7)
    else:
        weeks = 0

    # Get recent data
    recent_weights = Weight.query.filter_by(user_id=current_user.id).order_by(Weight.date.desc()).limit(5).all()
    recent_movements = Movement.query.filter_by(user_id=current_user.id).order_by(Movement.date.desc()).limit(3).all()
    upcoming_appointments = Appointment.query.filter_by(user_id=current_user.id)\
        .filter(Appointment.date >= datetime.now())\
        .order_by(Appointment.date.asc()).limit(3).all()
    recent_photos = Photo.query.filter_by(user_id=current_user.id).order_by(Photo.date.desc()).limit(4).all()
    
    return render_template('dashboard.html',
                         current_date=current_date,
                         weeks=weeks,
                         recent_weights=recent_weights,
                         recent_movements=recent_movements,
                         upcoming_appointments=upcoming_appointments,
                         recent_photos=recent_photos)
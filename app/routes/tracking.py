from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_required, current_user
from app import db
from app.forms import WeightForm, MovementForm, AppointmentForm, PhotoForm, SymptomForm
from app.models.tracking import Weight, Movement, Appointment, Photo, Symptom
from datetime import datetime
import os
from werkzeug.utils import secure_filename


bp = Blueprint('tracking', __name__)

# Add this function at the top of the file
def ensure_upload_directory_exists():
    upload_dir = os.path.join('app', 'static', 'uploads')
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

# Weight tracking routes
@bp.route('/weight/record', methods=['GET', 'POST'])
@login_required
def record_weight():
    form = WeightForm()
    if form.validate_on_submit():
        weight = Weight(
            user_id=current_user.id,
            date=form.date.data,
            weight=form.weight.data,
            notes=form.notes.data
        )
        db.session.add(weight)
        db.session.commit()
        flash('Weight recorded successfully!')
        return redirect(url_for('main.dashboard'))
    return render_template('tracking/weight.html', form=form)

# Movement tracking routes
@bp.route('/movement/track', methods=['GET', 'POST'])
@login_required
def track_movement():
    form = MovementForm()
    if form.validate_on_submit():
        try:
            movement = Movement(
                user_id=current_user.id,
                date=form.date.data,
                duration=form.duration.data,
                kick_count=form.kick_count.data,
                notes=form.notes.data
            )
            db.session.add(movement)
            db.session.commit()
            flash('Movement tracked successfully!')
            return redirect(url_for('main.dashboard'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error tracking movement: {str(e)}', 'error')
            print(f"Error: {str(e)}")  # For debugging
    
    # If there are form errors, display them
    if form.errors:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'{field}: {error}', 'error')

    return render_template('tracking/movement.html', form=form)

# Appointment routes
@bp.route('/appointment/add', methods=['GET', 'POST'])
@login_required
def add_appointment():
    form = AppointmentForm()
    if form.validate_on_submit():
        try:
            appointment = Appointment(
                user_id=current_user.id,
                date=form.date.data,
                title=form.title.data,
                doctor=form.doctor.data,
                location=form.location.data,
                notes=form.notes.data
            )
            db.session.add(appointment)
            db.session.commit()
            flash('Appointment added successfully!')
            return redirect(url_for('main.dashboard'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error adding appointment: {str(e)}', 'error')
            
    # If there are form errors, display them
    if form.errors:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'{field}: {error}', 'error')
                
    return render_template('tracking/appointment.html', form=form)

# Photo routes
@bp.route('/photo/add', methods=['GET', 'POST'])
@login_required
def add_photo():
    form = PhotoForm()
    if form.validate_on_submit():
        ensure_upload_directory_exists()  # Add this line
        try:
            file = form.photo.data
            filename = f"{current_user.id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}{os.path.splitext(file.filename)[1]}"
            file_path = os.path.join('app', 'static', 'uploads', filename)
            file.save(file_path)
            
            photo = Photo(
                user_id=current_user.id,
                date=form.date.data,
                image_path=filename,  # Store just the filename
                caption=form.caption.data
            )
            db.session.add(photo)
            db.session.commit()
            flash('Photo uploaded successfully!')
            return redirect(url_for('main.dashboard'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error uploading photo: {str(e)}', 'error')
    return render_template('tracking/photo.html', form=form)

# Symptom routes
@bp.route('/symptoms/log', methods=['GET', 'POST'])
@login_required
def log_symptoms():
    form = SymptomForm()
    if form.validate_on_submit():
        # Convert headache string to boolean
        headache_value = True if form.headache.data == 'True' else False
        
        symptom = Symptom(
            user_id=current_user.id,
            date=form.date.data,
            nausea=form.nausea.data,
            fatigue=form.fatigue.data,
            mood=form.mood.data,
            headache=headache_value,  # Use the converted boolean value
            notes=form.notes.data
        )
        try:
            db.session.add(symptom)
            db.session.commit()
            flash('Symptoms logged successfully!')
            return redirect(url_for('main.dashboard'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error logging symptoms: {str(e)}', 'error')
    
    return render_template('tracking/symptoms.html', form=form)

# Appointments deletion
@bp.route('/appointment/delete/<int:id>', methods=['POST'])
@login_required
def delete_appointment(id):
    appointment = Appointment.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    try:
        db.session.delete(appointment)
        db.session.commit()
        flash('Appointment deleted successfully!')
    except Exception as e:
        db.session.rollback()
        flash('Error deleting appointment.', 'error')
    return redirect(url_for('main.dashboard'))
import os
from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user
from datetime import datetime
from app.models.tracking import Weight, Movement, Appointment, Photo

bp = Blueprint('main', __name__)
auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('auth/login.html')

@auth.route('/register')
def register():
    return render_template('auth/register.html')

@bp.route('/')
@bp.route('/home')
def home():
    return render_template('index.html')

@bp.route('/base')
def base():
    return render_template('base.html')

@bp.route("/api/config")
def get_api_key():
    return jsonify(api_key=os.getenv("PUBLIC_API_KEY"))

@bp.route('/dashboard')
@login_required
def dashboard():
    current_date = datetime.now().date()

    if current_user.due_date:
        weeks = ((current_user.due_date - current_date).days // 7)
    else:
        weeks = 0

    current_week = 40 - ((current_user.due_date - current_date).days // 7)

    if 0 <= current_week < 40:  # 40 items in the list
        baby_size = get_baby_size_list(current_week)
    else:
        baby_size = "your baby!"

    # Data for dashboard
    recent_weights = Weight.query.filter_by(user_id=current_user.id).order_by(Weight.date.desc()).limit(5).all()
    recent_movements = Movement.query.filter_by(user_id=current_user.id).order_by(Movement.date.desc()).limit(3).all()
    upcoming_appointments = Appointment.query.filter_by(user_id=current_user.id)\
        .filter(Appointment.date >= datetime.now())\
        .order_by(Appointment.date.asc()).limit(3).all()
    recent_photos = Photo.query.filter_by(user_id=current_user.id).order_by(Photo.date.desc()).limit(4).all()

    return render_template('dashboard.html',
                           current_date=current_date,
                           weeks=weeks,
                           baby_size=baby_size,
                           recent_weights=recent_weights,
                           recent_movements=recent_movements,
                           upcoming_appointments=upcoming_appointments,
                           recent_photos=recent_photos)

def get_baby_size_list(x):
    baby_size = [
        "Poppy seed 🌱",            # Week 1
        "Sesame seed ⚪",           # Week 2
        "Lentil 🫘",                # Week 3
        "Blueberry 🫐",            # Week 4
        "Raspberry 🍓",            # Week 5
        "Green olive 🫒",          # Week 6
        "Prune 🍑",                # Week 7
        "Lime 🍈",                 # Week 8
        "Plum 🍑",                 # Week 9
        "Peach 🍑",                # Week 10
        "Lemon 🍋",                # Week 11
        "Apple 🍎",                # Week 12
        "Avocado 🥑",              # Week 13
        "Onion 🧅",                # Week 14
        "Sweet potato 🍠",         # Week 15
        "Mango 🥭",                # Week 16
        "Banana 🍌",               # Week 17
        "Carrot 🥕",               # Week 18
        "Spaghetti squash 🎃",     # Week 19
        "Coconut 🥥",              # Week 20
        "Corn on the cob 🌽",      # Week 21
        "Cauliflower 🥦",          # Week 22
        "Red cabbage 🥬",          # Week 23
        "Cucumber 🥒",             # Week 24
        "Eggplant 🍆",             # Week 25
        "Butternut squash 🍠",     # Week 26
        "Zucchini 🥒",             # Week 27
        "Pineapple 🍍",            # Week 28
        "Cantaloupe 🍈",           # Week 29
        "Teddy bear 🧸",           # Week 30
        "Basketball 🏀",           # Week 31
        "Honeydew melon 🍈",       # Week 32
        "Small watermelon 🍉",     # Week 33
        "Birthday cake 🎂",        # Week 34
        "Stuffed bunny 🐰",        # Week 35
        "Newborn kitten 🐱",       # Week 36
        "Full-size watermelon 🍉", # Week 37
        "Beach ball 🏖️",          # Week 38
        "Overnight bag 🎒",        # Week 39
        "A miracle ✨👶"           # Week 40
    ]
    return baby_size[x] if 0 <= x < len(baby_size) else "your baby!"

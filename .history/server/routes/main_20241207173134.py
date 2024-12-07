from flask import Blueprint, render_template, request, redirect, url_for, flash

main_bp = Blueprint('main', __name__)

USER = {'username': 'admin', 'password': 'password'}

@main_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == USER['username'] and password == USER['password']:
            flash('Login successful!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid username or password.', 'danger')
    return render_template('login.html')

@main_bp.route('/index')
def index():
    return render_template('index.html')

@main_bp.route('/eventmap')
def eventmap():
    return render_template('eventmap.html')

@main_bp.route('/events')
def events():
    return render_template('events.html')

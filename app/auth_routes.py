from flask import Blueprint, render_template, request, redirect, session, flash, url_for
from app.decorators import login_required
auth_routes = Blueprint('auth_routes', __name__)

# Hardcoded user data for demonstration purposes
users = {
    "admin": "123456",
    "user": "123456"
}



@auth_routes.route('/public')
def public():
    return "This is a public page."

@auth_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            
            return redirect(url_for('auth_routes.dashboard'))
        else:
            flash('Login Failed')
    return render_template('auth/login.html', title='Login Page')

@auth_routes.route('/dashboard')
@login_required
def dashboard():
    return render_template('auth/dashboard.html', username=session['username'])

@auth_routes.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/login')

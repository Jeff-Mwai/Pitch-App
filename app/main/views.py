from flask import Flask, render_template, url_for, flash, redirect
from . import main
from .forms import RegistrationForm, LoginForm





@main.route('/')
def home():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html', title = 'About')

@main.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for { form.username.data }!','success')
        return redirect(url_for('.home'))
    return render_template('register.html', title = 'register', form = form)

@main.route('/login' , methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'jeffreymwai4@gmail.com' and form.password.data == '1234':
            flash('You have been logged in successfully!', 'success')
            return redirect(url_for('.home'))
        else:
            flash('login unsuccessful. Please check your password or email', 'danger')

    return render_template('login.html', title = 'login', form = form)



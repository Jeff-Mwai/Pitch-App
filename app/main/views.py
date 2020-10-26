from flask import Flask, render_template, url_for, flash, redirect, abort
from . import main
from .forms import RegistrationForm, LoginForm, UpdateProfile, PitchForm
from ..models import User,Pitch
from .. import db, photos
from flask_login import login_user,login_required, logout_user, current_user






@main.route('/')
def home():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html', title = 'About')

@main.route('/signout')
@login_required
def signout():
    logout_user()
    return redirect(url_for("main.home"))

@main.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data,email = form.email.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for { form.username.data }!','success')
        return redirect(url_for('.home'))
    return render_template('register.html', title = 'register', form = form)


@main.route('/new_pitch', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        pitch_content = form.post.data
        category = form.category.data
        user_id = current_user
        new_pitch_item = Pitch(pitch_content=pitch_content,user_id=current_user._get_current_object().id,category=category,title=title)
        new_pitch_item.save_pitch()
        return redirect(url_for('main.home'))
        
    return render_template('pitch.html', form = form)

@main.route('/login' , methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            flash('You have been logged in successfully!', 'success')
            return redirect(url_for('.home'))
    else:
        flash('login unsuccessful. Please check your password or email', 'danger')

    return render_template('login.html', title = 'login', form = form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
    






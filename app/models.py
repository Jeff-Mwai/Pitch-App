from werkzeug.security import generate_password_hash,check_password_hash
from . import db
from flask_login import UserMixin
from . import login_manager
# from datetime import datetime




class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    comment = db.relationship('Comment',backref='user',lazy='dynamic')
    like = db.relationship('Likes',backref='user',lazy='dynamic')
    dislike = db.relationship('Dislikes',backref='user',lazy='dynamic')





    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def __repr__(self):
        return f'User {self.username}'


class Pitch(db.Model):

    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    pitch_content = db.Column(db.String)
    category = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comment = db.relationship('Comment',backref='pitch',lazy='dynamic')
    like = db.relationship('Likes',backref='pitch',lazy='dynamic')
    dislike = db.relationship('Dislikes',backref='pitch',lazy='dynamic')
    
    


    def append_pitch(self):
        ''' Save the pitches '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def delete_pitches(cls):
        Pitch.all_pitches.clear()


    def get_pitches(category):

        pitches = Pitch.query.filter_by(category=category).all()

      
        return pitches

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text(),nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable = False)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'),nullable = False)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,pitch_id):
        comments = Comment.query.filter_by(pitch_id=pitch_id).all()

        return comments

    
    def __repr__(self):
        return f'comment:{self.comment}'

class Likes(db.Model):
    __tablename__ = 'likes'

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_likes(cls,id):
        like = Likes.query.filter_by(pitch_id=id).all()
        return like


    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'
class Dislikes(db.Model):
    __tablename__ = 'dislikes'

    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    

    def save(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_dislikes(cls,id):
        dislike = Dislikes.query.filter_by(pitch_id=id).all()
        return dislike

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
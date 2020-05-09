from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    # posted = db.Column(db.DateTime,default=datetime.utcnow)
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))















# class Blog:

#     all_blogs = []


#     def save_blogs(self):
#         Blog.all_blogs.append(self)


#     @classmethod
#     def clear_blogs(cls):
#         Blog.all_blogs.clear()
    
#     @classmethod
#     def get_blogs(cls,id):

#         response = []

#         for blog in cls.all_blogs:
#             if blog.id == id:
#                 response.append(blog)

#         return response


from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))

    def __repr__(self):
        return f'User {self.username}'

class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'
















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


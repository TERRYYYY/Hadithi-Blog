from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_quote
from .forms import BlogForm
from ..models import Blog
from flask_login import login_required
from flask import render_template,request,redirect,url_for,abort
from ..models import Blog, User


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'HadithiBlog'

    return render_template('index.html', title = title)

@main.route('/blog', methods = ['GET','POST'])
@login_required
def new_blog():
    form = BlogForm()
    blogs = Blog.query.all()


    if request.method == "POST":
        req = request.form
        print(req)

        blog = req.get('blog')
        new_blog = Pitch(description = blog , user = current_user)
        db.session.add(new_blog)
        db.session.commit()
        blog = Blog.query.all()

        
    return render_template("new_blog.html" ,blogs = blogs , form= form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

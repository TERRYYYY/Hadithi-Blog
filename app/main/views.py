from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_quote
from flask_login import login_required
from flask import render_template,request,redirect,url_for,abort
from ..models import Blog, User
from .forms import BlogForm,UpdateProfile
from .. import db
# from .. import db,photos


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
        new_blog = Blog(title=blog)
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

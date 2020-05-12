from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_quote
from flask_login import login_required
from flask import render_template,request,redirect,url_for,abort,flash
from ..models import Blog, User
from .forms import BlogForm,UpdateProfile
from .. import db
import markdown2  
# from .. import db,photos

@main.route('/')
def home():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('home.html')

@main.route('/blog/<int:blog_id>')
def blog(blog_id):
    blog = Blog.query.get(blog_id)

    return render_template('blog.html',title=blog.title , blog=blog)


@main.route('/blog')
def index():
    
    title = 'HadithiBlog'
    blogs = Blog.query.all()

    return render_template('index.html', title = title, blogs=blogs)

@main.route('/blog/new', methods = ['GET','POST'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        blog = Blog(title=form.title.data , subtitle=form.subtitle.data ,content=form.content.data )
        db.session.add(blog)
        db.session.commit()
        flash('Your post has been created !' , 'success')
        return redirect(url_for('.index'))

    return render_template('new_blog.html',title='New Post',form=form)

@main.route('/blog/<int:blog_id>/delete' ,methods = ['POST'])
@login_required
def delete_blog(blog_id):
    blog = Blog.query.get(blog_id)
    db.session.delete(blog)
    db.session.commit()
    flash('Your post has been deleted !' , 'danger')
    return redirect(url_for('.index'))
@main.route('/blog/<int:blog_id>/update' ,methods = ['GET','POST'])
@login_required
def update_blog(blog_id):
    blog = Blog.query.get(blog_id)
    form = BlogForm()
    if form.validate_on_submit():
        blog.title = form.title.data
        blog.subtitle = form.subtitle.data
        blog.content = form.content.data
        db.session.commit()
        flash('Your post has been updated !', 'primary')
        return redirect(url_for('.blog',blog_id=blog.id))
    return render_template('new_blog.html',title='Update Post',form=form)




# @main.route('/blog', methods = ['GET','POST'])
# @login_required
# def new_blog():
#     form = BlogForm()
#     if form.validate_on_submit():
#         title = form.title.data
#         subtitle = form.subtitle.data
#         content = form.content.data

#         # Updated review instance
#         new_blog = Blog(title=title,subtitle=subtitle, content=content,user=current_user)

#         # save review method
#         new_blog.save_blog()
#         # return redirect(url_for('.movie',id = movie.id ))

#     return render_template('new_blog.html',form=form)

# @main.route('/blog', methods = ['GET','POST'])
# @login_required
# def new_blog():
#     form = BlogForm()
#     blogs = Blog.query.all()


#     if request.method == "POST":
#         req = request.form
#         print(req)

#         blog = req.get('blog')
#         new_blog = Blog(title=blog)
#         db.session.add(new_blog)
#         db.session.commit()
#         blog = Blog.query.all()

        
#     return render_template("new_blog.html" ,blogs = blogs , form= form)

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

# @main.route('/blog/<int:id>')
# def single_blog(id):
#     blog=Blog.query.get(id)
#     if blog is None:
#         abort(404)
#     format_blog = markdown2.markdown(blog.title,extras=["code-friendly", "fenced-code-blocks"])
#     return render_template('blog.html',blog = blog,format_blog=format_blog)



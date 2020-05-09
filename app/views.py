# from flask import render_template
# from .request import get_quote
# from .models import Blog
# from .forms import BlogForm
# # Blog = blog.Blog

# # Views
# @app.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''
#     popular_quote = get_quote()
#     title = "HadithiBlog"
#     return render_template('index.html', title=title ,popular_quote=popular_quote)

# @app.route('/blog/<int:id>')
# def blog(id):

#     '''
#     View blog page function that returns the blog details page and its data
#     '''
#     blogs = Blog.get_blogs(id)

#     return render_template('blog.html', blog=blog)

# @app.route('/blog/new/<int:id>', methods = ['GET','POST'])
# def new_blog(id):
#     form = BlogForm()

#     if form.validate_on_submit():
#         title = form.title.data
#         subtitle = form.subtitle.data
#         content = form.content.data
#         new_blog = Blog(id,title,subtitle,content)
#         new_blog.save_blog()
#         return redirect(url_for('blog',id = id ))

#     return render_template('new_blog.html',form=form)
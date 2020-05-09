from flask import render_template
from app import app
from .request import get_quote

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    popular_quote = get_quote()
    title = "HadithiBlog"
    return render_template('index.html', title=title ,popular_quote=popular_quote)

@app.route('/blog/<int:id>')
def blog(id):

    '''
    View blog page function that returns the blog details page and its data
    '''
    blog = get_quote(id)

    return render_template('blog.html',blog = blog)
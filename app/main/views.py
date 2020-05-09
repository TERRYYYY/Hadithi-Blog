from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_quote
from .forms import BlogForm
from ..models import Blog
from flask_login import login_required

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
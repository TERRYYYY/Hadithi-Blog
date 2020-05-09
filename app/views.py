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
    title = "Hadithi-Blog"
    return render_template('index.html', title=title ,popular_quote=popular_quote)
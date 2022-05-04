"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime

@route('/')
@route('/home')
@view('index')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/life')
@view('life')
def contact():
    """Renders the contact page."""
    return dict(
        title='Жизнь',
        message='Статьи о жизни',
        year=datetime.now().year
    )

@route('/culture')
@view('culture')
def about():
    """Renders the about page."""
    return dict(
        title='Культура',
        message='Статьи о культуре',
        year=datetime.now().year
    )

@route('/sport')
@view('sport')
def contact():
    """Renders the contact page."""
    return dict(
        title='Спорт',
        message='Спортивные новости',
        year=datetime.now().year
    )


@route('/partner')
@view('partner')
def contact():
    """Renders the contact page."""
    return dict(
        title='Партнёры',
        message='Партнёры СМИ',
        year=datetime.now().year
    )
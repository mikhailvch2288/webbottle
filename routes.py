"""
Routes and views for the bottle application.
"""



from bottle import route, view,post, post, request, redirect


from datetime import datetime
import json
import re
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



@route('/revi')
@view('revi')
def contact():
    """Renders the contact page."""
    return dict(
        title='Отзывы',
        message='Оставьте ваш отзыв',
        year=datetime.now().year
    )



@route('/orders')
@view('orders')
def orders():
    """Renders the about page."""
    return dict(
        title='Ваши заказы',
        message='Выполните заказ',
        year=datetime.now().year
    )

shame = re.compile(r"[0-9]")
salaga = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})")
products = {}
@post('/orders', method='post')
def my_form():

    product= request.params.QUEST
    address= request.params.ADDRESS
    mail=request.params.MAIL
    pay=request.params.PAYMENT


    if product == '' or address == '' or mail == '' or pay == '':
            return "Заполните все поля."

    if salaga.match(mail) is None:
             return "Неверный мэил адрес" 
         
    if shame.match(pay) is None:
             return "Неверный номер карты"  
    
    products[mail] = product
    #pdb.set_trace()
    with open ('orders.txt', 'w') as txtquest:
        json.dump(products, txtquest,ensure_ascii=False)    
    return "Спасибо! Ваш заказ внесен в базу. %s" % mail
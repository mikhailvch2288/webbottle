from bottle import post, request, redirect
import re
import json



shame1 = re.compile(r"[0-9]")
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
         
    if shame1.match(pay) is None:
            return "Неверный номер карты"  
    
    products[mail] = product
    pdb.set_trace()
    with open ('orders.txt', 'w') as txtquest:
        json.dump(products, txtquest,ensure_ascii=False)    
    return "Спасибо! Ваш заказ внесен в базу. %s" % mail

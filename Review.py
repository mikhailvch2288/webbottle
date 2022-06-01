from bottle import post, request, redirect
import re

import json

orders = {}

shame = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})')
shame1 = re.compile(r'(\A[A-Z]+[a-z])')
@post('/home', method='post')
def my_form():

    mail = request.forms.get('MAIL')
    Nickname = request.forms.get('NICKNAME')
    review = request.forms.get('REVIEW')
    

    if review == "" or mail == "" or Nickname == "":
        return "Invalid inserts"
   
    if shame.match(mail) is None:
             return "Invalid mail"
    if shame1.match(Nickname) is None:
             return "Invalid Nickname" 

    order =  Nickname + "(" + mail + ")" + ":" + review + " "


    new_string = order[:-2]

    new_string = new_string + "."
    with open('orders1.txt','a') as txtorder:   
        txtorder.write("\n" + new_string)
    return "Thank you for the order!"

#проверка имени
def isCorrectNameT(Nickname: str):
    pattern = re.compile(r'(\A[A-Z]+[a-z])')
    if pattern.match(Nickname):
        return True
#проверка имени
def isCorrectNameF(Nickname: str):
    pattern = re.compile(r'(\A[A-Z]+[a-z])')
    if pattern.match(Nickname) is None:
        return False
#проверка фамилии
def isCorrectNicknameT(mail: str):
    pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})')
    if pattern.match(mail):
        return True
#проверка фамилии
def isCorrectNicknameF(mail: str):
    pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})')
    if pattern.match(mail) is None:
        return False

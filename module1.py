from bottle import post, request, redirect
import re
import json

company={}
shame = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})')


@post('/revi', method='post')
def my_form():

    

    Nickname = request.forms.get('NICKNAME')
    mail = request.forms.get('MAIL')
    otz = request.forms.get('OTZYV')


    if (Nickname == '' or Nickname is None) or (mail == '' or mail is None): 
             return "!!!"

    if shame.match(mail) is None:
             return "Invalid email"



    quest= str(mail) + " - "+ str(Nickname)

    #company[email]=description


    new_str = quest
    with open('review.txt','a') as pq:
        pq.write("\n"+new_str)
    return "Thanks! The application will be sent to the email %s" % mail

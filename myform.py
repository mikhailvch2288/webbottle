from bottle import post, request
import re
import pdb
import json
questions={}
sh = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})')

@post('/home', method='post')
def my_form():
    quest = request.forms.get('QUEST')
    mail = request.forms.get('ADRESS')
    if quest == '' or mail == '':
        return "Some fields are empty. Fill they all"
    if sh.match(mail) is None:
             return "Invalid mail address"    

    questions[mail]=quest
    #pdb.set_trace()
    with open ('question.txt','w') as txtquest:
        json.dump(questions,txtquest)
    return "Thanks! The answer will be sent to the mail %s" % mail
    

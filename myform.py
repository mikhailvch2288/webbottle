from bottle import post, request, redirect
import re
import json

company={}
shame = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})')
shame2 = re.compile(r'(\A[A-Z]+[a-z])')

@post('/partner', method='post')
def my_form():

    if(fill_up('REQUEST','EMAIL')is False):
        return "Заполните все поля!!!"

    description= request.params.REQUEST
    email = request.params.EMAIL

    company[email]=description
    with open('partner.txt','w') as pq:
        json.dump(company,pq)
    return "Thanks! The application will be sent to the email %s" % email
    
def fill_up(*words):
    for i in words:
        word = request.forms.get(i)
        if(not word): return False

    return True


def checkmail(quest,mail):
    if quest == '' or mail == '':
        return "Some fields are empty. Fill they all"
    if shame.match(mail) is None:
             return "Invalid mail address"    


    #pdb.set_trace()
    #with open ('question.txt','w') as txtquest:
        #json.dump(questions,txtquest)
    return None
    


#проверка описания
def isCorrectdescriptionT(description: str):
    pattern = re.compile(r'(\A[A-Z]+[a-z])')
    if pattern.match(description):
        return True

#проверка описания
def isCorrectdescriptionF(description: str):
    pattern = re.compile(r'(\A[A-Z]+[a-z])')
    if pattern.match(description) is None:
        return False
#проверка почты
def isCorrectmailTrue(email: str):
    pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})')
    if pattern.match(email):
        return True
#проверка почты
def isCorrectmailFalse(email: str):
    pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})')
    if pattern.match(email) is None:
        return False
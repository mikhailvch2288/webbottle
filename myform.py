from bottle import post, request, redirect
import re
import json

company={}
shame = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})')
shame2 = re.compile(r'(\A[A-Za-zа-яА-Я])')


@post('/partner', method='post')
def my_form():

    

    description= request.forms.get('TEXT')
    email = request.forms.get('EMAIL')


    if (description == '' or description is None) or (email == '' or email is None): 
             return "Заполните все поля!!!"

    if shame.match(email) is None:
             return "Invalid email"



    quest= str(email) + " - "+ str(description)

    #company[email]=description


    new_str = quest
    with open('partner.txt','a') as pq:
        pq.write("\n"+new_str)
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
    


def IsCorrectdescriptionF(description: str):
    if shame2.match(description) is None:
        return False

def IsCorrectdescriptionT(description: str):
    if shame2.match(description):
        return True

#проверка почты
def isCorrectmailTrue(email: str):
    #pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})')
    if shame.match(email):
        return True
#проверка почты
def isCorrectmailFalse(email: str):
    #pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})')
    if shame.match(email) is False:
        return False
from bottle import post, request
import re
import pdb
import json
import os
import datetime

@post('/actUsers', method='post')
def my_form():
    users={}
    user=request.forms.get('user')
    num = request.forms.get('num')
    text=request.forms.get('text')
    data = datetime.datetime.now().strftime("%d-%m-%Y")
    if os.stat('users.txt').st_size !=0:
        with open('users.txt') as fr: #открытие файла для чтения
            users=json.load(fr)
            fr.close()
            with open('users.txt', 'w') as f: #открытие файла для записи
                users[num]={'num':num,'name':user,'text':text,'data':data}
  
                json.dump(users, f)
                f.close()
                return "Added user %s" % num



@post('/home', method='post')
def home():
    questions={}
    d_test = dict(); 
    regex_email=(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    question=request.forms.get('QUEST')
    mail = request.forms.get('ADRESS')
    #question="what"
    #mail="a@gmaieioqfj33n4y5yoi43567...,l.com"
    if (question=="" and mail ==""):
        return "You didn't enter a question and email!"
    elif mail=="":
        return "You didn't enter an email!"
    elif question=="":
        return "You didn't enter a question!"
    else: 
        if not re.search(regex_email,mail):
           # return "Incorrect email!"
            d_test['cor']=False
            d_test['incor']=True
            #return d_test
        else:
            d_test['incor']=False
            d_test['cor']=True
            
            if os.stat('data.txt').st_size !=0:
                with open('data.txt') as fr: #открытие файла для чтения
                    questions=json.load(fr)
                fr.close()
            with open('data.txt', 'w') as f: #открытие файла для записи
                questions[mail]=question
                json.dump(questions, f)
            f.close()
            return "Thanks! The answer will be sent to the mail %s" % mail
            #return d_test
            

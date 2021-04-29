from bottle import post, request
import re
import pdb
import json
import os

@post('/home', method='post')



def my_form():
    questions={}
    d_test = dict(); 
    regex_email=(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    #question=request.forms.get('QUEST')
    #mail = request.forms.get('ADRESS')
    question="what"
    mail="a@gmail.com"
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
            return d_test
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
            #return "Thanks! The answer will be sent to the mail %s" % mail
            return d_test

   
            

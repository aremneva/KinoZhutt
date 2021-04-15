from bottle import post, request
import re
import pdb
import json
import os

@post('/home', method='post')

def my_form():
    questions={}
    regex_email=(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    question=request.forms.get('QUEST')
    mail = request.forms.get('ADRESS')
    if (question=="" and mail ==""):
        return "You didn't enter a question and email!"
    elif mail=="":
        return "You didn't enter an email!"
    elif question=="":
        return "You didn't enter a question!"
    else: 
        if not re.search(regex_email,mail):
            return "Incorrect email!"
        else:
            if os.stat('data.txt').st_size !=0:
                with open('data.txt') as fr: #открытие файла для чтения
                    questions=json.load(fr)
                fr.close()
            with open('data.txt', 'w') as f: #открытие файла для записи
                questions[mail]=question
                json.dump(questions, f)
                f.write("\n")
            f.close()
            #pdb.set_trace()
            return "Thanks! The answer will be sent to the mail %s" % mail

   
            

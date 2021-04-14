from bottle import post, request
import re
import pdb
import json

@post('/home', method='post')
def my_form():
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
            questions={}
            questions[mail]=question
            with open('data.txt', 'a+') as f: #открытие файла для записи
                json.dump(questions, f)
                f.write('\n') 
                f.close()
            
            #pdb.set_trace()
            return "Thanks! The answer will be sent to the mail %s" % mail

   
            

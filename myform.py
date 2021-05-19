from bottle import post, request

import re, pdb, json, os, checks

@post('/home', method='post')
def my_form():
    question = request.forms.get('QUESTION')
    mail = request.forms.get('ADRESS')
    warning = ""
    if question=="" or mail=="":
        return "Fill all the fields!"
    else:
        if not myform_mail.input_check.mail_correct(mail):
            return "Your email seems to be invalid"
        else:
            questions = {}
            if os.stat('questions.txt').st_size != 0:
                with open('questions.txt') as file:
                    questions = json.load(file)
                file.close()
            questions[mail] = question
            with open('questions.txt','w') as outfile:
                json.dump(questions, outfile)
            outfile.close()
            return "Thanks! The answer will be sent to the mail %s" % mail


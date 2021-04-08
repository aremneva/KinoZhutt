from bottle import post, request

import re

@post('/home', method='post')
def my_form():
    question = request.forms.get('QUESTION')
    mail = request.forms.get('ADRESS')
    warning = ""
    if question=="" or mail=="":
        return "Вы не заполнили все поля!"
    else:
        regex = re.compile('^[A-Za-z0-9\._]+@[A-Aa-z0-9]+(\.[A-Za-z]+)+$')
        if not re.match(regex,mail):
            return "Your email seems to be invalid"
        else:
            return "Thanks! The answer will be sent to the mail %s" % mail
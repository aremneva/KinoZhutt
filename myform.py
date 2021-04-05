from bottle import post, request

@post('/home', method='post')
def my_form():
    question=request.forms.get('QUEST')
    mail = request.forms.get('ADRESS')
    if (question=="" and mail ==""):
        return "You didn't enter a question and email!"
    elif mail=="":
        return "You didn't enter an email!"
    elif question=="":
        return "You didn't enter a question!"
    else: 
        return "Thanks! The answer will be sent to the mail %s" % mail
        

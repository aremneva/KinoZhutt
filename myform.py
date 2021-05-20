from bottle import post, request
import re
import pdb
import json
import os
import datetime
import date_test

@post('/actUsers', method='post')
def my_form():
    list_date_cor=["03.08.2020","14.12.2000","10-02-2015","3.4.2021","31.02.2020","04.10.2004","07/02/2013","5.3.2012","12.05.2021"]
    list_date_incor=["0.08.2020","14.12.200","40.02.2015","3.34.2021","31.13.2020","04..10.2004","07.2013","5.0.212","12.05./2021"]
    regex_data ="^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.][0-9]{4}\d\d$"
   

    users={}
    #Получение введенных данных
    user=request.forms.get('user')
    num = request.forms.get('num')
    text=request.forms.get('text')
    data=request.forms.get('data')

    #Проверки на пустые поля
    if (text==""):
        return "You didn't enter a description"
    #data = datetime.datetime.now().strftime("%d-%m-%Y")
    elif (num==""):
        return "You didn't enter a position"
    elif (user==""):
        return "You didn't enter an username"
    elif (data==""):
        return "You didn't enter a data"
    if not date_test.date_cor(data): #Сравнение даты с регулярным выражением
        return "Incorrect data! %s" %data

    if os.stat('users.txt').st_size !=0: 
        with open('users.txt') as fr: #открытие файла для чтения
            users=json.load(fr) #Чтение из файла в словарь users
            fr.close()
        with open('users.txt', 'w') as f: #открытие файла для записи
            users[num]={'num':num,'name':user,'text':text,'data':data} #Запись данных в users
            json.dump(users, f) #Запись в json из словаря users
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
            

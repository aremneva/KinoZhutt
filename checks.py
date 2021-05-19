import re, datetime
from datetime import datetime

class input_check:
    
    def mail_correct(mail):
        regex = re.compile('^[A-Za-z0-9\._]+@[A-Za-z0-9]+(\.[A-Za-z]{2,3})+$')
        return re.match(regex,mail) is not None

    # метод для проверки даты
    def written_date_correct(date_input):
        # проверка регулярным выражением
        regex = re.compile('^[0-9]{4}-[0-9]{2}-[0-9]{2}$')
        if re.match(regex, date_input) is None:
            return False

        try:
            # попытка перевести строку в datetime 
            date = datetime.strptime(date_input, '%Y-%m-%d')
            # проверка того, что введенная дата не больше текущей
            if date <= datetime.today():
                return True
            else: return False
        # вызов исключения в случае неудачи перевода в datetime
        except ValueError:
            return False




import re
def date_cor(date):
    regex_data ="^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$"
    if re.match(regex_data, date) is None: #Проверка даты по регулярному выражению, если нет совпадений - проверка не пройдена
        return False
    else:
        return True
from bottle import post, request
import json, checks, datetime

@post('/articles', method='post')
# метод для добавления в файл информации о статьях
def add_article():
    # берем введенные значения, а также текущую дату
    title = request.forms.get('TITLE')
    description = request.forms.get('DESCRIPTION')
    author = request.forms.get('AUTHOR')
    published_date = datetime.date.today().isoformat()
    written_date = request.forms.get('WRITTEN_DATE')
    # проверка того, все ли поля заполнены
    if title=="" or description=="" or author=="" or written_date=="":
        return "Fill all the fields!"

    # вызов метода для проверки корректности ввода даты написания статьи
    if not checks.input_check.written_date_correct(written_date):
        return "Data should have a format 'YYYY-MM-DD' and not be after today"
    # открытие файла для чтения для подсчета количества статей
    with open('./articles.json', 'r') as file:
        articles=json.load(file)
        articles_number = len(articles)
    # открытие файла для записи
    with open('./articles.json', 'w') as file:
        articles[articles_number+1] = {'author':author, 'title':title,'description':description,
                                       'published_date': published_date, 'written_date': written_date}
        json.dump(articles, file)

    return "The article is added!"



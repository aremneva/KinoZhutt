from bottle import post, request
import datetime, json

@post('/articles', method='post')
def add_article():
    title = request.forms.get('TITLE')
    description = request.forms.get('DESCRIPTION')
    author = request.forms.get('AUTHOR')
    published_date = datetime.date.today().isoformat()
    written_date = request.forms.get('WRITTEN_DATE')

    with open('./articles.json', 'r') as file:
        articles=json.load(file)
        articles_number = len(articles)

    with open('./articles.json', 'w') as file:
        articles[articles_number+1] = {'author':author, 'title':title, 'description':description, 'published_date': published_date, 'written_date': written_date}
        json.dump(articles, file)

    return "The article is added!"


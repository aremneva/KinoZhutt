% rebase('layout.tpl', title=title, year=year)
%import json

<head>
<title> Articles </title>
<style>
    .content{
        width:400px;
        height:200px;
        border:1px;
        display:inline-block;
    }
     p {
    font-family: Verdana, Arial, Helvetica, sans-serif; 
    font-size: 12pt; /* Размер шрифта в пунктах */ 
   }

    </style>
</head>
<body>

<div class="jumbotron">
    <h1>KinoZhutt</h1>
</div>

<h2> Articles to read</h2>

%with open('./articles.json') as articles:
%data=json.load(articles)
%for key, value in data.items():
    <div>
        <h3 style="margin-top:40px">
        {{value['title']}}
        </h3>
        <p>
        {{value['description']}}
        </p>
        <p style="font-size:10pt">
        By {{value['author']}}
        </p>
        <p style="font-size:10pt">
        Published on {{value['published_date']}}, written on {{value['written_date']}}
        </p>
    </div>
%end

<h2> Add your own article</h2>

<form action="/articles" method="post">
        <p><input rows="2" cols="50" name="TITLE" placeholder="Your article's title"></p>
        <p><textarea type="text" size="50" name="DESCRIPTION" placeholder="Your article's description"></textarea></p>
        <p><input rows="2" cols="50" name="AUTHOR" placeholder="Your name"></p>
        <p><input rows="2" cols="50" name="WRITTEN_DATE" placeholder="A date when you wrote the article"></p> 
        <p><input type="submit" value="Add" class="btn btn-default"></p>
</form>

</body>
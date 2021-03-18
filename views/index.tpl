% rebase('layout.tpl', title='Home Page', year=year)

<div class="jumbotron">
    <h1>KinoZhutt</h1>
    <p class="lead">KinoZhutt is a website with horrors and trillers for all tastes (but not for all ages).</p>
    <style>
    img {
    width: 350px;
    height: 200px;
    object-fit: cover;
    margin-right: 10px;
    margin-top: 20 px;
    }

    .box {
   display: flex;
   align-items: top;
}
    </style>
</div>

<div class="row">
    <div class="col-md-6">

        <h2>Brand new articles</h2>
        <div class="box">
        <img src="static\images\cat.jpg">
        <br>
        <p>
            This is just a cat. It's cute. This is just a cat. It's cute. 
        </p>
        </div>

        <br> <br>

        <div class="box">
        <img src="https://fastly.syfy.com/sites/syfy/files/styles/1200x680/public/2020/08/seafever_0hero.jpg?offset-y=0">
        <p>
        8 Indie horror movies from 2020 you can watch right now
        </p>
        </div>

    </div>
    <div class="col-md-6">
        <h2>Hot films</h2>
        <p>Here's supposed to be films. Yeah.</p>
        <p><a class="btn btn-default" href="https://pypi.python.org/pypi">Learn more &raquo;</a></p>
    </div>
</div>

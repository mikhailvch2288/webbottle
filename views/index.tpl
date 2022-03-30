% rebase('layout.tpl', title='Home Page', year=year)    


<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Новости сегодня</title>
    <link rel="stylesheet" type="text/css" href="/static/content/bootstrap.min.css" />
    <link rel="stylesheet" type="text/css" href="/static/content/site.css" />
    <script src="/static/scripts/modernizr-2.6.2.js"></script>
</head>



<div class="jumbotron">
   <img src="static\images\news.png">
    <p> </p>
    <p class="lead">Мы группа студентов, представляющие проект "Сайт СМИ"</p>
    <p><a href="https://guap.ru/emtp" class="btn btn-primary btn-large">Узнать больше... &raquo;</a></p>
</div>

<div class="row">
<meta charset="utf-8" />
    <div class="col-md-4">
        <h2>Кто мы?</h2>
        <p>
            Мы независимое студенческое СМИ, говорим о темах, волнующие студентов, следим за информацией в реальном времени!
        </p>
        <p><a class="btn btn-default" href="https://new.guap.ru/urmisk/vpolet">Learn more &raquo;</a></p>
    </div>
    <div class="col-md-4">
        <h2>Главный редактор</h2>
        
        <p><a class="btn btn-default" href="https://vk.com/fastback228">Главный редактор &raquo;</a></p>
    </div>
    <div class="col-md-4">
        <h2>Заместители редактора</h2>
        
        <p><a class="btn btn-default" href="https://vk.com/karlrex12">1-й заместитель главного редактора &raquo;</a></p>
        <p><a class="btn btn-default" href="https://vk.com/jungawoonga">2-й заместитель главного редактора &raquo;</a></p>
    </div>
    
</div>




    <h3> Ask a Question </h3>
    <form action="/home" method="post">
        <p><textarea rows="2" cols="50" name="QUEST" placeholder="Your question"></textarea></p> 
        <p><input type="text" size="50" name="ADRESS" placeholder="Your email"></p>
        <p><input type="submit" class="btn btn-default" value="Send"></p>
    </form>


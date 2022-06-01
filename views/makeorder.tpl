% rebase('layout.tpl', title=title, year=year) 
<!-- 
Заголовок страницы 
--> 
<h2>_________</h2> 
<!-- 
Описание и вставка картинки 
--> 
<h3>leave your feedback</h3> 
<!-- Присваивание для файла py --> 
<form action="/home" method="post"> 
        <p><input type="text" cols="50" name="NICKNAME" placeholder="Nickname"></p>  
        <p><input type="text" size="50" name="MAIL" placeholder="mail"></p> 
        <p><textarea rows="5" columns="20" cols="100" name="REVIEW" placeholder="review"></textarea></p> 
        <p><input type="submit" value="send review!" class="btn btn-default" size="100"></p> 
 

 
<h5>Reviw</h5> 
<!-- Заполнение отзывов --> 
%f = open('orders1.txt', 'r+') 
%lines = f.readlines() 
%for line in reversed(lines): 
<div class="container"> 
  <p style="border:">{{line.strip()}}</p> 
   
</div> 
%end 
 
 
 
<!-- 
Отделение от меню для нижнего заголовка сайта 
--> 
</form> 
 
<div style="clear:both"></div>
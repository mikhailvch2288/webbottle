% rebase('layout.tpl', title=title, year=year) 
<!-- 
Заголовок страницы 
--> 
<h2>Make a order</h2> 
<!-- 
Описание и вставка картинки 
--> 
<h3>ostafte svoi otzyv</h3> 
<!-- Присваивание для файла py --> 
<form action="/otz" method="post"> 
        <p><input type="text" cols="50" name="Nickname" placeholder="Nickname"></p>  
        <p><input type="text" size="50" name="Mail" placeholder="Mail"></p> 
        <p><input type="text" size="50" name="otzyv" placeholder="otzyv"></p> 
        <p><input type="submit" value="Confirm your order!" class="btn btn-default" size="100"></p> 
 
<!-
Отделение от меню для нижнего заголовка сайта 
--> 
</form>
% rebase('layout.tpl', title=title, year=year)

<h2>{{ title }}.</h2>
<h3>{{ message }}</h3>

<h3> Хотите стать нашим партнёром? </h3>
    <form action="/orders" method="post">
        <p><textarea rows="5" columns="20" cols="100" name="QUEST" placeholder="Продукты"></textarea></p> 
        <p><input type="text" size="100" name="ADDRESS" placeholder="Ваш адрес" ></p>
        <p><input type="text" size="100" name="MAIL" placeholder="Ваша почта" ></p>
        <p><input type="text" size="100" name="PAYMENT" placeholder="Ваш номер карты" ></p>
        <p><input type="submit" class="bot1" value="Добавить заказ"></p>
    </form>

<address>
    <strong>Support:</strong>   <a href="mailto:Support@example.com">fastback9a@gmail.com</a><br />
    <strong>Marketing:</strong> <a href="mailto:Marketing@example.com">velnik2003@gmail.com</a>
</address>

 

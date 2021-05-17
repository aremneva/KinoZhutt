% rebase('layout.tpl', title=title, year=year)
%import json
<h1>Active users!</h1>
<br>
<style>
    .content{
        width:400px;
        height:200px;
        border:2px ;
		
       
    }
     p {
    font-family: Verdana, Arial, Helvetica, sans-serif; 
    font-size: 12pt; /* Размер шрифта в пунктах */ 
   }
   .button {
  background-color: #242425;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-radius: 16px;
}
}
</style>
%with open('./users.txt') as users:
	%data=json.load(users)
	%a = 20
	
	<h2>Top active users:</h2>
	<br>
	<br>
	<br>
%for key, value in data.items():
	<div class=content>
	
	<p width=200 height=350> {{value}}</p>
	<hr>
	</div>
	
%end 
<div class=blocktext>
<h3> Add user </h3>
<form action="/actUsers" method="post">
		<p><textarea rows="2" cols="50" name="num" placeholder="Position"></textarea></p> 
        <p><textarea rows="2" cols="50" name="user" placeholder="User"></textarea></p> 
        <p > <input type="submit"  class="button button" value="Send"></p>
</form>
</div>



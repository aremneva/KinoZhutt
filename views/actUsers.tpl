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
	
	<h2>Top active users:</h2>
	<br>
	<br>
	<br>
%for key, val in data.items():
	<div class="jumbotron jumbotron-fluid">	
	<div class="container">
	<p width=200 height=350><font size="5" color="gray" face="Arial">#{{val['num']}}</font></p>
	<p><font size="4" color="gray" face="Arial">User: </font></p>
	<p width=200 height=350> <font size="5" color="gray" face="Arial">{{val['name']}}</font></p>
	<p><font size="4" color="gray" face="Arial">Description: </font></p>
	<p width=200 height=350> <font size="5" color="gray" face="Arial">{{val['text']}}</font></p>
	<div align="right">
	<p width=200 height=350> <font size="3" color="gray" face="Arial">{{val['data']}}</font></p>
	</div>
	</div>
	</div>
%end 
	<div class="junbotron">
	<h3> Add user </h3>
	<form action='/actUsers' method='post'>
		<p><textarea rows="2" cols="50" name="num" placeholder="Position"></textarea></p> 
        <p><textarea rows="2" cols="50" name="user" placeholder="User"></textarea></p> 
		<p><textarea rows="2" cols="50" name="text" placeholder="Description"></textarea></p> 
		
        <p> <input type="submit"  class="button button" value="Send"></p>
		
</form>
</div>



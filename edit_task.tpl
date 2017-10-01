<link rel="stylesheet" href="/css/app.css">
<div class="title">
	     <h1> TO-DO LIST </h1>
	     <ul>
	     <li><a href="/" > View Tasks</a> </li>
	        <li><a href="/new" class="active"> Add Task</a></li>
	     </ul>
			 <div class="add">
	     <p>Edit an existing task in the ToDo list:</p>
<form action="/edit/{{id}}" method="POST">
  <input type="text" size="50" maxlength="100" name="task">{{text}}</input>
  <input type="submit" name="save" value="save">
</form>

</div>
	</div>

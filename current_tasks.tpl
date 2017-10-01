%#template to generate a HTML table from a list of tuples (or list of lists, or tuple of tuples or ...)
<link rel="stylesheet" href="/css/app.css">
<div class="title">
	     <h1> TO-DO LIST </h1>
	     <ul>
	     	<li><a href="/" class="active"> View Tasks</a> </li>
	        <li><a href="/new"> Add Task</a></li>
	       	
	     </ul>
	     <div class="items">
	     	<table >
%for row in rows:
  <tr>
  %for col in row:
    <td>{{col}}<a href="/edit/{{row[0]}}">Edit</a><a href="/delete/{{row[0]}}">Delete</a></td>
		<td></td>
		<td></td>
  %end
  </tr>
%end
</table>
	     </div>
	</div>


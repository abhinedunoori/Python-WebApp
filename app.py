import sqlite3
from bottle import route, run, template, debug, request, static_file

@route('/css/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./css/')

@route('/')
@route('/index.html')
@route('/tasks')
def tasks():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    c.close()
    output = template('current_tasks', rows=result)
    return output

@route('/new', method='GET')
def new():
    return template('new_task')    

@route('/new', method='POST')
def new_item():
    new = request.POST.task.strip()

    conn = sqlite3.connect('todo.db')
    c = conn.cursor()

    c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new, 1))
    new_id = c.lastrowid

    conn.commit()
    c.close()

    return template('task_added')

@route('/edit/<id>', method='GET')
def edit(id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task, status FROM todo WHERE id LIKE ?",(id,))
    result = c.fetchall()
    if len(result) == 0:
        return "Error: wrong number of results"
    result = result[0]
    id, text, status = result
    c.close()
    output = template('edit_task', id=id, text=text, status=status)
    return output

@route('/edit/<id>', method='POST')
def edit(id):
    updated_task = request.POST.task.strip()

    conn = sqlite3.connect('todo.db')
    c = conn.cursor()

    c.execute("UPDATE todo SET task = ? WHERE id LIKE ?", (updated_task,id))
    new_id = c.lastrowid

    conn.commit()
    c.close()
    return template('edited')

@route('/delete/<id>', method='GET')
def delete(id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("DELETE from todo WHERE id LIKE ?", (id,))

    conn.commit()
    c.close()

    return template('deleted')

debug(True)
run(host='localhost', port=8080, reloader=True)
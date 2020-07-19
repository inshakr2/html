#!C:\Users\user\anaconda3\python.exe
import sys
import io

sys.stdout=io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
print("content-type: text/html; charset=utf-8\n")
import cgi
import os

files = os.listdir('data')
li = ''
for item in files:
    li += '<li><a href="index.py?id={file}">{file}</a></li>'.format(file = item)

form = cgi.FieldStorage()

if "id" in form:
    pageId = form["id"].value
    description = open('data/' + pageId, 'r', encoding='UTF8').read()
    update_link = '<a href = update.py?id={}>update</a>'.format(pageId)
    delete_action = '''
        <form action="process_delete.py" method='post'>
            <input type='hidden' name='pageId' value={}>
            <input type='submit' value='delete'>
        </form>
    '''.format(pageId)
else:
    pageId = 'Welcome'
    description = 'Hello, Flask'
    update_link = ''
    delete_action = ''

print('''
<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>{list}</ol>
  <a href="creat.py">creat</a>
  {update_link}
  {delete}
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(list = li, update_link = update_link ,title=pageId, desc=description, delete = delete_action))

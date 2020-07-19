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
else:
    pageId = 'Welcome'
    description = 'Hello, Flask'

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
  <form action="process_creat.py" method='post'>
      <p><input type="text" name="title" placeholder="title"></p>
      <p><textarea rows="4" name="description" placeholder="description"></textarea></p>
      <p><input type="submit"></p>
  </form>
</body>
</html>
'''.format(list = li,title=pageId, desc=description))

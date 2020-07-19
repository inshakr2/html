#!C:\Users\user\anaconda3\python.exe
import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

import cgi
import os

form = cgi.FieldStorage()
pageId = form['pageId'].value

os.remove('data/' + pageId)

print("Location: index.py" + '\n')

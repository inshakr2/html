#!C:\Users\user\anaconda3\python.exe
import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

import cgi
import os

form = cgi.FieldStorage()
pageId = form["pageId"].value
title = form["title"].value
description = form["description"].value


file = open('data/' + pageId, 'w')
file.write(description)
file.close()

os.rename('data/'+pageId, 'data/'+title)

print("Location: index.py?id="+title+'\n')

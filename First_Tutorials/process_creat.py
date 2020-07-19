#!C:\Users\user\anaconda3\python.exe
import sys
import io
sys.stdout=io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr=io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

import cgi

form = cgi.FieldStorage()
title = form["title"].value
description = form["description"].value


file = open('data/' + title, 'w')
file.write(description)
file.close()

print("Location: index.py?id="+title+'\n')

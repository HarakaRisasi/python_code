# -*- coding: utf-8 -*-
import subprocess
subprocess.call("clear")

# Urllib — это модуль Python, который можно использовать для открытия URL-адресов. 
# Он определяет функции и классы для обработки URL-адресов.
# С помощью Python вы также можете получать и получать данные из Интернета, такие как XML, HTML, JSON и т. д. 
# #


from urllib.request import urlopen

myURL = urlopen("http://pythonscraping.com/pages/page1.html")
# this outputs the HTML file page1.html, found in the directory <web root>/pages, 
# on the server located at the 'http://pythonscraping.com/pages/page1.html'
print(myURL.read())
#urlopen - it can read HTML files, image files, or any other file stream with ease
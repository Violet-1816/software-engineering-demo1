#!C:\Users\user\AppData\Local\Microsoft\WindowsApps\python.exe
#-*- coding: utf-8 -*-
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import cart

print("Content-type: text/html; charset: utf-8\n")
sys.stdout.flush()

form = cgi.FieldStorage()
name = form.getvalue('name')
content = form.getvalue('content')
price = form.getvalue('price')
amount = form.getvalue('amount')

target=""

if cart.addStock(name, content, price, amount):
    target = "<p>add stock success!</p>"
else:
    target = "<p>add stock failure!</p>"


with open("template.html",'rb') as fp:
    st=fp.read()
    st=st.replace(b"#content#",target.encode())
    st=st.decode()
    sys.stdout.write(st)
sys.stdout.flush()
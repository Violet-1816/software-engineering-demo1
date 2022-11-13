#!C:\Users\user\AppData\Local\Microsoft\WindowsApps\python.exe
#-*- coding: utf-8 -*-
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import cart

print("Content-type: text/html; charset: utf-8\n")
sys.stdout.flush()

form = cgi.FieldStorage()
sid = form.getvalue('sid')
name = form.getvalue('name')
content = form.getvalue('content')
price = form.getvalue('price')
amount = form.getvalue('amount')

target=""

if name != None:
    if cart.updateStockName(sid, name):
        target += f"<p>update id={sid} name success!</p>"
    else:
        target += f"<p>update id={sid} name failure!</p>"
else:
    target += f"<p>id={sid} name not update</p>"

if content != None:
    if cart.updateStockContent(sid, content):
        target += f"<p>update id={sid} content success!</p>"
    else:
        target += f"<p>update id={sid} content failure!</p>"
else:
    target += f"<p>id={sid} content not update</p>"

if price != None:
    if cart.updateStockPrice(sid, price):
        target += f"<p>update id={sid} price success!</p>"
    else:
        target += f"<p>update id={sid} price failure!</p>"
else:
    target += f"<p>id={sid} price not update</p>"

if amount != None:
    if cart.updateStockAmount(sid, amount):
        target += f"<p>update id={sid} amount success!</p>"
    else:
        target += f"<p>update id={sid} amount failure!</p>"
else:
    target += f"<p>id={sid} amount not update</p>"

with open("template.html",'rb') as fp:
    st=fp.read()
    st=st.replace(b"#content#",target.encode())
    st=st.decode()
    sys.stdout.write(st)
sys.stdout.flush()
#!C:\Users\user\AppData\Local\Microsoft\WindowsApps\python.exe
#-*- coding: utf-8 -*-
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import cart

print("Content-type: text/html; charset: utf-8\n")
sys.stdout.flush()

form = cgi.FieldStorage()
cid = form.getvalue('cid')
amount = form.getvalue('amount')

target=""

if cart.addCartAmount(cid, amount):
    target = "<p>update cart success!</p>"
else:
    target = "<p>update cart failure!</p>"

with open("template.html",'rb') as fp:
    st=fp.read()
    st=st.replace(b"#content#",target.encode())
    st=st.decode()
    sys.stdout.write(st)
sys.stdout.flush()
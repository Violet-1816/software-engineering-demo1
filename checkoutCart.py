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

target=""

if cart.checkoutCart(cid):
    target = f"<p>checkout cart id={cid} success!</p>"
else:
    target = f"<p>checkout cart id={cid} failure!</p>"


with open("template.html",'rb') as fp:
    st=fp.read()
    st=st.replace(b"#content#",target.encode())
    st=st.decode()
    sys.stdout.write(st)
sys.stdout.flush()
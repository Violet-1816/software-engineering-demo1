#!C:\Users\user\AppData\Local\Microsoft\WindowsApps\python.exe
#-*- coding: utf-8 -*-
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import cart

print("Content-type: text/html; charset: utf-8\n")
sys.stdout.flush()

target=""

if cart.delChecked():
    target = "<p>delete checked cart success!</p>"
else:
    target = "<p>delete checked cart failure!</p>"


with open("template.html",'rb') as fp:
    st=fp.read()
    st=st.replace(b"#content#",target.encode())
    st=st.decode()
    sys.stdout.write(st)
sys.stdout.flush()
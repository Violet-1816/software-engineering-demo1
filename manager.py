#!C:\Users\user\AppData\Local\Microsoft\WindowsApps\python.exe
#-*- coding: utf-8 -*-
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import cart

print("Content-type: text/html; charset: utf-8\n")
sys.stdout.flush()

stock = cart.getList()
target=""

target += "<p>stock:</p>"
for (sid, name, content, price, amount) in stock:
    target += f"<li>id={sid} name={name} content={content} price={price} amount={amount}</li>"

target += "<p>cart:</p>"
cartList = cart.getCartList()
for (cid, uid, sid, amount, checkout, complete) in cartList:
    target += f"<li>id={cid} user={uid} stock={sid} amount={amount} checkout={checkout} complete={complete}</li>"

addStock = (f"""
<div>
<fieldset>
<legend>add stock</legend>
<form method="post" action="addStock.py">
input name<input type="text" name='name'><br>
input content<input type="text" name='content'><br>
input price<input type="text" name='price'><br>
input amount<input type="text" name='amount'><br>
<input type="submit">
</form>
</fieldset>
</div>
""")

target += addStock

updateStock = (f"""
<div>
<fieldset>
<legend>update stock</legend>
<form method="post" action="updateStock.py">
input stock id<input type="text" name='sid'><br>
input name<input type="text" name='name'><br>
input content<input type="text" name='content'><br>
input price<input type="text" name='price'><br>
input amount<input type="text" name='amount'><br>
<input type="submit">
</form>
</fieldset>
</div>
""")

target += updateStock
title = f"manager"

with open("template.html",'rb') as fp:
    st=fp.read()
    st=st.replace(b"#content#",target.encode())
    st=st.replace(b"#title#",title.encode())
    st=st.decode()
    sys.stdout.write(st)
sys.stdout.flush()
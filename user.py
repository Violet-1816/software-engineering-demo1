#!C:\Users\user\AppData\Local\Microsoft\WindowsApps\python.exe
#-*- coding: utf-8 -*-
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import cart

print("Content-type: text/html; charset: utf-8\n")
sys.stdout.flush()

target=""
uid = [1]

stock = cart.getList()
target += "<p>stock:</p>"
for (sid, name, content, price, amount) in stock:
    if(amount != 0):
        target += f"<li>id={sid} name={name} content={content} price={price} amount={amount}</li>"

cartContent = cart.getCart(uid)
target += "<p>cart:</p>"
for (cid, sid, amount, checkout, complete) in cartContent:
    name = cart.getStockName([sid])
    target += f"<li>cart id={cid} name={sid} amount={amount} checkout = {checkout} complete = {complete}</li>"
    
addCart = (f"""
<div>
<fieldset>
<legend>add cart</legend>
<form method="post" action="addCart.py">
input stock id<input type="text" name='sid'><br>
input amount<input type="text" name='amount'><br>
<input type="submit">
</form>
</fieldset>
</div>
""")

target += addCart

updateCart = (f"""
<div>
<fieldset>
<legend>update cart</legend>
<form method="post" action="updateCart.py">
input cart id<input type="text" name='cid'><br>
input amount<input type="text" name='amount'><br>
<input type="submit">
</form>
</fieldset>
</div>
""")

target += updateCart

checkoutCart = (f"""
<div>
<fieldset>
<legend>delete checked</legend>
<form method="post" action="checkoutCart.py">
input cart id<input type="text" name='cid'><br>
<input type="submit">
</form>
</fieldset>
</div>
""")

target += checkoutCart
title = f"user"

with open("template.html",'rb') as fp:
    st=fp.read()
    st=st.replace(b"#content#",target.encode())
    st=st.replace(b"#title#",title.encode())
    st=st.decode()
    sys.stdout.write(st)
sys.stdout.flush()
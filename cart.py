from dbConfig import conn, cur


def getList():
    sql = "select sid, name, content, price, amount from stock order by sid;"
    cur.execute(sql)
    records = cur.fetchall()
    return records

def addStock(name, content, price, amount):
    sql = "insert into stock (name, content, price, amount) values (%s, %s, %s, %s)"
    cur.execute(sql, (name, content, price, amount))
    conn.commit()
    return True

def updateStockName(sid, name):
    sql = "update stock set name = %s where sid = %s;"
    cur.execute(sql, (name, sid))
    conn.commit()
    return True

def updateStockContent(sid, content):
    sql = "update stock set content = %s where sid = %s;"
    cur.execute(sql, (content, sid))
    conn.commit()
    return True
    
def updateStockPrice(sid, price):
    sql = "update stock set price = %s where sid = %s;"
    cur.execute(sql, (price, sid))
    conn.commit()
    return True

def updateStockAmount(sid, amount):
    sql = "update stock set amount = amount + %s where sid = %s;"
    cur.execute(sql, (amount, sid))
    conn.commit()
    return True

def delChecked(uid):
    sql = "select cid, sid, amount from cart where uid = %s and checkout = 1"
    cur.execute(sql, (uid))
    records = cur.fetchall()
    for (sid, amount) in records:
        tempsql = "update stock set amount = amount - %s where sid = %s"
        cur.execute(tempsql, (amount, sid))
        conn.commit()
    for(cid) in records:
        sql2 = "update cart set complete = 1 where cid = %s"
        cur.execute(sql2, (cid))
        conn.commit()
    return True

def addCart(uid, sid, amount):
    sql = "insert into cart (uid, sid, amount) values (%s, %s, %s)"
    cur.execute(sql, (uid, sid, amount))
    conn.commit()
    return True

def addCartAmount(cid, amount):
    sql = "update cart set amount = amount + %s where cid = %s"
    cur.execute(sql, (amount, cid))
    conn.commit()
    return True

def getCart(uid):
    sql = "select cid, sid, amount, checkout, complete from cart where uid = %s order by cid"
    cur.execute(sql, (uid))
    records = cur.fetchall()
    return records

def getCartList():
    sql = "select cid, uid, sid, amount, checkout, complete from cart order by cid"
    cur.execute(sql)
    records = cur.fetchall()
    return records

def getStockName(sid):
    sql = "select name from stock where sid = %s"
    cur.execute(sql, (sid))
    records = cur.fetchall()
    return records
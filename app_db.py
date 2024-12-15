from flask import Flask, render_template, request
import sqlite3


app = Flask(__name__)

@app.route("/message", methods=['GET', 'POST']) # 結果表示

def message():
    con = sqlite3.connect("test.db")
    cur = con.cursor()
    dblen, dblist = 0, []
    
    if request.method=="GET":
        var1 = None
    
    else:
        name = request.form.get('name', '')
        msg = request.form.get('msg', '')
        
        cur.execute("INSERT INTO log(name, msg) values(?,?)", (name,
        msg) )
        
        con.commit()
        
        cur.execute("SELECT * FROM log ORDER BY id DESC")
        dblist = cur.fetchall()
        
    con.close()
    
    return render_template('message.html',
dblen=len(dblist), dblist=dblist)

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=8000)
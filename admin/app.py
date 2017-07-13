from flask import Flask, render_template, request
# import sqlite3 as sql
import MySQLdb
db = MySQLdb.connect("localhost","root","abc","shilpa" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
db.rollback()
app = Flask(__name__,template_folder='./')

# @app.route('/')
# def home():
#    return render_template('home.html')

@app.route('/')
def new_student():
   return render_template('addcategory.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   if request.method == 'POST':
      try:
         catid = request.form['catid']
         categoryname = request.form['categoryname']
         price = request.form['price']
         des = request.form['des']
         msg="Done"
         print categoryname

         try:
        # print("writing","insert into product_details values(`"+idx+"`,`"+name+"`,`"+cat+"`,`"+qty+"`,`"+price+"`);")
            cursor.execute("insert into coco values('"+catid+"','"+categoryname+"','"+price+"','"+des+"');")
            print 1
            db.commit()
         except:
            cursor.execute("create table coco (cat_id varchar(10) primary key,name varchar(10),price int(10),des varchar(100));")
            cursor.execute("insert into coco values('"+catid+"','"+categoryname+"','"+price+"','"+des+"');")
            print 2
            db.commit()
             
             # with sql.connect("database.db") as con:
             #    cur = con.cursor()
                
             #    cur.execute("INSERT INTO students (name,addr,city,pin) VALUES (?,?,?,?)",(nm,addr,city,pin) )
                
             #    con.commit()
             #    msg = "Record successfully added"
      except:
         # con.rollback()
         msg = "error in insert operation"
      
      finally:
         return render_template("result.html",msg = msg)
         con.close()

# @app.route('/list')
# pass
# def list():
#    con = sql.connect("database.db")
#    con.row_factory = sql.Row
   
#    cur = con.cursor()
#    cur.execute("select * from students")
   
#    rows = cur.fetchall();
#    return render_template("list.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)
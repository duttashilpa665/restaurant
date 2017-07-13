import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","abc","shilpa" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
db.rollback()

# execute SQL query using execute() method.
# print("to write","insert into product_details values('"+idx+"','"+name+"','"+cat+"','"+qty+"','"+price+"');")
html_old=""

while(1):
	f=open("inner-2.tmpl","r")
	html_read=f.read()
	f.close()
	cursor.execute("select * from product_details;")
	result=cursor.fetchall()
	db.close()
	db = MySQLdb.connect("localhost","root","abc","shilpa" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()
	db.rollback()

	print result
	html_req=""
	tmpl="<li>#</li> <a href=\"@\">buy</a>"
	for each in result:
		sub=each[1]
		tmpl_here=tmpl.split('#')[0]+sub+tmpl.split('#')[1]
		tmpl_here=tmpl_here.split('@')[0]+"./"+sub+".html"+tmpl_here.split('@')[1]
		html_req+=tmpl_here+"\n"
		g=open("inner-3.tmpl","r")
		html_read_inner=g.read()
		html_req_inner=html_read_inner.split('<!-- INSERT HERE -->')[0]+"<div class=\"page-title\">"+sub+"</div>"+html_read_inner.split('<!-- INSERT HERE -->')[1]
		#only for display
		g.close()
		g=open(sub+".html","w")
		g.write(html_req_inner)
		g.close()

	html_final=html_read.split('<!-- INSERT HERE -->')[0]+"\n"+html_req+"\n"+html_read.split('<!-- INSERT HERE -->')[1]
	if html_final!=html_old:
		f=open("index.html","w")
		html_read=f.write(html_final)
		f.close()
		html_old=html_final
		print "Wrote to file"
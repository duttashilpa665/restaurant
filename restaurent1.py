import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","abc","shilpa" )

# prepare a cursor object using cursor() method
cursor = db.cursor()
db.rollback()

# execute SQL query using execute() method.

while 1:
	a=raw_input("Enter id, product name,category,quantity,price separated by space.to quit press 0")
	if a=="0": db.close(); exit(0)
	idx=a.split(" ")[0]
	name=a.split(" ")[1]
	cat=a.split(" ")[2]
	qty=a.split(" ")[3]
	price=a.split(" ")[4]
	# pass
	print("to write","insert into product_details values('"+idx+"','"+name+"','"+cat+"','"+qty+"','"+price+"');")
	try:
		# print("writing","insert into product_details values(`"+idx+"`,`"+name+"`,`"+cat+"`,`"+qty+"`,`"+price+"`);")
		cursor.execute("insert into product_details values('"+idx+"','"+name+"','"+cat+"','"+qty+"','"+price+"');")
		print 1
		db.commit()
	except:
		cursor.execute("create table product_details (product_id varchar(10) primary key,product varchar(10),catagory varchar(10),quantity int(10),price int(10));")
		cursor.execute("insert into product_details values('"+idx+"','"+name+"','"+cat+"','"+qty+"','"+price+"');")
		print 2
		db.commit()

# cursor.execute("create table product_details (product_id primary key varchar(10),product varchar(10),catagory varchar(10),quantity int(10),price int(10));

# Fetch a single row using fetchone() method.
# data = cursor.fetchone()

print "Database version : %s " % data

# disconnect from server
db.close()

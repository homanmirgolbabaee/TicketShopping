import sqlite3
import os
def Shop():
	con=sqlite3.connect("cart.db")
	c=con.cursor()
	c.execute('''SELECT * FROM product''')
	obj=c.fetchall()
	row_count=len(obj)
	print ('***************************************************************************')
	print ('Ticket-ID  ','Ticket-Destination  ','Ticket-Price  ','Ticket-Number')
	print ('***************************************************************************')
	i=0
	count=0
	while i<row_count:
		print ('  ',obj[i][0],' '*(12-len(obj)), obj[i][1],' '*(12-len(obj)), obj[i][2],' '*(12-len(obj)), obj[i][3])
		count+=obj[i][3]
		i=i+1
	print ('***************************************************************************')
	print ("\t Total Products in cart is:",count)
	print ('***************************************************************************')
def Add():
	pid=int(input("Enter Ticket-ID:"))
	print("ProdcutId is:",pid)
	pname=input("Enter Ticket-Destination:")
	print("Ticket-Destination is:",pname)
	pprice=int(input("Enter Ticket-Price:"))
	print("Ticket-Price is:",pprice)
	pqty=int(input("Enter Ticket-Number:"))
	print("Ticket-Number is:",pqty)
	con=sqlite3.connect("cart.db")
	c=con.cursor()
	d=c.execute("INSERT INTO product (pId,pName,pPrice,pQty) VALUES (?,?,?,?)",(pid,pname,pprice,pqty))
	con.commit()
	if(d):
			print ("Inserted successfull!!!!!!!!!!\n\n")
	else:
		print ("Soem error occured")
def Update():
	Shop()
	a=int(input("Enter Ticket-ID for updating"))
	if(a):
		pname=input("Enter Ticket-Destination:")
		print("Ticket-Destination is:",pname)
		pprice=input("Enter Ticket-Price:")
		print("Ticket-Price is:",pprice)
		pqty=input("Enter Ticket-Number:")
		print("Ticket-Number is:",pqty)
		con=sqlite3.connect("cart.db")
		c=con.cursor()
		d=c.execute("UPDATE product SET pName=?,pPrice=?,pQty=? WHERE pId=?",(pname,pprice,pqty,a))
		con.commit()
		c.close()
	else:
		print("Please provide correct input")

	
def Delete():
	Shop()
	a=input("Enter Ticket-ID for Deleting")
	if(a):
		con=sqlite3.connect("cart.db")
		c=con.cursor()
		c.execute('DELETE FROM product WHERE pId = ?',(a))
		con.commit()
		c.close()
	else:
		print("please give correct input")
print("Welcome to TicketShop With Database connection with python")
con=sqlite3.connect("cart.db")
c=con.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS product (pId int,pName text,pPrice int,pQty int)''')
con.close()
while(True):
	print("1.Shop Product\n2.Add Prodcut\n3.Update Product\n4.Delete Product\n")
	a=int(input("Enter your option:-"))
	if(a==1):
		Shop()
	elif(a==2):
		Add()
	elif(a==3):
		Update()
	elif(a==4):	
		Delete()
	else:
		print ("please provide correct input")


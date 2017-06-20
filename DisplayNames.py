import MySQLdb
db = MySQLdb.connect(host="sql10.freemysqlhosting.net",port=3306, user='', passwd='', db="")

cursor = db.cursor()


cursor.execute("SELECT nm_customer ,AVG(vl_total) FROM tb_customer_account WHERE vl_total > 560 AND id_customer BETWEEN 1500 AND 2700 group by nm_customer DESC" )

#Displays the names that are in the pattern set by selct
for row in cursor.fetchall() :
      nm_customer = str(row[0])

      print "Person's name is " + nm_customer + " "


# disconnect
db.close()

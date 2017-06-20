
import MySQLdb
db = MySQLdb.connect(host="sql10.freemysqlhosting.net",port=3306, user='', passwd='', db="")

cursor = db.cursor()

#select average
cursor.execute("SELECT  AVG(vl_total) FROM tb_customer_account WHERE vl_total > 560 AND id_customer BETWEEN 1500 AND 2700" )
data = cursor.fetchone()

#display average
print "Exiba a media final : %s " % data


# disconnect 
db.close()

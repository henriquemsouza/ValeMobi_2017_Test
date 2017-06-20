
import MySQLdb
db = MySQLdb.connect(host="sql10.freemysqlhosting.net",port=3306, user='', passwd='', db="")

cursor = db.cursor()
# Delete table if already exists 
cursor.execute("DROP TABLE IF EXISTS tb_customer_account")

# Create new table

sql = """CREATE TABLE tb_customer_account (
 id_customer INT(11),,
cpf_cnpj INT(11) ,
nm_customer varchar(30) NOT NULL,
is_active varchar(30),
vl_total INT(10) ,
  PRIMARY KEY (id_customer)
)"""
cursor.execute(sql)

# disconnect from server
db.close()

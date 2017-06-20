import MySQLdb
db = MySQLdb.connect(host="sql10.freemysqlhosting.net",port=3306, user='', passwd='', db="sql10181205")

cursor = db.cursor()

#Inserts values on the table
sql = """INSERT INTO tb_customer_account (id_customer ,cpf_cnpj  ,nm_customer, is_active,vl_total)
VALUES(1,123456789,'Juan jr','ativo',500)
"""
try:
   cursor.execute(sql)
   # Commit changes
   db.commit()
except:
   db.rollback() #case there is any error

# disconnect
db.close()

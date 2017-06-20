import MySQLdb
db = MySQLdb.connect(host="sql10.freemysqlhosting.net",port=3306, user='', passwd='', db="sql10181205")

cursor = db.cursor()

sql = """INSERT INTO tb_customer_account (id_customer ,cpf_cnpj  ,nm_customer, is_active,vl_total)
VALUES
 (1501,123456923,'Juan senior','ativo',800), (1600,693456789,'Lucas jr','inativo',400)
,(1780,697756789,'Lucas senior','ativo',1200), (1790,193455889,'mobi jr','inativo',2700)
,(1890,193455889,'mobi senior','ativo',2600), (1900,193455889,'wolfgam jr','inativo',2500)
,(2710,193455889,'wolfgam senior','ativo',2400)
"""
try:
   cursor.execute(sql)
   # Commit your changes 
   db.commit()
except:
   # in case there is any error
   db.rollback()

# disconnect 
db.close()

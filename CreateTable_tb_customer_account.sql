use acsm_a42e5ceb178f3dc; --My personal database for testing

/* Delete table if already exists */
DROP TABLE IF EXISTS tb_customer_account;

/*Create new table*/
CREATE TABLE tb_customer_account (
 id_customer tinyint(6) NOT NULL AUTO_INCREMENT,
cpf_cnpj INT(11) ,
nm_customer varchar(30) NOT NULL,
is_active varchar(30),
vl_total INT(10) ,
  PRIMARY KEY (id_customer)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

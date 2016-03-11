# from flask.ext.mysqldb import MySQL
import MySQLdb

# Create MySQL object. We create it here to avoid
# circular dependencies that would occur if we created in
# app.py
options = {
	"host": "localhost",
	"user": "root",
	"passwd": "root",
	"db" : "polititweetstorm"
}

# server
# options = {
#     "host": "localhost",
#     "user": "group57",
#     "passwd": "ozdunmi",
#     "db" : "group57pa1"
# }

mysql = MySQLdb.connect(**options)
mysql.autocommit(True)
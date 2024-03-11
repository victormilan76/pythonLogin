#cadena de conexion con mariadb
#herramientas a descargar (desde la terminasl de python ingresar el comando)
#ejecutar los siguientes comandos en python

#C:\Users\PC\AppData\Local\Programs\Python\Python312>python -m pip install --upgrade pip setuptools wheel
#C:\Users\PC\AppData\Local\Programs\Python\Python312>pip install mysql-connector-python
'''
import mysql.connector
from mysql.connector import Error
conection = mysql.connector.connect(user='root',password='',
                                    host = 'localhost',
                                    database = 'bd_nube',
                                    port = '3306')
print(conection)
'''


'''
class DAO():
    def _init_(self):
        try:
            self.conection = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user='root',
                password = '',
                db = 'bd_nube'
            )
        except Error as ex:
            print("Error al intentar la conexion: {0}".format(ex))
'''

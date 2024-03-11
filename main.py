

#def home():
 #  return render_template('home.html')    
'''
@app.route('/acceso-login', methods=["GET","POST"])
def login():
    if request.method == 'POST' and 'user' in request.form and 'password' in request.form:
'''

import mysql.connector
from mysql.connector import Error
conection = mysql.connector.connect(user='root',password='',
                                    host = 'localhost',
                                    database = 'bd_nube',
                                    port = '3306')



user = 'PEREZ'
password = '22988523'
cur = conection.cursor()
cur.execute('SELECT ID_USER,NAME,USER,PASSWORD,DATE_CREATION,ROL,STATUS FROM USER WHERE USER=%s AND PASSWORD=%s', (user,password))
data_user = cur.fetchone()
print("==========LOGIN==========")
if data_user:
   print(data_user)
   _user = data_user[1]
   print("welcome: "+_user)
else:
    print("USUARIO NO IDENTIFICADO")



'''
user = input('Ingrese su usuario = >')
password = input('Ingrese su password = >')
print("========>"+user+"-"+password)
'''
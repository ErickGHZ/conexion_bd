import mysql.connector  #  impotamos libreria para realizar la connexion con la base de datos

conexion = mysql.connector.connect(user="root", password="1234", host="localhost", database="compras", port="3306")  #  datos para poder conectarse con la base de datos
print(conexion)  #  confirma que la conexion fue exitosa

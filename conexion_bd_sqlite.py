import sqlite3  #  importa libreria

miConexion = sqlite3.connect("PruebaDB")  #   crea la base de datos

miCursor = miConexion.cursor()  #  realiza la conexion

miCursor.execute("""
    CREATE TABLE PRODUCTOS (
        SKU VARCHAR(30) PRIMARY KEY,
        NOMBRE VARCHAR(60),
        UNIDAD VARCHAR(20)
    )

""")  #  realiza una ejecucuion la cual es crear tabla
AñadirDatos = [
    ("1234", "Coca Cola 600ml", "Mililitos"),
    ("12345", "Galletas Emperador", "Gramos")
]  #  se realiza una introduccion de datos
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", AñadirDatos)  #  se realiza una ejecuccion la cual inserta datos ne la tabla ademas de llamar de donde se obtenbran los datos que se ingresaran
miConexion.commit()  #  guarda la ejecucion
miConexion.close()  #  cierra la base de datos

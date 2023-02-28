import sqlite3

miConexion = sqlite3.connect("PruebaDB")

miCursor = miConexion.cursor()

miCursor.execute(
     """CREATE TABLE PRODUCTOS (
        SKU VARCHAR(30) PRIMARY KEY,
        NOMBRE VARCHAR(60),
        UNIDAD VARCHAR(20)
    )
"""
)
AñadirDatos = [
    ("4568", "Jabon Zote", "Gramos"),
    ("7164", "Fabuloso", "Gramos")
]
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", AñadirDatos)

miConexion.commit()
miConexion.close()
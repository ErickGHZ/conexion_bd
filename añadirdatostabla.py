import sqlite3

miConexion = sqlite3.connect("PruebaDB")

miCursor = miConexion.cursor()

AñadirDatos = [
    ("4568", "Jabon Zote", "Gramos"),
    ("7164", "Fabuloso", "Gramos")
]
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", AñadirDatos)

miConexion.commit()
miConexion.close()
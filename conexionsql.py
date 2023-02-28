import sqlite3

miConexion = sqlite3.connect("Productos")

miCursor = miConexion.cursor()

miConexion.commit()
miConexion.close()
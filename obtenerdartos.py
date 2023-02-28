import sqlite3

miConexion = sqlite3.connect("PruebaDB")

miCursor = miConexion.cursor()


for row in miCursor.execute ("SELECT * FROM PRODUCTOS ORDER BY NOMBRE"):
    print(row)

miConexion.commit()
miConexion.close()


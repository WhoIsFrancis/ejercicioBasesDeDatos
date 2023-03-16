import sqlite3

conn = sqlite3.connect('baseDeDatos.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE Alumnos(id INT PRIMARY KEY, nombre TEXT, apellido TEXT)')

cursor.execute('INSERT INTO Alumnos VALUES(1, "Joan", "Mir")')
cursor.execute('INSERT INTO Alumnos VALUES(2, "Marc", "Marquez")')
cursor.execute('INSERT INTO Alumnos VALUES(3, "Max", "Verstappen")')
cursor.execute('INSERT INTO Alumnos VALUES(4, "Charles", "LeClerc")')
cursor.execute('INSERT INTO Alumnos VALUES(5, "Carlos", "Sainz")')
cursor.execute('INSERT INTO Alumnos VALUES(6, "Sergio", "Perez")')
cursor.execute('INSERT INTO Alumnos VALUES(7, "Fernando", "Alonso")')
cursor.execute('INSERT INTO Alumnos VALUES(8, "Lance", "Stroll")')
cursor.execute('INSERT INTO Alumnos VALUES(9, "Lando", "Norris")')
cursor.execute('INSERT INTO Alumnos VALUES(10, "Oscar", "Piastri")')

conn.commit()

nombre_buscado = input('Insertar nombre a buscar: ')

cursor.execute(f"SELECT * FROM Alumnos WHERE nombre= '{nombre_buscado}' ")

resultado = cursor.fetchall()

if len(resultado) > 0:
    print(f"Se encontraron {len(resultado)} resultados para el nombre '{nombre_buscado}':")
    for fila in resultado:
        print(fila)
else:
    print(f"No se encontraron resultados para el nombre '{nombre_buscado}'")

conn.close()
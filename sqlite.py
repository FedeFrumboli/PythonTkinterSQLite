import sqlite3

'''
conexion = sqlite3.connect("04-tkiner+sql-lite/base_de_datos.db")
cursor = conexion.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS productos(nombre varchar (50))")
conexion.commit()
conexion.close
'''

def agregarProducto(producto):
    conexion = sqlite3.connect("04-tkiner+sql-lite/base_de_datos.db")
    cursor = conexion.cursor()
    sql = "INSERT INTO productos VALUES ('%s')" %(producto.get())
    cursor.execute(sql)
    conexion.commit()
    conexion.close

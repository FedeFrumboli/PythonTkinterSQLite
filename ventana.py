from tkinter import *
from tkinter import ttk
import sqlite
import sqlite3
from functools import partial


def mostrarProductosEnTabla():
    conexion = sqlite3.connect("04-tkiner+sql-lite/base_de_datos.db")
    cursor = conexion.cursor()
    productos = cursor.execute("SELECT * FROM productos")
    conexion.commit()
    conexion.close
    for producto in productos:
        #print(producto[0])
        lista_productos.insert("", 0, text=producto[0])

#_____________________________________________________________________________________________

# Ventana
ventana = Tk()
ventana.geometry("300x300")
ventana.resizable(0,0)
ventana.title("Stock App")

# Variables de control
nombre_producto = StringVar()

#_____________________________________________________________________________________________

# Label nombre
label = Label(ventana, text="Nombre")
label.pack(pady=5)

# Campo nombre
campo_nombre_producto = Entry(ventana, textvariable=nombre_producto)
campo_nombre_producto.pack(pady=5)

# Boton de cargar producto
boton_carga = Button(ventana, text="Agregar producto", command=lambda:sqlite.agregarProducto(nombre_producto))
boton_carga.pack(pady=5)

# Imprimir lista productos en pantalla
boton_ver_todos_los_productos = Button(ventana, text="Mostrar todos los productos", command=mostrarProductosEnTabla)
boton_ver_todos_los_productos.pack(pady=5)

# Lista de productos
lista_productos = ttk.Treeview(height=6)
lista_productos.pack(pady=5)
lista_productos.heading("#0", text="Producto")

# Loop ventana
ventana.mainloop()

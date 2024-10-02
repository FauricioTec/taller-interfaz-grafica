import tkinter as tk
from tkinter import LEFT, RIGHT, BOTH, TOP
#pip install tk

root = tk.Tk() # Crea la ventana principal

root.title('Hola Mundo') # Titulo de la ventana

altoVentana = 500
anchoVentana = 800

xPosicion = root.winfo_screenwidth() // 2 - anchoVentana // 2
yPosicion = root.winfo_screenheight() // 2 - altoVentana // 2
yPosicion -= 20 # Correccion para la barra de tareas

root.geometry("%dx%d+%d+%d" % (anchoVentana, altoVentana, xPosicion, yPosicion))
#root.resizable(False, False) # Este *metodo* evita que la ventana se pueda redimensionar

colores = {
    'naranja_palido': '#fff8f0', 
    'negro': '#1e1e24', 
    'negro_azulado': '#14141b', 
    'azul_grisaceo_claro': '#0a0a96', 
    'blanco_azulado': '#dee4f7', 
    'azul_oscuro': '#0b1432', 
    'azul_grisaceo_claro': '#eef1fb', 
    'naranja_grisaceo': '#d7d0c8', 
    'naranja_claro': '#ffd099'
}

contenedorLateral = tk.Frame(root, bg=colores['negro'], width=anchoVentana / 3, height=altoVentana)
contenedorLateral.pack(side=LEFT, fill='y')

contenedorPrincipal = tk.Frame(root, bg=colores['naranja_palido'])
contenedorPrincipal.pack(side=RIGHT, fill=BOTH, expand=True)

# Notese que el root.mainloop() debe ser lo ultimo que se ejecute
root.mainloop() # Mantiene la ventana abierta
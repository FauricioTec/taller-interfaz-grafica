import tkinter as tk
from tkinter import LEFT, RIGHT, BOTH
#pip install tk

root = tk.Tk() # Crea la ventana principal

root.title('Hola Mundo') # Titulo de la ventana

altoVentana = 500
anchoVentana = 800

xPosicion = root.winfo_screenwidth() // 2 - anchoVentana // 2
yPosicion = root.winfo_screenheight() // 2 - altoVentana // 2
yPosicion -= 20 # Correccion para la barra de tareas

root.geometry("%dx%d+%d+%d" % (anchoVentana, altoVentana, xPosicion, yPosicion))
root.resizable(False, False) # Este *metodo* evita que la ventana se pueda redimensionar

# Se empieza a agregar widgets

contenedorLateral = tk.Frame(root, bg='blue', width=anchoVentana / 3, height=altoVentana)
contenedorLateral.pack(side=LEFT)

contenedorPrincipal = tk.Frame(root, bg='red')
contenedorPrincipal.pack(side=RIGHT, fill=BOTH, expand=True)

# Notese que el root.mainloop() debe ser lo ultimo que se ejecute
root.mainloop() # Mantiene la ventana abierta
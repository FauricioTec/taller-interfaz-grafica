import tkinter as tk
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

root.mainloop() # Mantiene la ventana abierta
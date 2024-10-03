import tkinter as tk
from tkinter.font import Font
from tkinter import LEFT, RIGHT, BOTH, Y, CENTER, W, E, N, S
from tkinter import ttk

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

root = tk.Tk() # Crea la ventana principal

root.title('Hola Mundo') # Titulo de la ventana

altoVentana = 600
anchoVentana = 900

xPosicion = root.winfo_screenwidth() // 2 - anchoVentana // 2
yPosicion = root.winfo_screenheight() // 2 - altoVentana // 2
yPosicion -= 40 # Correccion para la barra de tareas

root.geometry("%dx%d+%d+%d" % (anchoVentana, altoVentana, xPosicion, yPosicion))
root.resizable(False, False) # Este *metodo* evita que la ventana se pueda redimensionar

contenedorLateral = tk.Frame(root, bg=colores['negro'], width=anchoVentana / 3.5, height=altoVentana)
contenedorLateral.pack(side=LEFT, fill=Y)

contenedorPrincipal = tk.Frame(root, bg=colores['naranja_palido'])
contenedorPrincipal.pack(side=RIGHT, fill=BOTH, expand=True)

# Definimos la fuente
fuenteTituloLateral = Font(family="Segoe UI Semibold", size=16, slant="roman")

# Colocamos el primer Label
tituloBarraLateral = tk.Label(contenedorLateral, text='¡Consulta tu tabla de pagos!', bg=colores['negro'], fg='white', font=fuenteTituloLateral, wraplength=200)
tituloBarraLateral.place(anchor=CENTER, relx=.5, rely=.15)  #Se usa el anchor center y el relx para colocar el label en el medio

# Definimos las fuentes para los entrys
fuenteEntry = Font(family="Segoe UI", size=12)
fuenteLabelEntry = Font(family="Segoe UI", size=9, weight='bold')

# Label y Entry para Nombre
labelInputNombre = tk.Label(contenedorLateral, text="Nombre del cliente", bg=colores['negro'], fg='white', font=fuenteLabelEntry)
labelInputNombre.place(anchor=W, relx=.14, rely=.25) # Tener cuidado a la hora de usar posiciones relaticas y definir anchos y altos a la vez
inputNombre = tk.Entry(contenedorLateral, bg='white', fg='black', font=fuenteEntry, width=20, bd=2, relief="solid")
inputNombre.place(anchor='center', relx=.5, rely=.3)

# Label y Entry para Monto
labelInputMonto = tk.Label(contenedorLateral, text="Monto del prestamo", bg=colores['negro'], fg='white', font=fuenteLabelEntry)
labelInputMonto.place(anchor=W, relx=.14, rely=.35)
inputMonto = tk.Entry(contenedorLateral, bg='white', fg='black', font=fuenteEntry, width=20, bd=2, relief="solid")
inputMonto.place(anchor=CENTER, relx=.5, rely=.4)

# Label y Entry para Plazo
labelInputPlazo = tk.Label(contenedorLateral, text="Plazo en años", bg=colores['negro'], fg='white', font=fuenteLabelEntry)
labelInputPlazo.place(anchor=W, relx=0.14, rely=.45)
inputPlazo = tk.Entry(contenedorLateral, bg='white', fg='black', font=fuenteEntry, width=20, bd=2, relief="solid")
inputPlazo.place(anchor=CENTER, relx=.5, rely=.5)

# Label y Entry para Interés
labelInputInteres = tk.Label(contenedorLateral, text="Interés anual %", bg=colores['negro'], fg='white', font=fuenteLabelEntry)
labelInputInteres.place(anchor=W, relx=.14, rely=.55)
inputInteres = tk.Entry(contenedorLateral, bg='white', fg='black', font=fuenteEntry, width=20, bd=2, relief="solid")
inputInteres.place(anchor=CENTER, relx=.5, rely=.6)

# IMPORTANTE: Todo lo que se obtiene un de un tk.Entry se obtiene como un String

# Adicional: Hay un Widget llamado Text que probablemente les sera mas util para el proyecto

#Colocamos el primer combobox

# Label para el Combobox
labelTipoAmortizacion = tk.Label(contenedorLateral, text="Sistema de amortización", bg=colores['negro'], fg='white', font=fuenteLabelEntry)
labelTipoAmortizacion.place(anchor=CENTER, relx=.5, rely=.67)

fuenteCombobox = Font(family="Segoe UI", size=10)

# Combobox para seleccionar el tipo de amortización
tipoAmortizacionCombobox = ttk.Combobox(contenedorLateral, values=["Frances", "Americano"], font=fuenteCombobox, width=10)
tipoAmortizacionCombobox.state(["readonly"]) # Elimina la posibilidad de escribir sobre el combobox
tipoAmortizacionCombobox.place(anchor=CENTER, relx=.5, rely=.72)

#Colocamos un boton

# Definimos la fuente para el botón
fuenteBoton = Font(family="Segoe UI", size=11, weight='bold')

def imprimirInputs(): # Notese que la funcion que va a ejecutar el comando debe tener argumentos
    # Si ocupan ejecutar una funcion con argumentos "envuelvanla" dentro de una funcion sin argumentos
    print(inputNombre.get())
    print(inputMonto.get())
    print(inputInteres.get())
    print(inputPlazo.get())
    print(tipoAmortizacionCombobox.get())
    #Notese ademas que con el .get se obtiene el valor del Entry en formato string

# Botón para calcular con fuente bold y bordes redondeados
botonCalcular = tk.Button(contenedorLateral, text="Calcular", bg=colores['naranja_claro'], fg='black', font=fuenteBoton, width=13, height=2, relief="solid", bd=2, command=imprimirInputs)
botonCalcular.place(anchor=CENTER, relx=.5, rely=.85)

# Notese que el root.mainloop() debe ser lo ultimo que se ejecute
root.mainloop() # Mantiene la ventana abierta
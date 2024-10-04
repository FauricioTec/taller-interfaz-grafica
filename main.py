import tkinter as tk
from tkinter.font import Font
from tkinter import LEFT, RIGHT, BOTH, Y, CENTER, W, E, N, S
from tkinter import ttk

colores = {
    'naranja_palido': '#fff8f0', 
    'negro': '#1e1e24', 
    'negro_azulado': '#14141b', 
    'azul': '#0a0a96', 
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

# Botón para calcular con fuente bold y bordes redondeados
botonCalcular = tk.Button(contenedorLateral, text="Calcular", bg=colores['naranja_claro'], fg='black', font=fuenteBoton, width=13, height=2, relief="solid", bd=2)
botonCalcular.place(anchor=CENTER, relx=.5, rely=.85)

# Se continua con el panel principal o el frame principal, para ejemplifiar como funciona ahora usaremos el metodo grid

# Definimos la fuente para los labels del panel principal
fuenteLabelPrincipal = Font(family="Segoe UI", size=12, weight='bold')

# Label con los datos de la consulta
labelDatosConsulta = tk.Label(contenedorPrincipal, text="Datos de la consulta", bg=colores['naranja_palido'], fg=colores['negro'], font=fuenteLabelPrincipal)
labelDatosConsulta.grid(row=0, column=0, padx=20, pady=(20, 10), sticky=W) # Se coloca como en una tabla o matriz
# el parametro Sticky W significa que se alineara el Widget a la izquierda de la celda

# Canvas para la línea horizontal
canvasLinea = tk.Canvas(contenedorPrincipal, width=600, height=2, bg=colores['naranja_palido'], highlightthickness=0)
canvasLinea.grid(row=1, column=0, padx=20, pady=5, sticky=W)
canvasLinea.create_line(0, 1, 600, 1, fill=colores['negro'])

# Cambio con respecto a la imagen de referencia, haremos uso del widget Text, para que lo implementen tambien en sus proyectos

# Widget Text para mostrar resultados
textResultados = tk.Text(contenedorPrincipal, bg='white', fg='black', font=fuenteEntry, width=50, height=10, wrap='word', bd=2, relief="solid")
textResultados.grid(row=2, column=0, padx=20, pady=(10, 5), sticky=N)

# Label con los resultados de la consulta
labelResultados = tk.Label(contenedorPrincipal, text="Resultados de la consulta", bg=colores['naranja_palido'], fg=colores['negro'], font=fuenteLabelPrincipal)
labelResultados.grid(row=3, column=0, padx=20, pady=(10, 5), sticky=W)

# Canvas para la línea horizontal debajo del labelResultados
canvasLineaResultados = tk.Canvas(contenedorPrincipal, width=600, height=2, bg=colores['naranja_palido'], highlightthickness=0)
canvasLineaResultados.grid(row=4, column=0, padx=20, pady=5, sticky=W)
canvasLineaResultados.create_line(0, 1, 600, 1, fill=colores['negro'])

# Ahora colocaremos el TreeView o la tabla
# Cambiamos el tema a 'clam'
style = ttk.Style()
style.theme_use('clam')

# Configuramos el estilo del Treeview
style.configure('Treeview.Heading', background=colores['azul_oscuro'], foreground='white', relief='flat')  # Añadimos foreground para el texto
style.map('Treeview.Heading', background=[('selected', colores['azul_oscuro'])], foreground=[('selected', 'white')])
style.configure('Treeview', background=colores['azul_grisaceo_claro'], fieldbackground=colores['azul_grisaceo_claro'], foreground='black')

# Creamos la tabla
tabla = ttk.Treeview(contenedorPrincipal, selectmode='browse', height=9)

tabla['columns'] = ('periodo', 'saldo_inicial', 'cuota', 'interes', 'amortizacion', 'saldo_final')

# Configuramos los encabezados de las columnas
tabla.heading('#0', text='', anchor=CENTER)
tabla.heading('periodo', text='Periodo', anchor=CENTER)
tabla.heading('saldo_inicial', text='Saldo Inicial', anchor=CENTER)
tabla.heading('cuota', text='Cuota', anchor=CENTER)
tabla.heading('interes', text='Interés', anchor=CENTER)
tabla.heading('amortizacion', text='Amortización', anchor=CENTER)
tabla.heading('saldo_final', text='Saldo Final', anchor=CENTER)

# Configuramos el ancho de las columnas
tabla.column('#0', width=0, stretch=tk.NO)  # Esto hará que no se muestre la columna por defecto
tabla.column('periodo', anchor=CENTER, width=80)
tabla.column('saldo_inicial', anchor=CENTER, width=100)
tabla.column('cuota', anchor=CENTER, width=80)
tabla.column('interes', anchor=CENTER, width=80)
tabla.column('amortizacion', anchor=CENTER, width=100)
tabla.column('saldo_final', anchor=CENTER, width=100)

# Insertamos datos de ejemplo
datos_ejemplo = [
    ('1', '1000', '150', '50', '100', '900'),
    ('2', '900', '150', '45', '105', '795'),
    ('3', '795', '150', '40', '110', '685'),
    ('4', '685', '150', '35', '115', '570'),
]

# Alternar colores de fondo para las filas
for i, dato in enumerate(datos_ejemplo):
    tag = 'par' if i % 2 == 0 else 'impar'
    tabla.insert('', 'end', values=dato, tags=(tag,))

tabla.tag_configure('par', background=colores['blanco_azulado'])
tabla.tag_configure('impar', background=colores['azul_grisaceo_claro'])

# Empaquetamos la tabla
tabla.grid(row=5, column=0, padx=20, pady=(10, 20), sticky=N)

# Notese que el root.mainloop() debe ser lo ultimo que se ejecute
root.mainloop() # Mantiene la ventana abierta
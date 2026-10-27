import tkinter as tk
from tkinter import messagebox

# Ocultar la ventana principal de tkinter
root = tk.Tk()
root.withdraw()

# Secuencia de alertas divertidas para Jhimmi
messagebox.showwarning(
    "Alerta del Sistema", 
    "¡Atención!\nIniciando escaneo profundo en la PC de Jhimmi..."
)

messagebox.showerror(
    "Error Crítico", 
    "Se ha detectado un nivel peligrosamente alto de genialidad en este equipo."
)

messagebox.showinfo(
    "Solución Encontrada", 
    "Para solucionar este error, el sistema exige que Jhimmi invite unos tacos o un café hoy mismo."
)

# Ventana interactiva final
respuesta = messagebox.askyesno(
    "Pregunta importante", 
    "¿Estás de acuerdo con los términos y condiciones, Jhimmi?"
)

if respuesta:
    messagebox.showinfo(
        "¡Excelente!", 
        "¡Trato hecho! Jhimmi ha aceptado oficialmente pagar la comida."
    )
else:
    messagebox.showinfo(
        "Rechazado", 
        "Error: Opción no válida. De igual forma Jhimmi debe los tacos."
    )
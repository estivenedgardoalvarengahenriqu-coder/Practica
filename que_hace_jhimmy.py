import random
import tkinter as tk


def mover_ventana(event):
  # Genera coordenadas aleatorias dentro de la pantalla
  ancho_pantalla = ventana.winfo_screenwidth()
  alto_pantalla = ventana.winfo_screenheight()

  nuevo_x = random.randint(100, ancho_pantalla - 300)
  nuevo_y = random.randint(100, alto_pantalla - 200)

  # Mueve la ventana a la nueva posición
  ventana.geometry(f"300x150+{nuevo_x}+{nuevo_y}")


# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("¡Atención Jhimmi!")
ventana.geometry("300x150+500+300")

# Etiqueta con mensaje gracioso
etiqueta = tk.Label(
    ventana,
    text=(
        "Jhimmi, haz clic aquí\nsi te atreves\n(o invita los tacos para"
        " parar):"
    ),
    font=("Arial", 11),
    pady=20,
)
etiqueta.pack()

# Detecta cuando el mouse pasa por encima de la ventana y la hace saltar
ventana.bind("<Enter>", mover_ventana)

ventana.mainloop()
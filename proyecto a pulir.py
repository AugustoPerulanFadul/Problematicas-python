import tkinter as tk


def reiniciar():
    entrada_text.delete(1.0, tk.END)


def mostrar_contenido():
    contenido = entrada_text.get(1.0, tk.END)
    print("Lo escrito:")
    print(contenido)


def abrir_ventana_nueva():
    ventana_nueva = tk.Toplevel(ventana)
    ventana_nueva.title("Contenido en tiempo real")

    contenido_text = tk.Text(ventana_nueva, height=10, width=30)
    contenido_text.pack(pady=10)

    def actualizar_contenido():
        contenido = entrada_text.get(1.0, tk.END)
        contenido_text.delete(1.0, tk.END)
        contenido_text.insert(tk.END, contenido)
        ventana_nueva.after(100, actualizar_contenido)  # Actualizar cada 100 ms

    actualizar_contenido()


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Programa de entrada")

# Establecer el color de fondo
ventana.configure(bg="light blue")

# Crear el campo de entrada
entrada_text = tk.Text(ventana, height=10, width=30)
entrada_text.pack(pady=10)

# Crear el botón "Mostrar Contenido"
boton_mostrar_contenido = tk.Button(ventana, text="Guardar Contenido", command=mostrar_contenido)
boton_mostrar_contenido.pack(pady=5)

# Crear el botón "Reiniciar"
boton_reiniciar = tk.Button(ventana, text="Reiniciar", command=reiniciar)
boton_reiniciar.pack(pady=5)

# Crear el botón "Abrir ventana nueva"
boton_abrir_ventana = tk.Button(ventana, text="Mostrar ubicaciónes", command=abrir_ventana_nueva)
boton_abrir_ventana.pack(pady=5)

# Ejecutar la ventana principal
ventana.mainloop()

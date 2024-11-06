import tkinter as tk 

ventana = tk.Tk()
ventana.title ("Mi primer interfaz grafica")
etiqueta = tk.Label(ventana, text= "Hola putos")
etiqueta.pack(pady=5)

ventana.mainloop()
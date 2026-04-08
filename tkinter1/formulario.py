import tkinter as Ventana

class Interfaz:
    def __init__(self, color, titulo):
        self.color = color
        self.titulo = titulo
        
    def crear_formulario(self):
        formulario = Ventana.Tk()
        formulario.title(self.titulo)
        formulario.config(bg=self.color)
        
        # 1. MENU
        barra_menu = Ventana.Menu(formulario)
        menu_opciones = Ventana.Menu(barra_menu, tearoff=0)
        menu_opciones.add_command(label="Archivo", command=self.accion_vacia)
        menu_opciones.add_separator()
        menu_opciones.add_command(label="Salir", command=formulario.quit)
        barra_menu.add_cascade(label="Opciones", menu=menu_opciones)
        formulario.config(menu=barra_menu)
        return formulario
    
    def crear_preguntas(self, formulario, pregunta1, pregunta2):
        # 2. FRAME (Contenedor para organizar todo)
        marco = Ventana.Frame(formulario, padx=10, pady=10)
        marco.pack()

        # 3. LABEL y 4. ENTRY (Pregunta 1)
        Ventana.Label(marco, text=pregunta1).pack()
        Ventana.Entry(marco).pack()
        
        # 3. LABEL y 4. ENTRY (Pregunta 2)
        Ventana.Label(marco, text=pregunta2).pack()
        Ventana.Entry(marco).pack()
        
        # 5. BUTTON
        Ventana.Button(marco, text="Registrar", command=self.accion_vacia).pack()
        
        # 6. CHECKBUTTON
        Ventana.Checkbutton(marco, text="Eres tú?").pack()
        
        # 7. RADIOBUTTON
        Ventana.Radiobutton(marco, text="Hombre", value=1).pack()
        Ventana.Radiobutton(marco, text="Mujer", value=2).pack()
        Ventana.Radiobutton(marco, text="Binario", value=3).pack()
        
        # 8. MESSAGE (Texto multilínea)
        Ventana.Message(marco, text="Este widget Message se usa para textos largos", width=150).pack()

        # 9. MENUBUTTON (Botón que despliega menú)
        mb = Ventana.Menubutton(marco, text="Click para opciones", relief="raised")
        mb.menu = Ventana.Menu(mb, tearoff=0)
        mb["menu"] = mb.menu
        mb.menu.add_command(label="Opción 1")
        mb.menu.add_command(label="Opción 2")
        mb.pack()

        # 10. LISTBOX
        lista = Ventana.Listbox(marco, height=3)
        lista.insert(1, "Elemento 1")
        lista.insert(2, "Elemento 2")
        lista.pack()

        # 11. CANVAS (Para dibujos o gráficos)
        canvas = Ventana.Canvas(formulario, width=100, height=40, bg="white")
        canvas.create_oval(10, 10, 90, 30, fill="orange") # Dibujamos un óvalo
        canvas.pack()

    def accion_vacia(self):
        print("Botón presionado")
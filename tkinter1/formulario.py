import tkinter as Ventana

class Interfaz:
    def __init__(self,color,titulo):
        self.color = color
        self.titulo = titulo
        
    def crear_formulario(self):
        #Sacar elementos de tkinter
        formulario = Ventana.Tk()
        formulario.title(self.titulo)
        #metodo config para modificar objetos ya creados
        formulario.config(bg = self.color, height=500, width=500)
        #todo lo que haga formulario debe retornar
        return formulario
    
    def crear_preguntas(self,formulario, pregunta1, pregunta2):
        label_p1 = Ventana.Label(formulario, text=pregunta1)
        label_p1.pack()
        entry_r1 = Ventana.Entry(formulario)
        entry_r1.pack()
        label_p2 = Ventana.Label(formulario, text=pregunta2)
        label_p2.pack()
        entry_r2= Ventana.Entry(formulario)
        entry_r2.pack()
        boton_enviar = Ventana.Button(formulario,text="Registrar", command="activa_evento -click")#En el command no tener parentesis
        boton_enviar.pack()
        boton_borrar = Ventana.Button(formulario, text="Borrar Campos", command="evento_click")
        boton_borrar.pack()
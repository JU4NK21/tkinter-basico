from formulario import Interfaz

#*** Codigo Principal***
#se consulto en una API los atributos de la interfaz

dato_color = input("Escriba el color: ")
dato_titulo = input("Escriba el nombre de la interfaz: ")
pregunta1 = input("Escriba la pregunta P1: ")
pregunta2 = input("Escriba la pregunta P2: ")

obj_formulario = Interfaz(dato_color, dato_titulo)#Ventana total
formulario_usuario = obj_formulario.crear_formulario()#Elementos retornados en la ventana

obj_formulario.crear_preguntas(formulario_usuario, pregunta1, pregunta2)
#mainloop siempre al final del codigo
formulario_usuario.mainloop()
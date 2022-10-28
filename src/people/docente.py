from people.persona import Persona

# Clase Docente que herda atributos de persona
# El docente es una persona, tiene id y nombre
# Permite simplificar la lectura y reducir lineas de codigo
class Docente(Persona):
    def __init__(self, id, nombre, asignatura, estudiante):
        super.__init__(id, nombre)
        self.asignatura = asignatura
        self.estudiante = estudiante

# Imprime o muestra los datos del docente
    def mostrar_docente(self):
        print("id Docente: " + self.idPerson)
        print("Nombre Docente: " + self.nombrePerson)
        print("Asignatura Docente: " + self.asignatura)

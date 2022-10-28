from people.persona import Persona

# Clase Estudiante que herda atributos de persona
# El estudiante es una persona, tiene id y nombre
# Permite simplificar la lectura y reducir lineas de codigo
class Estudiante(Persona):
    def __init__(self, id, nombre, curso, nota):
        super.__init__(id, nombre)
        self.curso = curso
        self.nota = nota

# Imprime o muestra los datos del estudiante
    def mostrar_estudiante(self):
        print("ID Estudiante: " + self.idPerson)
        print("Nombre Estudiante: " + self.nombrePerson)
        print("Curso Estudiante: " + self.curso)
        print("Nota Estudiante: " + self.nota)

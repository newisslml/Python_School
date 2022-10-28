from people.persona import Persona


class Estudiante(Persona):
    def __init__(self, curso, nota):
        self.curso = curso
        self.nota = nota

    def mostrarEstudiante(self):
        print("ID Estudiante: " + self.idPerson)
        print("Nombre Estudiante: " + self.nombrePerson)
        print("Curso Estudiante: " + self.curso)
        print("Nota Estudiante: " + self.nota)

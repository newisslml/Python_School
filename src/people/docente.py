from people.persona import Persona


class Docente(Persona):
    def __init__(self, id, nombre, asignatura, estudiante):
        super.__init__(id, nombre)
        self.asignatura = asignatura
        self.estudiante = estudiante

    def mostrarDocente(self):
        print("id Docente: " + self.idPerson)
        print("Nombre Docente: " + self.nombrePerson)
        print("Asignatura Docente: " + self.asignatura)

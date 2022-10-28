class Docente():
    def __init__(self,idDoc,nombreDoc,asignatura,estudiante):
        self.idDoc = idDoc
        self.nombreDoc = nombreDoc
        self.asignatura = asignatura
        self.estudiante = estudiante
    def mostrarDocente(self):
        return "\nId             : "+str(self.idDoc)+\
               "\nNombre Docente : "+self.nombreDoc+\
               "\nAsignatura     : "+self.asignatura+\
               "\nEstudiante     : "+self.estudiante.mostrarEstudiante()          
    
      


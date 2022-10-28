class Estudiante():
    def __init__(self,idEst,nombreEst,curso,nota):
        self.idEst = idEst
        self.nombreEst =  nombreEst
        self.curso = curso
        self.nota = nota
    def mostrarEstudiante(self):
        return "\nId      : "+str(self.idEst)+\
               "\nNombre   : "+str(self.nombreEst)+\
               "\nCurso   : "+str(self.curso)+\
               "\nNota    : "+str(self.nota.mostrarNota())    


class Nota():
    def __init__(self,id,calificacion,fecha):
        self.id = id
        self.calificacion = calificacion
        self.fecha = fecha
    def mostrarNota(self):
        return  "\nId           : "+str(self.id)+\
                "\nCalificacion : "+str(self.calificacion)+\
                "\nFecha        : "+str(self.fecha.mostrarFecha())



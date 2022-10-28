# Clase padre que posee propiedades unicas y heredables
# Permite simplificar la lectura y reducir lineas de codigo
# La base de la POO (programacion orientada a objetos)
class Persona():
    def __init__(self, idPerson, nombrePerson):
        self.idPerson = idPerson
        self.nombrePerson = nombrePerson

# Muestra los datos de la persona que puede ser usado por sus hijos
# Hijos dicese a las clases que comparten estos mismos atributos
    def mostrar_persona(self):
        print("ID Persona: " + self.idPerson)
        print("Nombre Persona: " + self.idPerson)

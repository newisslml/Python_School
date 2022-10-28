

from people.docente import Docente


def spaces_menus():
    print("\n")
    print("·····································")


def not_option():
    print("No existe esa opcion, intente nuevamente...")


def agregar_docente():
    idDoc = int(input("Ingrese ID del Docente: "))
    nombreDoc = str(input("Ingrese Nombre Docente: "))
    asignatura = str(input("Asignatura que realiza: "))
    estudiante = None
    d = Docente(idDoc, nombreDoc, asignatura, estudiante)
    #listaDocentes.append(d)
    print("\nDocente agregado correctamente")

#def listar_docente():
    #for obj in listaDocentes:
    #    obj.nombrePersona    

def menu_docente():
    spaces_menus()
    print("1. Agregar Docente")
    print("2. Listar Docente")
    print("3. Salir")
    option = int(input("Ingrese su Opcion de (1-): "))
    
    while True:
        match option:
            case 1:
                agregar_docente()
            #case 2:
                #listar_docente()
            case 3: 
                return 
            case _:
                not_option()
                return 

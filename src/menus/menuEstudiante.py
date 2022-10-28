
from people.estudiante import Estudiante


def spaces_menus():
    print("\n")
    print("·····································")


def not_option():
    print("No existe esa opcion, intente nuevamente...")


def agregar_estudiante():
    idEst = int(input("Ingrese ID Estudiante: "))
    nombreEst = str(input("Ingrese Nombre: "))
    curso = str(input("Ingrese Curso: "))
    nota = None
    e = Estudiante(idEst, nombreEst, curso, nota)
    # listaDocentes.append(e)
    print("\nEstudiante agregado Correctamente")


def menu_estudiante():
    spaces_menus()
    print("1. Agregar Estudiante")
    print("2. Listar Estudiante")
    print("3. Salir")
    option = int(input("Ingrese su Opcion de (1-): "))
    while True:
        match option:
            case 1:
                agregar_estudiante()
            case _:
                not_option()

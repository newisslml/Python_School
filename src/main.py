

from people.docente import Docente
from people.estudiante import Estudiante
from utils.nota import Nota
from utils.fecha import Fecha
from menus.menuDocente import menu_docente
from menus.menuEstudiante import menu_estudiante

listaDocentes = []


def spaces_menus():
    print("\n")
    print("·····································")


def not_option():
    print("No existe esa opcion, intente nuevamente...")


def menu_principal():
    spaces_menus()
    print("1. Menu Docente")
    print("2. Menu Estudiante")
    print("3. Salir")
    option = int(input("Ingrese su Opcion de (1-5): "))
    return option


while True:
    option = menu_principal()
    match option:
        case 1:
            menu_docente()
        case 2:
            menu_estudiante()
        case 3:
            break
        case _:
            not_option()

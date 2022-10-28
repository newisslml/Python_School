

from people.docente import Docente
from people.estudiante import Estudiante
from utils.nota import Nota
from utils.fecha import Fecha
from menus.menudocente import menu_docente
from menus.menuestudiante import menu_estudiante

listaDocentes = []

# Funcion para reutilizar y no repetir codigo
def spaces_menus():
    print("\n")
    print("·····································")

# Funcion para reutilizar y no repetir codigo
def not_option():
    print("No existe esa opcion, intente nuevamente...")

# Menu principal que deriva a otros sub menus
# Sirve para desaclopar el codigo y se vea mas ordenado
def menu_principal():
    spaces_menus()
    print("1. Menu Docente")
    print("2. Menu Estudiante")
    print("3. Salir")
    option = int(input("Ingrese su Opcion de (1-5): "))
    return option

# Loop infinito hasta que el usuario decida Salir = break
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

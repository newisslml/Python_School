from asyncio.windows_events import NULL
from contextlib import nullcontext
from docente import Docente
from estudiante import Estudiante
from nota import Nota
from fecha import Fecha
lista = []
while True:
    print("\n1. Agregar Docente")
    print("2. Agregar Estudiante")
    print("3. Modificar Nota")
    print("4. Eliminar Nota")
    print("5. Mostrar Promedio Estudiante")
    opcion = int(input("Ingrese su Opcion de (1-5):  "))
    if opcion==1: 
        idDoc = int(input("Ingrese ID del Docente: ")) 
        nombreDoc = str(input("Ingrese Nombre Docente: "))
        asignatura = str(input("Asignatura que realiza: "))
        estudiante = None
        d= Docente(idDoc,nombreDoc,asignatura,estudiante)
        lista.append(d)
        print("\nDocente agregado correctamente")
    elif opcion ==2:
        idEst = int(input("Ingrese ID Estudiante: "))
        nombreEst = str(input("Ingrese Nombre: "))
        curso = str(input("Ingrese Curso: "))
        nota = None
        e = Estudiante(idEst,nombreEst,curso,nota)
        lista.append(e)
        print("\nEstudiante agregado Correctamente")
        break

f = Fecha(25,10,2022)
print(f.mostrarFecha)
n = Nota(111,6.0,f)
print(n.mostrarNota())
e = Estudiante(101,"El gargola Vera","IN1",n)
print(e.mostrarEstudiante())
d = Docente(11,"Jego","POO",e)
print(d.mostrarDocente())

lista.append(d)




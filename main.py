from claseAlumnos import *
from claseMaterias import *
from ManejadorAlumnos import *
from ManejadorMaterias import *
import os

def Menu():
    print("0).Salir")
    print("1).Informar promedio con y sin aplazos de un alumno")
    print("2).Informar estudiantes promocionales aprobados por materia")
    print("3).Listar alumnos alfabeticamente por años")

if __name__ == '__main__':
    lista_alum = ManejaAl(0)
    lista_mat = ManejaMateria()
    lista_alum.carga_alumnos()
    lista_mat.carga_materias()
    while True:
        os.system('cls')
        Menu()
        menu = {
            "1": 'lista_mat.MuestraProm_alumno()',
            "2": 'lista_mat.MuestraAp(lista_alum)',
            "3": 'lista_alum.Ordena()',
            "4": 'print("Gracias por usar el sistema")'
        }
        opc = input("Ingrese la opción elegida: \n")
        os.system('cls')
        if opc in menu:
            if opc == '4':
                eval(menu[opc])
                break
            else:
                eval(menu[opc])
            aux = input("\nIngrese cualquier botón para continuar\n")
        else:
            print("Ha ingresado una opción incorrecta, por favor, ingrese una opción nuevamente")
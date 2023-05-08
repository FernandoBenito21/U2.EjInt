from claseMaterias import *
import csv

class ManejaMateria:
    def __init__(self):
        self.__Materias= []

    def carga_materias(self):
        archivo = open("materiasAprobadas.csv")
        lector= csv.reader(archivo, delimiter=';')
        i = 0
        for elemento in lector:
            if i != 0:
                alumnoaux= Materia(elemento[0], elemento[1].upper(), elemento[2], int(elemento[3]), elemento[4])
                self.__Materias.append(alumnoaux)
            i += 1

    def MuestraProm(self):
        dni = input("Ingrese el dni del alumno ")
        lista_indices = []
        i = 0
        for fila in self.__Materias:
            if fila.get_dni() == dni:
                lista_indices.append(i)
            i += 1
        if len(lista_indices) == 0:
            print("No se encontró el Alumno buscado")
        else:
            prom = [0, 0]
            for cant in range(len(lista_indices)):
                prom[0] += self.__Materias[lista_indices[cant]].get_nota()
                if self.__Materias[lista_indices[cant]].get_cond() == 'E':
                    if self.__Materias[lista_indices[cant]].get_nota() >= 4:
                        prom[1] += self.__Materias[lista_indices[cant]].get_nota()
                if self.__Materias[lista_indices[cant]].get_cond() == 'P':
                    if self.__Materias[lista_indices[cant]].get_nota() >= 7:
                        prom[1] += self.__Materias[lista_indices[cant]].get_nota()
                if self.__Materias[lista_indices[cant]].get_cond() == 'X':
                    if self.__Materias[lista_indices[cant]].get_nota() >= 6:
                        prom[1] += self.__Materias[lista_indices[cant]].get_nota()
            print("El promedio del alumno con aplazos es " + str(prom[0] / len(lista_indices)))
            print("El promedio del alumno sin aplazos es " + str(prom[1] / len(lista_indices)))

    def MuestraAp(self, alumnos):
        materia = input("Ingrese la materia a buscar: ")
        print("DNI            Apellido y Nombre           Fecha           Nota        Año que cursa")
        for fila in self.__Materias:
            if materia.upper() == fila.get_nombre():
                if fila.get_cond() == 'P':
                    if fila.get_nota() >= 7:
                        p = alumnos.Buscar(fila.get_dni())
                        print("{}      {}           {}".format(fila.get_fecha(), str(fila.get_nota()), p))


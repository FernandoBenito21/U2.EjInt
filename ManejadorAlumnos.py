from claseAlumnos import *
import numpy as np
import csv

class ManejaAl:
    __cantidad = 0
    __dimension = 0
    __incremento = 5
    def __init__(self, dimension, incremento=8):
        self.__Alumnos= np.empty(dimension, dtype=Alumno)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento

    def carga_alumnos(self):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__Alumnos.resize(self.__dimension)
        archivo= open("Alumnos_EjInt.csv")
        lector= csv.reader(archivo, delimiter=';')
        i = 0
        for elemento in lector:
            if i != 0:
                alumnoaux = Alumno(elemento[0], elemento[1], elemento[2], elemento[3], elemento[4])
                self.__Alumnos[self.__cantidad] = alumnoaux
                self.__cantidad += 1
            i += 1

    def Buscar(self, dni):
        i = 0
        while ((i < self.__cantidad) and (dni != self.__Alumnos[i].get_dni())):
            i += 1
        if i != self.__cantidad:
            print("{}{}".format(self.__Alumnos[i].get_dni(), self.__Alumnos[i].get_NyA().ljust(17)), end="           ")
        return self.__Alumnos[i].get_año()

    def Ordenar(self):
        alumnos_ordenados = sorted(self.__Alumnos)
        for alumno in alumnos_ordenados:
            alumno.mostrar_datos()


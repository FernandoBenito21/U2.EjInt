class Alumno:
    def __init__(self, dni, apellido, nombre, carrera, año_carrera):
        self.__dni=dni
        self.__ap=apellido
        self.__nom=nombre
        self.__carrera=carrera
        self.__año_carrera=año_carrera

    def get_dni(self):
        return self.__dni

    def get_NyA(self):
        return self.__ap + " " + self.__nom

    def get_año(self):
        return self.__año_carrera

    def __lt__(self, otro):
        return (self.__año_carrera, (self.__ap + self.__nom)) < (otro.get_anio(), (otro.get_nomap()))

    def mostrar_datos(self):
        print("{}, {} {}, {}, {}".format(self.__dni, self.__ap, self.__nom, self.__carrera, self.__año_carrera))




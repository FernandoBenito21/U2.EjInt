class Materia:
    def __init__(self, dni, nombre, fecha, nota, aprobacion):
        self.__dni=dni
        self.__nombre=nombre
        self.__fecha=fecha
        self.__nota=nota
        self.__aprobacion=aprobacion

    def get_dni(self):
        return self.__dni

    def get_nota(self):
        return self.__nota

    def get_cond(self):
        return self.__aprobacion

    def get_nomate(self):
        return self.__nombre
    def get_fecha(self):
        return self.__fecha

    def mostrar(self):
        print(self.__dni)
        print(self.__nombre)
        print(self.__fecha)
        print(self.__nota)
        print(self.__aprobacion)
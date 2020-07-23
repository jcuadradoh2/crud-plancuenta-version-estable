class PlanCuenta:
    def __init__(self, id=0, cod="", grupo=0, descr="", nat="", est=True):
        self.__id=id
        self.__codigo=cod
        self.__grupo=grupo
        self.__descripcion=descr
        self.__naturaleza=nat
        self.__estado=est

    #Metodo id
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id=id    
    #Metodo codigo
    @property
    def codigo(self):
        return self.__codigo
    @id.setter
    def id(self, codigo):
        self.__codigo=codigo

    #Metodo grupo
    @property
    def grupo(self):
        return self.__grupo
    @id.setter
    def id(self, grupo):
        self.__grupo=grupo

    #Metodo descripcion
    @property
    def descripcion(self):
        return self.__descripcion
    @id.setter
    def id(self, descripcion):
        self.__descripcion=descripcion

    #Metodo naturaleza
    @property
    def naturaleza(self):
        return self.__naturaleza
    @id.setter
    def id(self, naturaleza):
        self.__naturaleza=naturaleza

    #Metodo estado
    @property
    def estado(self):
        return self.__estado
    @id.setter
    def id(self, estado):
        self.__estado=estado
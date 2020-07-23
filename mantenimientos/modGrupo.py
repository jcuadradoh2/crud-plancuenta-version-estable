class modGrupo:
    def __init__(self,id=0,des=''):
        self.__id = id
        self .__des = des

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,id):
        self.__id= id 

    @property
    def des(self):
        return self.__des
    @des.setter
    def des(self,des):
        self.__des= des
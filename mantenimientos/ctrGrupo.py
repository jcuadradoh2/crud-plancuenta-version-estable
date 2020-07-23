from modGrupo import modGrupo
from daoGrupo import daoGrupo

class controlador:
    def __init__(self, gr=None):
        self.__gr=gr
    
    def consultar(self, busca):
        objdao=daoGrupo()
        return objdao.consultar(busca)

    def insertar(self, gr):
        objdao=daoGrupo()
        return objdao.insertar(gr)

    def eliminar(self, gr):
        objdao=daoGrupo()
        return objdao.eliminar(gr)

    def modificar(self, gr):
        objdao=daoGrupo()
        return objdao.modificar(gr)
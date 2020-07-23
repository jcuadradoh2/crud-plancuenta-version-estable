from dao_plancuenta import DaoPlanCuenta
from mod_plancuenta import PlanCuenta

class ctrPlanCuenta:
    def __init__(self, pc=None):
        self.pc = pc
        
    def consulta(self, buscar):
        objDao = DaoPlanCuenta()
        return objDao.consulta(buscar)

    def insertar(self, pc):
        objDao = DaoPlanCuenta()
        return objDao.insertar(pc)

    def modificar(self, pc):
        objDao = DaoPlanCuenta()
        return objDao.modificar(pc)

    def eliminar(self, pc):
        objDao = DaoPlanCuenta()
        return objDao.eliminar(pc)

    def valId(self, pc):
        objDao = DaoPlanCuenta()
        return objDao.valId(pc)

    def returnDato(self, pc):
        objDao = DaoPlanCuenta()
        return objDao.returnDato(pc)

    def create_view(self):
        objDao = DaoPlanCuenta()
        return objDao.create_view()
import sys
import pymysql
from conexion import conexion
import os

class daoGrupo(conexion):
    def __init__(self):
        super().__init__()
    
    def consultar(self,busca):
        result = False
        try:
            sql="select id, descripcion from grupo where descripcion like '%" +str(busca)+ "%' order by id"
            self.conectabd()
            self.conector.execute(sql)
            result=self.conector.fetchall()
        except Exception as e:
            print('error en la consulta: {}'.format(e))
        finally:
            self.close()
            return result

    def insertar(self,gr):
        correcto=True
        try:
            id=self.id()
            sql="insert into grupo values(%s,%s)"
            self.conectabd()
            self.conector.execute(sql,(id, gr.des))
            self.conn.commit()
        except Exception as e:
            correcto = False
            self.conn.rollback()
            print('error en la insercion: {}'.format(e))
        finally:
            self.close()
            return correcto

    def eliminar(self,gr):
        correcto = True
        try:
            sql="delete from grupo where id = %s"
            self.conectabd()
            self.conector.execute(sql,(gr.id))
            self.conn.commit()
        except Exception as e:
            print('Error en la eliminacion:  {}', e)
            correcto = False
        finally:
            self.close()
            return correcto

    def modificar(self,gr):
        correcto = True
        try:
            sql="UPDATE grupo set descripcion = %s WHERE id = %s"
            self.conectabd()
            self.conector.execute(sql,(gr.des, gr.id))
            self.conn.commit()
        except Exception as e:
            print('Error en la modificacion: {}'.format(e))
            self.conn.rollback()
            correcto=False
        finally:
            self.close()
            return correcto

    def id(self):
        result = False
        try:
            sql="SELECT ifnull(MAX(id+1),1) FROM grupo"
            self.conectabd()
            self.conector.execute(sql)
            result=self.conector.fetchall()
        except Exception as e:
            print('error en la consulta: {}'.format(e))
        finally:
            self.close()
            return result
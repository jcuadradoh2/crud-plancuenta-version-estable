import sys
from colorama import Fore
from conexion import conexion
import os
class DaoPlanCuenta(conexion):
    def __init__(self):
        super().__init__()

    def consulta(self, buscar):        
        result = False
        column_names = ''
        try:
            sql="Select * from view_plancuenta where descripcion like '%" + str(buscar) + "%' order by id"            
            self.conectabd()
            self.conector.execute(sql)
            column_names = [i[0] for i in self.conector.description]
            result = self.conector.fetchall()
            self.conn.commit()
        except Exception as e:
            print('Error en la consulta plan de cuentas', e)
            self.conn.rollback()            
        finally:
            self.close()
        return column_names, result       

    #--------------------------------------------------------------------
    def insertar(self, pc):
        correcto = True        
        try:                  
            sql='insert into plancuenta (codigo, idgrupo, descripcion, naturaleza, estado) values (%s, %s, %s, %s, %s)'            
            self.conectabd()           
            x=''
            #x=pc.estado==True and '1' or '0'                        
            self.conector.execute(sql, (pc.codigo, pc.grupo, pc.descripcion, pc.naturaleza, pc.estado))               
            self.conn.commit()
        except Exception as e:
            print('Error en la insercion de plan de cuentas', e)                
            print(e.args)         
            self.conn.rollback()            
        finally:
            self.close()
        return correcto       

    #--------------------------------------------------------------------
    def modificar(self, pc):
        correcto = True        
        try:
            #sql='update plancuenta set codigo = %s, idgrupo = $s, descripcion = %s, naturaleza = $s, estado = %s where id = %s'
            sql='update plancuenta set codigo=  %s, idgrupo= %s, descripcion= %s, naturaleza= %s, estado= %s where id= %s'
            self.conectabd()
            x=''
            #x=pc.estado==True and '1' or '0'
            print(pc.codigo, pc.grupo, pc.descripcion, pc.naturaleza, pc.estado, pc.id) 
            self.conector.execute(sql, (pc.codigo, pc.grupo, pc.descripcion, pc.naturaleza, x, pc.id))                                    
            self.conn.commit()
        except Exception as e:
            print('Error en la modificacion de plan de cuentas', e)
            self.conn.rollback()            
        finally:
            self.close()
        return correcto 

    #--------------------------------------------------------------------
    def eliminar(self, pc):
        correcto = True        
        try:
            sql="delete from plancuenta where id= %s"
            self.conectabd()            
            self.conector.execute(sql, (pc.id))                                    
            self.conn.commit()
        except Exception as e:
            print('Error en la eliminacion de plan de cuentas', e)
            self.conn.rollback()
            correcto = False            
        finally:
            self.close()
        return correcto 

    def valId(self, pc):
        result=''
        try:
            sql="Select * from view_plancuenta where id= " + str(pc)
            self.conectabd()
            self.conector.execute(sql)            
            result = self.conector.fetchone()
            self.conn.commit()
        except Exception as e:
            print('Error en la consulta plan de cuentas', e)
            self.conn.rollback()            
        finally:
            self.close()
        return result  

    def returnDato(self, pc):
        result=''
        try:                       
            self.conectabd()
            self.conector.execute(pc)            
            result = self.conector.fetchone()
            self.conn.commit()
        except Exception as e:
            print('Error en la consulta plan de cuentas', e)
            self.conn.rollback()            
        finally:
            self.close()
        return str(result)

    def create_view(self):                
        correcto = True                
        if self.returnDato("select IF (EXISTS (select TABLE_NAME from information_schema.TABLES where Table_Name = 'view_plancuenta' and  table_schema='BDcuentas'), 1, 0) AS FOUND;").strip(')(,') == '0':                   
            try:
                sql= "create view if not exists view_plancuenta as select pc.id Id, pc.codigo, pc.idgrupo as 'grupo', pc.descripcion, pc.naturaleza, pc.estado  FROM plancuenta pc inner join grupo gp on pc.idgrupo = gp.id;"                
                self.conectabd()          
                self.conector.execute(sql)                                    
                self.conn.commit()
            except Exception as e:
                print('Error en la creacion de la vista', e)
                self.conn.rollback()
                correcto = False            
            finally:
                self.close()        
        return correcto 

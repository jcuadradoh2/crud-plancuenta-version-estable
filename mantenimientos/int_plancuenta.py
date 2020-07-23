import sys
from ctrPlanCuentas import ctrPlanCuenta
from mod_plancuenta import PlanCuenta
from funciones import *
import os
from colorama import Fore
import msvcrt
from interfaz import Consultar as grConsul

ctr = ctrPlanCuenta()
men=('Ingrese un codigo: ', 'Ingrese un grupo: ', 'Ingrese una descripcion: ', 'Ingrese la naturaleza: ', 'Ingrese un estado [0/1]: ', 'Ingrese el id: ')

def insertar(rango=0):
    grConsul()
    for i in range (int(rango)):                
        if ctr.insertar(inputs('i')):
            mensaje('Registro grabado correctamente', 'i')
        else:
            mensaje('Error en la insercion', 'a')
        input('Presione una tecla para continuar...')
        os.system('cls')
        consultar(False)

def inputs(id=0):     
    cdg=validarNumeros(input(men[0]), men[0])
    gp=validarNumeros(input(men[1]), men[1])    
    while ctr.returnDato("select * from grupo where id = " +gp) == 'None':
        mensaje('EL ID ES INCORRECTO, ASEGURECE DE QUE EXISTA UN GRUPO ASOCIADO A ESE ID', 'a')
        gp=validarNumeros(input(men[1]), men[1])
    dscr=validarLetra(input(men[2]), men[2])    
    nat=input(men[3])
    while len(nat) > 1:
        nat=validarLetra(input(men[3]), men[3])
    est=input(men[4])
    while not (est=='1' or est=='0'):
        mensaje('EL CAMPO "ESTADO" SOLO ADMITE VALORES DE 0 y 1', 'a')
        est=input(men[4])
    
    mod=PlanCuenta(id=id, cod=cdg, grupo=gp, descr=dscr, nat=nat, est=est)
    return mod

def modificar():    
    id=validarNumeros(input(men[5]), men[5])        
    if ctr.valId(id) != None:
        if ctr.modificar(inputs(id)):
            mensaje('Registro modificado correctamente', 'i')
        else:
            mensaje('Error al modificar el registro', 'a')
    else:
        mensaje('EL ID QUE HA INGRESADO NO SE ENCONTRÓ EN EL REGISTRO', 'a')

def eliminar():    
    global men 
    cdg=validarNumeros(input(men[5]), men[5])  
    while ctr.valId(cdg) == None:
        mensaje('EL ID QUE HA INGRESADO NO SE ENCONTRÓ EN EL REGISTRO', 'a')
        cdg=validarNumeros(input(men[5]), men[5])      
    mod=PlanCuenta(id=cdg)    
    if ctr.eliminar(mod):
        mensaje('Registro eliminado correctamente', 'i')
    else:
        mensaje('Error al eliminar el registro', 'a')
def consultar(ok):
    buscar=''
    imprimir(buscar)     
    if ok:                                                           
        buscar=input('Ingrese descripcion a buscar: ')        
    imprimir(buscar)

def imprimir(args):
    os.system('cls||clear')        
    args= ctr.consulta(args)    
    st=''
    ln=113
    for x in args[0]:         
        st+=' '+str(x)+'\t\t'    
    print(Fore.WHITE+'-'*ln+'\n| '+ Fore.LIGHTBLUE_EX + st.strip().upper()+ '\t\t'+Fore.WHITE+'|'+'\n' +'-'*ln)
    for r in args[1]:
        x=''
        x=r[5]==1 and 'True' or 'False' 
        print('| {0:15} {1:7}   {2:7}\t\t {3:30}{4:15}   {5:15}|'.format(str(r[0]),r[1],r[2],r[3],r[4],x))
    print('-'*ln)        


def ejecutar_plancuenta(): 
    if ctr.create_view():
        opc=''
        while True:
            os.system('cls||clear')
            opc=str(menu('  MENU PLAN DE CUENTAS'))
            if opc =='0':
                if valOpciones('INGRESAR'):
                    os.system('cls||clear')
                    mensaje('\t<<<Insertar datos>>> ','i')
                    value=input('Defina la cantidad de datos a ingresar -> ')
                    if value != '' or None : insertar(value)
            elif opc=='1':
                if valOpciones('CONSULTAR'):
                    mensaje('\n\t<<<Consultar datos>>> ', 'i')
                    consultar(True)            
            elif opc=='2':
                if valOpciones('MODIFICAR'):
                    mensaje('\n\t<<<Modificar datos>>> ', 'i')            
                    consultar(False)
                    modificar()                      
            elif opc=='3':
                if valOpciones('ELIMINAR'):
                    mensaje('\n\t<<<Eliminar datos>>> ', 'i')                        
                    consultar(False)
                    eliminar()  
            elif opc=='4':
                if valOpciones('SALIR'):
                    #mensaje('\n\t<<<Gracias por usar el Sistema>>> \n', 'i')
                    input('Presione una tecla para continuar...')
                    break
            elif opc!='4':
                mensaje('\n\t<<<Seleccione una opcion correcta>>> ', 'a')
            input('Presione una tecla para continuar...')
            os.system('cls')

    

#-------------------------------------------------------
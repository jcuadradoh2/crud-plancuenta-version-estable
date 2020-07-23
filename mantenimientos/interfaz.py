from ctrGrupo import controlador
from funciones import *
from modGrupo import modGrupo
import os
from colorama import Style, Back, Cursor, Fore, init
init()
men=('ingrese el grupo: ','ingrese codigo de dato a eliminar: ','ingrese el id a modificar: ','ingrese grupo a buscar(enter para ver todos): ','Cuantos grupos va a ingresar: ')
ctr = controlador()

def insertar(rango):
    for paso in range(int(rango)):
        ing = validarLetra(input(men[0]),men[0])
        gr=modGrupo(id=0, des=ing)
        if ctr.insertar(gr):
            print('Registro Guardado exitosamente')
        else:
            print('error al insertar registro')
    input(Cursor.DOWN(3) + 'Presione una tecla para continuar....: ')

def eliminar():
    ing = validarNumeros(input(men[1]),men[1])
    gr = modGrupo(id=int(ing))
    if ctr.eliminar(gr):
        print('Registro eliminado exitosamente')
    else:
        print('error al eliminar registro')
    input(Cursor.DOWN(3) + 'Presione una tecla para continuar....: ')

def modificar():
    id=validarNumeros(input(men[2]),men[2])
    des=validarLetra(input(men[0]),men[0])
    gr = modGrupo(id=id, des=des)
    if ctr.modificar(gr) :
        print('Registro actualizado exitosamente')
    else:
        print('error al actualizar registro')
    input(Cursor.DOWN(3) + 'Presione una tecla para continuar....: ')

def Consultar(busca='', ban=0):
    result=ctr.consultar(busca)
    print('-'*34, Cursor.DOWN(1) + Cursor.BACK(35) + '{:3}'.format('|'), 
    Style.BRIGHT + Fore.BLUE + '{:15} {:12}'.format('ID', 'Grupo'), 
    Style.RESET_ALL + '|', Cursor.DOWN(1) + Cursor.BACK(35) +('-'*34))
    for x in result:
        print('{:3} {:15} {:12} |'.format('|', str(x[0]), x[1]), 
        Cursor.DOWN(1) + Cursor.BACK(35) + '-'*34)
    if ban == 1:
        input(Cursor.DOWN(3) + 'Presione una tecla para continuar....: ')
        ban = 0
    else:
        ban = 0

def ejecuta():
    while True:
        opc=MenuGrupo(('Ingresar', 'Modificar','Eliminar','Consultar','Retornar al menu principal'),'Menu Grupos')
        if opc == 1:
            if valOpciones('ingresar'):
                os.system('cls')
                rango=validarNumeros(input(men[4]),men[4])
                insertar(rango)
            else:
                os.system('cls')
        elif opc == 2:
            if valOpciones('Modificar'):
                os.system('cls')
                Consultar()
                modificar()
            else:
                os.system('cls')
        elif opc == 3:
            if valOpciones('eliminar'):
                os.system('cls')
                Consultar()
                eliminar()
            else:
                os.system('cls')
        elif opc ==4:
            if valOpciones('consultar'):
                os.system('cls')
                x=1
                #busca = input(men[3])
                #if busca != "":
                busca = validarLet(input(men[3]), men[3])
                Consultar(busca,x)
            else:
                os.system('cls')
        elif opc == 5:
            confirma = 'pasa'
            while confirma != 'y' and confirma != 'n':
                confirma = input('¿Esta seguro de salir?(Y/N): ').lower()
            if confirma == 'y':
                os.system('cls')
                input('Presione una tecla para continuar....: ')
                break
            else:
                continue
os.system('cls')

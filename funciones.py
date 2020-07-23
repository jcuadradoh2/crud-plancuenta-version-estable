from colorama import Style, Fore, Cursor, init
init()
import sys
import os

def MenuGrupo(opcion,titulo):
    os.system('cls')
    print('-'*41, Cursor.DOWN(1) + Cursor.BACK(42) + "{:14} {:33}".format('|',Style.BRIGHT+Fore.BLUE+titulo),
    Style.RESET_ALL + "|", Cursor.DOWN(1) + Cursor.BACK(42) + '-'*41)
    for x in range(len(opcion)):
        print("{:3} {:5} {:30}|".format('|',str(x+1)+')',opcion[x]))
    print('-'*41)
    while True:
        opc = int(input('ingrese opcion [1...{}]: ' .format(len(opcion))))
        if 1 <= opc <= int(len(opcion)):
            break
    return opc

def menu(titulo, opciones = ('Ingresar', 'Consultar', 'Modificar', 'Eliminar', 'Retornar Menu Principal')):
    print('-'*49)
    print(Fore.LIGHTBLUE_EX+'\t\t{0:10}'.format(titulo.upper()), Fore.WHITE)
    print('-'*49)
    for op in range(0,len(opciones)):
        print("{0})  {1}".format(op, opciones[op]))
    print('\n')
    opc = input('Elija Opcion [0/{}]: '.format(len(opciones)-1))
    return opc

#-------------------------------------------------------------
def mensaje(msj, tipo):
    msj=msj.upper()
    #tipo == a:alert, i:information
    if tipo=='a':
         print(Fore.RED+msj+Fore.WHITE)
    elif tipo=='i':
         print(Fore.BLUE+msj+Fore.WHITE)


#Metodo para validar que solo hayan letras
def validarLetra(args, msj):        
    copy=args.replace(' ', '')
    while (not copy.isalpha() or args == ''):
        mensaje('TIPO DE DATO INCORRECTO', 'a')
        args=input(msj)
        copy=args.replace(' ', '')
    return args

def validarLet(args, msj):        
    copy=args.replace(' ', '')
    while (not copy.isalpha() and copy != ''):
        mensaje('TIPO DE DATO INCORRECTO', 'a')
        args=input(msj)
        copy=args.replace(' ', '')
    return args

#Metodo para validar que solo hayan numeros
def validarNumeros(args, msj): 
    global men  
    while not args.isdigit() or args == '':  
        mensaje('TIPO DE DATO INCORRECTO', 'a')
        args=input(msj)            
    return args    


#Metodo para confirmar opciones
def valOpciones(args):        
    bol='Usted a seleccionado la opcion '+args+'. ¿Desea continuar? [y/N]   '
    var = input(bol).upper()
    while not (var == 'N' or var == 'Y'):
        os.system('cls||clear')
        var = input(bol).upper()
    if var == 'N':
        mensaje('Operacion cancelada.', 'a')
        bol= False
    else:
        bol=True
    return bol

#Metodo que llama al menu principal
def menu_principal(opciones,titulo):
    os.system('cls')
    print('-'* 40, Cursor.DOWN(1) + Cursor.BACK(41) + '{:15}{:29}{}'.format('|',Fore.BLUE+titulo, Style.RESET_ALL+'|'),
    Cursor.DOWN(1) + Cursor.BACK(41) + '-'*40)
    for x in range (len(opciones)):
        print("{:3} {:5} {:29}|".format('|',str(x+1)+')',opciones[x]))
    print('-'*40)
    mn = 3
    while mn != '1' and mn != '2' and mn != '3':
        mn = input('Elija Opcion [1/{}] '.format(len(opciones)))
    return mn
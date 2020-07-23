from interfaz import ejecuta, Consultar
from int_plancuenta import ejecutar_plancuenta
from funciones import menu_principal, valOpciones, mensaje


def ejec():
    while True:
        paso = menu_principal(['Grupo','Plan Cuenta','Salir'],'MENU PRINCIPAL')
        if paso == '1':
            ejecuta()
        elif paso == '2':
            ejecutar_plancuenta()
        elif paso == '3':
            if valOpciones('Salir'):
                mensaje('\n\t<<<Gracias por usar el Sistema>>> \n', 'i')
                input('Presione una tecla para continuar...')
                break
ejec()
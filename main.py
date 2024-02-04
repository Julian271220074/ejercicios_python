import metodos
import ejercicio_01
import ejercicio_02
import ejercicio_03
import ejercicio_04
import ejercicio_05
import ejercicio_06
import ejercicio_07
import ejercicio_08
import ejercicio_09
import ejercicio_10
import ejercicio_11
import ejercicio_12
import ejercicio_13
import ejercicio_14
import ejercicio_15


def menu():
    while True:
        print("")
        print("--------  MENU PRINCIPAL  --------")
        print(metodos.informacion("Seleccione una opcion para iniciar el programa"))
        print(metodos.informacion(""))
        print(metodos.informacion("1| Division de 2 numeros"))
        print(metodos.informacion("2| Par o impar"))
        print(metodos.informacion("3| Area del circulo"))
        print(metodos.informacion("4| Multiplo de 2 y 3"))
        print(metodos.informacion("5| Validar fecha"))
        print(metodos.informacion("6| Validar mayor - medio - menor"))
        print(metodos.informacion("7| Calcular hipotenusa"))
        print(metodos.informacion("8| Convertidor de numero de mes a texto"))
        print(metodos.informacion("9| Convertidor de segundos a horas y minutos"))
        print(metodos.informacion("10| Numero inverso"))
        print(metodos.informacion("11| Verificar si un numero es capicua"))
        print(metodos.informacion("12| Numero de ocurrencias de un caracter"))
        print(metodos.informacion("13| Validar cadena pailindroma"))
        print(metodos.informacion("14| Pedir un número de 0 a 99 y mostrarlo escrito"))
        print(metodos.informacion("15| Capitalizar frase"))

        print(metodos.informacion("40| Salir"))

        opcion = metodos.texto_a_numero(input())
        if opcion == 1:
            ejercicio_01.menu_cociente()
        elif opcion == 2:
            ejercicio_02.menu_par()
        elif opcion == 3:
            ejercicio_03.menu_area_circulo()
        elif opcion == 4:
            ejercicio_04.menu_multiplos()
        elif opcion == 5:
            ejercicio_05.menu_validar_fecha()
        elif opcion == 6:
            ejercicio_06.menu_mayor_medio_menor()
        elif opcion == 7:
            ejercicio_07.menu_calcular_hipotenusa()
        elif opcion == 8:
            ejercicio_08.menu_imprimir_mes()
        elif opcion == 9:
            ejercicio_09.menu_convertir_segundos()
        elif opcion == 10:
            ejercicio_10.menu_numeros_inversos()
        elif opcion == 11:
            ejercicio_11.menu_verifia_capicua()
        elif opcion == 12:
            ejercicio_12.menu_ocurrencias_caracter()
        elif opcion == 13:
            ejercicio_13.menu_verificador_cadena_palindroma()
        elif opcion == 14:
            ejercicio_14.menu_convertir_numero_a_palabra()
        elif opcion == 15:
            ejercicio_15.menu_capitalizar_frase()
        elif opcion == 40:
            print(metodos.salida("El programa ha termidado correctamente"))
            exit(0)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(metodos.bienvenida("*** Bienvenido al Programa ***"))
    menu()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

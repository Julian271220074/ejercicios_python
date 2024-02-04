import metodos

'''
: Se debe de ingresar un numero comprendido entre 1 y 12 por el usuario. El algoritmo debe
de imprimir el mes correspondiente en texto.
'''



def obtener_numero_mes():
    while True:
        try:
            numero_mes = int(input(metodos.informacion("Digite un número de mes (1-12): ")))
            if 1 <= numero_mes <= 12:
                return numero_mes
            else:
                print(metodos.error("Por favor, digite un número de mes válido."))
        except ValueError:
            print(metodos.error("Por favor, digite un número entero."))


def imprimir_mes_texto(numero_mes):

    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    nombre_mes = meses[numero_mes - 1]
    print(metodos.resultado(f"El número {numero_mes} corresponde al mes de {nombre_mes}."))


def menu_imprimir_mes():
    """
    metodo para convertir de numero de mes a texto
    :return:
    """

    print(metodos.bienvenida("--- Convertidor de número de mes a texto ---"))

    numero_mes = obtener_numero_mes()
    imprimir_mes_texto(numero_mes)


if __name__ == "__main__":
    menu_imprimir_mes()

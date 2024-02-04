import metodos

'''
Se debe de ingresar un numero por el usuario, este debe de ser evaluado para verificar que el
número de cifras sea par y verificar si el número es capicúa o no.

'''


def es_cifras_par(numero: int) -> bool:
    cantidad_cifras = len(str(abs(numero)))
    return cantidad_cifras % 2 == 0


def es_capicua(numero: int) -> bool:
    str_numero = str(abs(numero))
    return str_numero == str_numero[::-1]


def menu_verifia_capicua():
    """
    Metodo para verificar si numero tiene cifras par y es capicua
    :return:
    """
    print(metodos.bienvenida("--- Verificador de cifras par y capicúa ---"))

    print(metodos.informacion("Digite un numero:"))
    numero = metodos.texto_a_numero(input())

    if es_cifras_par(numero):
        print(metodos.resultado("El número de cifras es par."))
    else:
        print(metodos.resultado("El número de cifras no es par."))

    if es_capicua(numero):
        print(metodos.resultado("El número es capicúa."))
    else:
        print(metodos.resultado("El número no es capicúa."))


if __name__ == "__main__":
    menu_verifia_capicua()

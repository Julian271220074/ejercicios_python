import metodos

'''
 Desarrollar un algoritmo que determine si una cadena de caracteres es palíndroma. Una
cadena se dice palíndromo si al invertirla es igual a ella misma.
'''


def verificar_palindroma(cadena: str):
    cadena = cadena.lower()
    cadena = ''.join(c for c in cadena if c.isalnum())
    return cadena == cadena[::-1]


def menu_verificador_cadena_palindroma():
    """
    Metodo para validar si una cadena de caracteres es palindroma
    :return:
    """
    print(metodos.bienvenida("--- Verificador de palíndromos ---"))

    cadena = input(metodos.informacion("Digite una cadena de caracteres: "))

    if verificar_palindroma(cadena):
        print(metodos.resultado("La cadena es palíndroma."))
    else:
        print(metodos.resultado("La cadena no es palíndroma."))


if __name__ == "__main__":
    menu_verificador_cadena_palindroma()

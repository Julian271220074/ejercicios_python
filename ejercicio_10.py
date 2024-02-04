import metodos

'''
Dado un número entero leído por pantalla, muestre cada uno de los dígitos del número en
orden inverso. Ej: Si el número es 324, se debe mostrar 4, 2, 3.
'''


def invertir_numeros(numero: int) -> bool:
    digitos_inversos = [int(d) for d in str(numero)][::-1]
    return digitos_inversos


def menu_numeros_inversos():
    """
    metodo para mostrar numeros de manera inversa
    :return:
    """
    print(metodos.bienvenida(" ---Mostrar numeros en orden inverso ---"))

    print(metodos.informacion("Digite un numero:"))
    numero = metodos.texto_a_numero(input())

    digitos_inversos = invertir_numeros(numero)

    print(metodos.resultado(f"Los numeros en orden inverso son: {', '.join(map(str, digitos_inversos))}"))


if __name__ == "__main__":
    menu_numeros_inversos()

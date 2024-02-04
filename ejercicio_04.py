import metodos

'''
En este problema tenemos un único dato de entrada: un valor numérico entero que deberá
ingresar el usuario. La salida del algoritmo será informar si el numero ingresado por el usuario es
múltiplo de 2 y 3. Sabemos que un número es múltiplo de otro cuando al dividir estos dos
números el residuo sea 0. Si el usuario ingresó un valor negativo o cero tendremos que emitir un
mensaje informando las causas por las cuales no se podrá efectuar la operación.
'''


def calcular_multiplo(numero: int) -> bool:
    if numero <= 0:
        print(metodos.error("El numero debe ser mayor a cero"))
        return False
    return numero % 2 == 0 and numero % 3 == 0


def menu_multiplos():
    """
    Metodo para valiadar si un numero es multiplo de 2 y 3
    :return:
    """

    print(metodos.bienvenida("--- Calcular multiplos de 2 y 3 ---"))

    numero = metodos.texto_a_numero(input(metodos.informacion("Digite un numero entero positivo: ")))
    result = calcular_multiplo(numero)
    print(f"El numero {numero} {result and metodos.resultado('SI') or metodos.error('NO')} es multiplo de 2 y 3")


if __name__ == '__main__':
    menu_multiplos()
    print(calcular_multiplo(12))
    print(calcular_multiplo(50))

import metodos

'''
 En este problema, los datos de entrada son los dos valores enteros que ingresará el usuario a
través del teclado (los llamaremos a y b) y la salida será su cociente (un número flotante). Ahora
bien, existe la posibilidad de que el usuario ingrese como segundo valor el número 0 (cero). En
este caso, no podremos mostrar el cociente ya que la división por cero es una indeterminación, así
que tendremos que emitir un mensaje informando las causas por las cuales no se podrá efectuar
la operación.

 '''


def calcular_cociente(numero_1: int, numero_2: int) -> float:
    """
    metodo para calcular el cociente de dos numeros
    :param numero_1:
    :param numero_2:
    :return:
    """

    if numero_2 == 0:
        print(metodos.error("La division por cero es una indeterminacion"))
        return 0
    else:
        return round(numero_1 / numero_2, 2)


def menu_cociente():
    """
    metodo para mostrar el cociente de una division
    :return:
    """
    print(metodos.bienvenida("---- Calcular Cociente ----"))

    print(metodos.informacion("Digite el primer numero:"))
    numero_1 = metodos.texto_a_numero(input())

    print(metodos.informacion("Digite el segundo numero:"))
    numero_2 = metodos.texto_a_numero(input())

    resultado = calcular_cociente(numero_1, numero_2)

    print(metodos.resultado(f"El resultado del  cociente es: {resultado}"))


if __name__ == '__main__':
    a = 8
    b = 2
    print(calcular_cociente(a, b))

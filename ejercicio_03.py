import metodos
import math

'''
En este problema debemos de definir una constante con el valor de PI como 3,1416 y
tenemos un único dato de entrada dado por el usuario: un valor numérico que puede ser entero o
flotante que indicara el radio de un círculo. La salida del algoritmo será el área del circulo teniendo
en cuenta que A=PI*r^2. Si el usuario ingresó valor negativo o cero tendremos que emitir un
mensaje informando las causas por las cuales no se podrá efectuar la operación.
'''


def calcular_area(numero: int | float) -> bool | float:
    if numero < 0:
        print(metodos.error("El numero debe ser mayor a cero"))
        return False
    else:
        return round(math.pi * math.pow(numero, 2), 2)


def menu_area_circulo():
    """
    Metodo para calcular el area del circulo
    :return:
    """
    print(metodos.bienvenida("--- Calcular area de un circulo ---"))

    numero = metodos.texto_a_numero(input(metodos.informacion("Digite el valor de la radio del circulo: ")))
    result = calcular_area(numero)

    if result:
        print(metodos.resultado(f"Para un circulo de {numero} radio el area es: {result}"))
    else:
        print(metodos.error(f"Para un circulo de {numero} no se puede calcular el area"))


if __name__ == '__main__':
  menu_area_circulo()

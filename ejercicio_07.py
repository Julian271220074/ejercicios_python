import metodos

'''
Calcular la hipotenusa de un triángulo, teniendo como base el valor del cateto 1 y 2 que serán
dados por el usuario. Para esto debe de hacer uso del Teorema de Pitágoras en el cálculo de la
hipotenusa teniendo los catetos. (h= √(a^2 )+b^2) no se debe hacer uso de la librería Math.hypot
'''


def calcular_hipotenusa(cateto1: int | float, cateto2: int | float) -> float | bool:
    hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 0.5
    return hipotenusa


def menu_calcular_hipotenusa():
    """
    Metodo para calcular la hipotenusa
    :return:
    """

    print(metodos.bienvenida("--- Calculadora de hipotenusa ---"))

    print(metodos.informacion("Digite el valor de cateto 1:"))
    cateto1 = metodos.texto_a_numero(input())

    print(metodos.informacion("Digite el valor de cateto 2:"))
    cateto2 = metodos.texto_a_numero(input())

    resultado = calcular_hipotenusa(cateto1, cateto2)

    print(metodos.resultado(f"\nLa hipotenusa del triángulo con catetos {cateto1} y {cateto2} es: {resultado}"))


if __name__ == "__main__":
    menu_calcular_hipotenusa()

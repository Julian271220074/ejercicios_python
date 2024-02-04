import metodos

'''
Pedir un número de 0 a 99 y mostrarlo escrito. Por ejemplo, para 56 mostrar: cincuenta y
seis.
'''


def obtener_numero():

    while True:
        try:
            numero = int(input(metodos.informacion("Digite un número entre 0 y 99: ")))
            if 0 <= numero <= 99:
                return numero
            else:
                print(metodos.error("Digite un número válido en el rango especificado."))
        except ValueError:
            print(metodos.error("Por favor, digite un número entero."))


def convertir_a_palabras(numero: int):

    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    decenas = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]

    if 1 <= numero <= 9:
        return unidades[numero]
    elif 10 <= numero <= 19:
        return "dieci" + unidades[numero % 10]
    elif 20 <= numero <= 29:
        return "veinti" + unidades[numero % 10]
    else:
        return decenas[numero // 10] + (" y " + unidades[numero % 10] if numero % 10 != 0 else "")


def menu_convertir_numero_a_palabra():

    print(metodos.bienvenida("--- Convertidor de números a palabras ---"))

    numero = obtener_numero()

    resultado = convertir_a_palabras(numero)

    print(metodos.resultado(f"El número {numero} escrito es: {resultado}"))


if __name__ == "__main__":
    menu_convertir_numero_a_palabra()

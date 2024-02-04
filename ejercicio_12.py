import metodos

'''
Desarrollar un algoritmo que reciba como entrada un carácter y de cómo salida el número de
ocurrencias de dicho carácter en una cadena de caracteres.
'''



def contar_ocurrencias(caracter: str, cadena):
    return cadena.count(caracter)


def menu_ocurrencias_caracter():
    """
    Metodo para contar el numero de ocurrencias de un caracter
    :return:
    """
    print(metodos.bienvenida("--- Contador de ocurrencias de un carácter en una cadena ---"))

    caracter = input(metodos.informacion("Digite un carácter: "))
    cadena = input(metodos.informacion("Digite una cadena de caracteres: "))

    if len(caracter) == 1:

        ocurrencias = contar_ocurrencias(caracter, cadena)
        print(metodos.resultado(f"El carácter '{caracter}' aparece {ocurrencias} veces en la cadena."))
    else:
        print(metodos.error("Por favor, ingresa solo un carácter."))


if __name__ == "__main__":
    menu_ocurrencias_caracter()

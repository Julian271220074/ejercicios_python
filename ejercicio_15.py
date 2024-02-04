import metodos

'''
Desarrollar un algoritmo que solicite una frase de mínimo 5 palabras y capitalizar la cadena

'''


def obtener_frase():
    while True:
        frase = input(metodos.informacion("Digite una frase con al menos 5 palabras: "))
        palabras = frase.split()
        if len(palabras) >= 5:
            return frase
        else:
            print(metodos.error("Digite una frase con al menos 5 palabras."))


def capitalizar_frase(frase: str):

    palabras = frase.split()
    capitalizadas = [palabra.capitalize() for palabra in palabras]
    return ' '.join(capitalizadas)


def menu_capitalizar_frase():
    """
    Metodo para capitalizar una frase
    :return:
    """

    print(metodos.bienvenida("--- Capitalizador de frases ---"))

    frase = obtener_frase()

    frase_capitalizada = capitalizar_frase(frase)

    print(metodos.resultado(f"La frase capitalizada es: {frase_capitalizada}"))


if __name__ == "__main__":
    menu_capitalizar_frase()

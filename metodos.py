colores = "\033[90m {}\033[0m"


def texto_color(texto: str, color: str):
    """
    Metodo para darle color a un texto
    :param texto: texto al cual se le va a modificar el color
    :param color: color que se le aplicara al texto
    :return: texto
    """

    global colores
    if color == "rojo":
        colores = "\033[91m {}\033[0m"
    elif color == "verde":
        colores = "\033[92m {}\033[0m"
    elif color == "amarillo":
        colores = "\033[93m {}\033[0m"
    elif color == "moradoClaro":
        colores = "\033[94m {}\033[0m"
    elif color == "morado":
        colores = "\033[95m {}\033[0m"
    elif color == "cyan":
        colores = "\033[96m {}\033[0m"
    elif color == "grisClaro":
        colores = "\033[97m {}\033[0m"
    elif color == "negro":
        colores = "\033[90m {}\033[0m"

    return colores.format(texto)


def informacion(texto: str):
    return texto_color(texto, "cyan")


def error(texto: str):
    return texto_color(texto, "rojo")


def resultado(texto: str):
    return texto_color(texto, "verde")


def bienvenida(texto: str):
    return texto_color(texto, "morado")


def advertencia(texto: str):
    return texto_color(texto, "amarillo")


def salida(texto: str):
    return texto_color(texto, "grisClaro")


def obtener_entero(mensaje: str = None) -> int:
    """
    Metodo para solicitar y validar un numero
    :param mensaje:
    :return:
    """

    valor = input(mensaje if mensaje is not None else informacion("Digite un numero entero"))
    while True:
        try:
            return int(valor)
        except ValueError:
            print(error(f"El texto\"{valor}\" no se puede convertir a numero entero"))
            valor = input(advertencia("Digite nuevamente un numero entero: "))


def texto_a_numero(valor: str = None) -> int:
    while True:
        if valor.isnumeric():
            return int(valor)
        else:
            print(error(f"El siguiente texto {valor} no se puede convertir a numero"))
            print(advertencia("Ingrese nuevamente un numero"))
            valor = input()

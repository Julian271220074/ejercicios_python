import metodos
from datetime import datetime

'''
En este problema Se ingresa un valor numérico de 8 dígitos que representa una fecha con el
siguiente formato: aaaammdd. Esto es: los 4 primeros dígitos representan el año, los siguientes 2
dígitos representan el mes y los 2 dígitos restantes representan el día. Se pide informar por
separado el día, el mes y el año de la fecha ingresada. Para su solución se debe de hacer uso de
divisiones, operador modulo y conversión de double a entero.
'''


def validar_fecha(cadena: str, formato: str = '%Y%m%d') -> bool:
    try:
        fecha = datetime.strptime(cadena, formato)
        return True
    except ValueError as msg_error:
        return False


def extraer_fecha(fecha: int) -> ():
    str_fecha = str(fecha)
    if len(str_fecha) == 8:
        fecha = validar_fecha(str_fecha)
        if fecha:
            return str_fecha[:4], str_fecha[4:6], str_fecha[6:]
        else:
            print(metodos.error(f"La cadena {str_fecha} no es fecha real valida..."))
    else:
        print(metodos.error(f"La cadena {str_fecha} no esta en el formato correcto aaaammdd..."))

        #  if 10000000 <= fecha <= 99999999:
        #     if validar_fecha(str(fecha)):
        #        anio = fecha // 10000
        #       mes = (fecha % 10000) // 100
        #       dia = fecha % 100
        #      return anio, mes, dias
        return False


def menu_validar_fecha():
    """
    Metodo para valiadar si una fecha es valida en un formato de aaaammdd
    :return:
    """
    print(metodos.bienvenida("--- Validar Fecha (aaaammdd) ---"))

    numero = metodos.texto_a_numero(input(metodos.informacion("Digite una fecha en el formato aaaammdd: ")))
    result = extraer_fecha(numero)
    if result:
        print(metodos.resultado(
            f"El numero {numero} representa la fecha {result[2]}/{result[1]}/{result[0]} que es valida"))


if __name__ == '__main__':
    menu_validar_fecha()


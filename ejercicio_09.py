import metodos

'''
Dado un número (leído por teclado), que representa los segundos que ha invertido una
persona en hacer un examen, determinar cuántas horas, minutos y segundos ha invertido.
Imprima el resultado por pantalla
'''


def convertir_segundos(segundos: int):
    if segundos > 0:
        minutos = segundos / 60
        horas = segundos / 3600
        return horas, minutos, segundos

    else:
        print(metodos.error("Digite un numero mayor a cero"))


def menu_convertir_segundos():
    """
    metodo para convertir segundos a horas y minutos
    :return:
    """
    print(metodos.bienvenida("--- Convertidor de segundos a horas, minutos y segundos ---"))

    print(metodos.informacion("Digite el numero de segundos gastados en el examen:"))
    segundos = metodos.texto_a_numero(input())

    horas, minutos, segundos = convertir_segundos(segundos)

    print(metodos.resultado(f"El tiempo invertido es: {horas} horas:{minutos} minutos:{segundos} segundos"))


if __name__ == "__main__":
    menu_convertir_segundos()

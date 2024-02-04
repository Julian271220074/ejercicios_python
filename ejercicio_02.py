import metodos

'''En este problema tenemos un único dato de entrada: un valor numérico entero que deberá
ingresar el usuario. La salida del algoritmo será informar si el usuario ingresó un valor par o impar.
Sabemos que un número par es aquel que es divisible por 2 o, también, que un número es par si el
valor residual que se obtiene al dividirlo por 2 es cero. Según lo anterior, podremos informar que
el número ingresado por el usuario es par si al dividirlo por 2 obtenemos un resto igual a cero. De
lo contrario, informaremos que el número es impar.
  '''
def numero_es_par(numero: int) -> bool:
    return  numero % 2 == 0




def menu_par():
    """
    metodo para validar si un numero es par o impar
    :return:
    """
    print(metodos.bienvenida("--- Par o Impar ---"))

    print(metodos.informacion("Digite el numero a validar"))
    numero = metodos.texto_a_numero(input())

    print(metodos.resultado("El numero es: " + ("par" if numero_es_par(numero) else "impar")))

if __name__ == '__main__':
        a = 8
        print(numero_es_par(a))
        menu_par()




import metodos

'''
Leer tres valores numéricos enteros, indicar cuál es el mayor, cuál es el del medio y cuál, el
menor. Considerar que los tres valores serán diferentes.
'''


def obtener_valores():
    while True:
        try:
            print(metodos.bienvenida("--- Validar mayor-medio-menor ---"))
            a = int(input(metodos.informacion("Digite el primer valor entero: ")))
            b = int(input(metodos.informacion("Digite el segundo valor entero: ")))
            c = int(input(metodos.informacion("Digite el tercer valor entero: ")))


            if a != b and b != c and a != c:
                return a, b, c
            else:
                print(metodos.error("Por favor, ingresa tres valores diferentes."))
        except ValueError:
            print(metodos.error("Por favor, ingresa valores numéricos enteros."))


def encontrar_mayor_medio_menor(a, b, c):
    mayor = max(a, b, c)
    menor = min(a, b, c)
    medio = (a + b + c) - mayor - menor
    return mayor, medio, menor


def menu_mayor_medio_menor():
    valores = obtener_valores()
    mayor, medio, menor = encontrar_mayor_medio_menor(*valores)

    print(metodos.resultado(f"\nEl mayor valor es: {mayor}"))
    print(metodos.resultado(f"El valor del medio es: {medio}"))
    print(metodos.resultado(f"El menor valor es: {menor}"))


if __name__ == "__main__":
    menu_mayor_medio_menor()

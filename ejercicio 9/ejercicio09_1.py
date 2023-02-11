#Primera parte: Escribir un algoritmo que calcula la media aritmética de tres números dados.


def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args):
        print("La media es: ", funcion_parametro(*args))
    return funcion_interior


@funcion_decoradora
def media_ponderada(list): # Calcula la media ponderada
    media = 0
    for i in list:
        media += i
    return media/len(list)


def inicio(): # Comprueba que los datos introducidos son números y pregunta por los números
    n1 = input("Introduce el primer número: ")
    n2 = input("Introduce el segundo número: ")
    n3 = input("Introduce el tercer número: ")
    try:
        n1 = int(n1)
        n2 = int(n2)
        n3 = int(n3)
        list = [n1, n2, n3]
        media_ponderada(list) # Llama a la función media_ponderada
    except:
        print("Error: No ha escrito un número")
        exit()

print("MEDIA ARITMÉTICA DE TRES NÚMEROS")
inicio()



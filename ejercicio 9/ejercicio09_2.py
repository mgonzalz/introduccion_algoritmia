#Segunda parte: Escribir un algoritmo que calcula la media ponderada cuando se dan los números y los coeficientes de ponderación.
def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args):
        print("La media es: ", funcion_parametro(*args))
    return funcion_interior

@funcion_decoradora
def media_ponderada(list, list_ponderacion): # Calcula la media ponderada
    media = 0
    for i in range(len(list)):
        media += list[i] * list_ponderacion[i]
    return media/sum(list_ponderacion)

def inicio():
    print("MEDIA PONDERADA")
    n = int(input("¿Cuántos números quiere introducir para realizar la media? "))
    list = []
    lista_ponderacion = []
    for i in range(n):
        num = input("Introduce el " + str(i+1) + "º número: ")
        try:
            num = int(num)
            list.append(num)
        except:
            print("Error: No ha escrito un número")
            exit()
    for i in range(n):
        c = input("Introduce el " + str(i+1) + "º coeficiente de ponderación: ")
        try:
            c = int(c)
            lista_ponderacion.append(c)
        except:
            print("Error: No ha escrito un número")
            exit()
    media_ponderada(list, lista_ponderacion)

inicio()

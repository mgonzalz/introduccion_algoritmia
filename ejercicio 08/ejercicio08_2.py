
#Segunda parte: Calcular el interes de un capital en un tiempo dado en meses
def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args):
        print("Con los intereses se muestra un total de: ", funcion_parametro(*args))
    return funcion_interior


@funcion_decoradora
def intereses(meses,capital,interes):
    return capital*interes*meses/100/12

meses = input("Introduce el tiempo en meses: ")
capital = input("Introduce el capital: ")
interes = input("Introduce el interes: ")
try:
    meses = int(meses)
    capital = int(capital)
    interes = int(interes)
    intereses(meses,capital,interes)
except:
    print("Error, introduce un numero")


#Primera parte: Calcular el area de un triangulo dado un lado y la altura relativa a este lado
def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args, **kwargs):
        print("El area del triangulo es: ", funcion_parametro(*args, **kwargs), "en metros cuadrados")
    return funcion_interior

@funcion_decoradora
def area_triangulo(lado,altura):
    return lado*altura/2



area_triangulo(lado = 5, altura = 10)

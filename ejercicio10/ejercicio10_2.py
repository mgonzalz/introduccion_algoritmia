
#Segunda parte: Calcular el area de un triangulo rectangulo dado dos lados perpendiculares
def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args, **kwargs):
        print("El area del triangulo es: ", funcion_parametro(*args, **kwargs), "en metros cuadrados")
    return funcion_interior

@funcion_decoradora
def area_triangulo(lado1,lado2):
    return lado1*lado2/2

area_triangulo(lado1 = 5, lado2 = 10)

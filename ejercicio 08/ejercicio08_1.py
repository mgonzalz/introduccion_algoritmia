#Primera parte: Precio con todos los impuestos y sin.


def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args, **kwargs):
        print("El precio sin impuestos es: ", precio, "€")
        print("El precio según el impusto los impuestos incluidos: ", funcion_parametro(*args, **kwargs), "€")
    return funcion_interior


@funcion_decoradora
def precio_con_iva(precio, iva):
    return precio + precio * iva



print("CALCULADORA DE PRECIOS sin/CON IVA")
precio = input("Introduce el precio sin impuestos: ")
try:
    precio = int(precio)
    precio_con_iva(precio, iva = 21/100)
except:
    print("Error: No ha escrito un número")
    exit()

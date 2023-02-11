'''
Se considera las cuentas de depósitos alojadas en un banco por los clientes. Solo se permite hacer una retirada si el saldo que queda en la cuenta no es negativo.

1. Definir el tipo de datos CUENTA..

2. Definir las operaciones aplicables.

En determinadas circunstancias y para determinados clientes, la banca autoriza un descubierto limitado y temporal.

3. Volver a hacer las definiciones previas para permitir estos descubiertos.
'''
def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args, **kwargs):
        print("El salario actual es de: ", funcion_parametro(*args, **kwargs), "euros")
    return funcion_interior

@funcion_decoradora
def operaciones(saldo):

    print("1. Ingresar dinero en cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Salir")
    opcion = int(input("Elige una opción: "))
    if opcion == 1:
        ingreso = float(input("Cantidad a ingresar: "))
        saldo = saldo + ingreso
        operaciones(saldo)
    elif opcion == 2:
        retirada = float(input("Cantidad a retirar: "))
        if saldo - retirada < 0:
            print("No se puede retirar esa cantidad")
            operaciones(saldo)
        else:
            saldo = saldo - retirada
            operaciones(saldo)
    elif opcion == 3:
        print("Gracias por utilizar nuestros servicios")
    else:
        print("Opción no válida")
        operaciones(saldo)
class Cuenta_Bancaria:
    def datos(self):
        self.nombre = input("Nombre del titular de la cuenta: ")
        self.saldo = float(input("Saldo actual de la cuenta: "))
        operaciones(self.saldo)

cuenta1 = Cuenta_Bancaria()
print(cuenta1.datos())

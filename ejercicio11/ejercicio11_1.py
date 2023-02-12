#Calcular el sueldo de un empleado que trabaja 35 horas a la semana, si el empleado trabaja más de 44 horas se le paga 1.5 veces el sueldo por hora, si trabaja entre 36 y 43 horas se le paga 1.25 veces el sueldo por hora, si trabaja menos de 35 horas no se le paga nada por las horas extras.

def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args):
        print("Segun el numero de horas trabajadas, el sueldo es: ", funcion_parametro(*args), "€")
    return funcion_interior


@funcion_decoradora
def calcularSueldo(horas, sueldo):
    if horas >= 44:
        return (sueldo)/35*1.5*(horas-35)
    elif horas >= 36 and horas<= 43:
        return (sueldo)/35*1.25*(horas-35)
    elif horas <=35:
        print("El empleado cobrará nada por las horas extras")
print("CALCULADORA DE SUELDO")
horas = int(input("Ingrese las horas trabajadas: "))
sueldo = int(input("Ingrese el sueldo por hora: "))
calcularSueldo(horas, sueldo)


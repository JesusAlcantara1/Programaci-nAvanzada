from escuela.escuela import Escuela
from Estudiantes.estudiante import Estudiante
from datetime import datetime 

escuela = Escuela()

while True: 
    print ("----------------------------------------")
    print ("\n***Mindbox***")
    print ("1. Registrar estudiante")
    print ("2. Registrar maestro")
    print ("3. Registrar materia")
    print ("4. Registrar horario")
    print ("5. Registrar grupo")
    print ("6. Salir")
    print ("-----------------------------------------")

    opcion = input ("Ingresa una opcion para continuar: ")

    if opcion == "1":
        print ("--------------------------------")
        print ("Elegiste la opción de elegir estudiante")

        numero_control = escuela.generar_numero_control()
        print("El numero de control es: ")
        print(numero_control)

        nombre = input(("Ingrese nombre del estudiante:  "))
        apellido = input(("Ingrese apellido del estudiante:  "))
        curp = input(("Ingrese la curp del estudiante:  "))
        ano = input(("Ingrese año de nacimiento del estudiante:  "))
        mes = input(("Ingrese el mes de nacimiento del estudiante:  "))
        dia = input(("Ingrese el dia del nacimiento del estudiante:  "))
        fecha_nacimiento = datetime(ano, mes, dia)


        if opcion == "2":
            pass


        if opcion == "3":
            pass


        if opcion == "4":
            pass


        if opcion == "5":
            pass


        if opcion == "6":
            print("-------------------------------------")
            print("Hasta luego")
            break
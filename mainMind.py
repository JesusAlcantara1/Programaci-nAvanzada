from escuela.escuela import Escuela
from Estudiantes.estudiante import Estudiante
from datetime import datetime 
from Maestros.maestro import maestro

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
        print ("Elegiste la opción de registrar estudiante")

        numero_control = escuela.generar_numero_control_estudiante()
        print("El numero de control es: ")
        print(numero_control)

        nombre = input(("Ingrese nombre del estudiante:  "))
        apellido = input(("Ingrese apellido del estudiante:  "))
        curp = input(("Ingrese la curp del estudiante:  "))
        ano = int(input("Ingrese año de nacimiento del estudiante:  "))
        mes = int(input("Ingrese el mes de nacimiento del estudiante:  "))
        dia = int(input("Ingrese el dia del nacimiento del estudiante:  "))
        fecha_nacimiento = datetime(ano, mes, dia)

    elif opcion =="2":
                
                print (("\n Seleccionaste la opcion para registrar maestros"))
                nombre = input (("Ingresa el nombre del docente:  "))
                apellido = input (("Ingresa el apellido del docente:  "))
                rfc = input (("Ingresa el rfc del docente:  "))
                ano = int (input("Ingresa el ano de nacimiento del docente:  "))
                sueldo = input (("Ingresa el sueldo del docente:  "))
            

                maestro = maestro(numero_control="",nombre=nombre, ano_nacimiento=ano, apellido=apellido, rfc=rfc, sueldo=sueldo)

                generar_numero_control_maestro = escuela.generar_numero_control_maestro(maestro)
                maestro.numero_control=generar_numero_control_maestro

                escuela.registrar_maestro(maestro)

                print("El numero de control generado es:  ")
                print(generar_numero_control_maestro)


    elif opcion =="3":
        pass

    elif opcion == "4":
            pass


    elif opcion == "5":
            pass


    elif opcion == "6":
            print("-------------------------------------")
            print("Hasta luego")
            break
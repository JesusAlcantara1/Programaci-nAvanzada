from escuela.escuela import Escuela
from Estudiantes.estudiante import Estudiante
from datetime import datetime
from Maestros.maestro import maestro
from Materias.materia import Materia


escuela = Escuela()

while True: 
    print ("----------------------------------------")
    print ("\n***Mindbox***")
    print ("1. Registrar estudiante")
    print ("2. Registrar maestro")
    print ("3. Registrar materia")
    print ("4. Registrar horario")
    print ("5. Registrar grupo")
    print ("6. Mostrar estudiantes")
    print ("7. Mostrar maestros")
    print ("8. Mostrar materias")
    print ("9. Mostrar grupos")
    print ("10. Eliminar estudiantes")
    print ("11. Eliminar maestros")
    print ("12. Eliminar materias")
    print ("13. Salir")




    print ("-----------------------------------------")

    opcion = input ("Ingresa una opcion para continuar: ")

    if opcion == "1":
        print ("--------------------------------")
        print ("Elegiste la opción de registrar estudiante")

        numero_control = escuela.generar_numero_control()
        print("El numero de control es: ")
        print(numero_control)

        nombre = input(("Ingrese nombre del estudiante:  "))
        apellido = input(("Ingrese apellido del estudiante:  "))
        curp = input(("Ingrese la curp del estudiante:  "))
        ano = int(input("Ingrese año de nacimiento del estudiante:  "))
        mes = int(input("Ingrese el mes de nacimiento del estudiante:  "))
        dia = int(input("Ingrese el dia del nacimiento del estudiante:  "))
        fecha_nacimiento = datetime(ano, mes, dia)


    elif opcion == "2":
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



    elif opcion == "3":
        print("Seleccionaste Registrar materia")
        nombre = input("Ingresa el nombre del la materia: ")
        descripcion = input("Ingresa la descripción de la materia: ")
        semestre = int(input("Ingresa el semestre de la materia: "))
        creditos = int(input("Ingresa el número de créditos del semestre: "))
        
        id = escuela.generar_id_materia(nombre, semestre, creditos)
        print("ID de la materia: ",id)
        escuela.registrar_materia(materia = Materia)

    elif opcion == "4":
            print("\nSeleccionaste la opcion de registrar horario\n")


    elif opcion == "5":
            print("\nSeleccionaste la opcion de registrar grupo\n")
    
    elif opcion == "6":
            escuela.listar_estudiantes()

    elif opcion == "7":
            escuela.listar_maestros()
    
    elif opcion == "8":
            escuela.listar_materias()
    
    elif opcion == "9":
            escuela.lista_estudiantes
    
    elif opcion == "10":
        print("\nSeleccionaste la opcion para eliminar un estudiante \n")
        numero_control = input("\nIngresa el numero de control del estudiante: ")
        escuela.eliminar_estudiante(numero_control=numero_control)
    
    elif opcion == "11":
        print("\nSeleccionaste la opcion para eliminar un maestro \n")
        numero_controlp = input("\nIngresa el numero de control del maestro: ")
        escuela.eliminar_maestro(numero_controlp=numero_controlp)
    
    elif opcion == "12":
        print("\nSeleccionaste la opcion para eliminar una materia \n")
        id_materia = input("\nIngresa el ID de la materia: ")
        escuela.eliminar_materia(id_materia=id_materia)
    


    elif opcion == "13":
            print("-------------------------------------")
            print("Hasta luego")
            break